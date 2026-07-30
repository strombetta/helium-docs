#!/usr/bin/env python3
"""Generate the Helium documentation content inventory.

The generator uses only the Python standard library. It inventories published
Markdown sources, resolves direct Markdown references from DocFX TOC files,
classifies page completeness, proposes target locations, and writes three
reviewable planning artifacts.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable


REQUIRED_OUTPUTS = (
    "content-inventory.yml",
    "url-migration-map.yml",
    "content-coverage.md",
)

PUBLIC_ROOTS = ("articles", "reference", "api")
BUILD_AREAS = {
    "configuration",
    "identity",
    "onboarding",
    "organizations",
    "authorization",
    "billing",
    "entitlements",
    "communications",
}
OPERATE_AREAS = {
    "deployment",
    "security",
    "diagnostics",
    "performance",
    "persistence",
    "durable-processing",
    "hosting",
    "troubleshooting",
}
P0_AREAS = {
    "product",
    "getting-started",
    "architecture",
    "configuration",
    "identity",
    "organizations",
    "authorization",
    "deployment",
    "security",
    "troubleshooting",
}
P1_AREAS = {
    "onboarding",
    "entitlements",
    "communications",
    "persistence",
    "diagnostics",
    "durable-processing",
    "contributing",
    "compatibility",
    "api",
}
ACTION_VERBS = {
    "add",
    "apply",
    "build",
    "complete",
    "configure",
    "create",
    "customize",
    "define",
    "deploy",
    "diagnose",
    "enable",
    "implement",
    "install",
    "invite",
    "manage",
    "migrate",
    "protect",
    "publish",
    "register",
    "replace",
    "resolve",
    "run",
    "select",
    "test",
    "transfer",
    "troubleshoot",
    "upgrade",
    "use",
    "validate",
    "verify",
}
DOC_CONTRIBUTION_FILES = {
    "repository-structure.md",
    "build-locally.md",
    "documentation-architecture.md",
    "authoring-conventions.md",
    "toc-conventions.md",
    "metadata-reference.md",
    "api-generation.md",
    "link-validation.md",
    "preview-environments.md",
    "publication-process.md",
    "issues-and-pull-requests.md",
}

FRONT_MATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.DOTALL)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
HREF_RE = re.compile(r"^\s*href:\s*['\"]?([^'\"\s#]+)", re.MULTILINE)
WORD_RE = re.compile(r"\b[\w][\w'.-]*\b", re.UNICODE)
CODE_FENCE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
PLACEHOLDER_RE = re.compile(
    r"\b(?:todo|tbd|placeholder|coming soon|content pending|to be written)\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class TocScan:
    references: dict[str, list[str]]
    missing_targets: list[dict[str, str]]


def posix(path: Path) -> str:
    return path.as_posix()


def parse_front_matter(text: str) -> tuple[dict[str, object], str]:
    """Parse the subset of YAML front matter used by this repository."""
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}, text

    data: dict[str, object] = {}
    current_list: str | None = None
    for raw_line in match.group(1).splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        list_match = re.match(r"^\s+-\s+(.+?)\s*$", line)
        if list_match and current_list:
            value = list_match.group(1).strip().strip("'\"")
            cast = data.setdefault(current_list, [])
            if isinstance(cast, list):
                cast.append(value)
            continue
        key_match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", line)
        if not key_match:
            current_list = None
            continue
        key, raw_value = key_match.groups()
        if raw_value == "":
            data[key] = []
            current_list = key
            continue
        current_list = None
        value = raw_value.strip().strip("'\"")
        if value.lower() in {"true", "false"}:
            data[key] = value.lower() == "true"
        else:
            data[key] = value
    return data, text[match.end() :]


def normalize_markdown_body(body: str) -> str:
    body = CODE_FENCE_RE.sub(" ", body)
    body = re.sub(r"<!--.*?-->", " ", body, flags=re.DOTALL)
    body = re.sub(r"!\[[^]]*\]\([^)]+\)", " ", body)
    body = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", body)
    body = re.sub(r"[`*_>#|]", " ", body)
    return body


def content_metrics(body: str) -> dict[str, int]:
    headings = HEADING_RE.findall(body)
    normalized = normalize_markdown_body(body)
    return {
        "word_count": len(WORD_RE.findall(normalized)),
        "heading_count": len(headings),
        "h2_count": sum(1 for level, _ in headings if len(level) == 2),
    }


def classify_completeness(body: str, metrics: dict[str, int]) -> str:
    stripped = body.strip()
    if not stripped:
        return "empty"
    if PLACEHOLDER_RE.search(stripped):
        return "placeholder"
    if metrics["word_count"] < 40 and metrics["heading_count"] <= 1:
        return "placeholder"
    if metrics["word_count"] < 180:
        return "outline"
    return "substantial"


def first_h1(body: str) -> str | None:
    for level, heading in HEADING_RE.findall(body):
        if len(level) == 1:
            return re.sub(r"\s+#+\s*$", "", heading).strip()
    return None


def iter_public_markdown(root: Path) -> list[Path]:
    files: list[Path] = []
    root_index = root / "index.md"
    if root_index.exists():
        files.append(root_index)
    for public_root in PUBLIC_ROOTS:
        base = root / public_root
        if base.exists():
            files.extend(base.rglob("*.md"))
    return sorted(
        {
            path
            for path in files
            if "_site" not in path.parts
            and ".authoring" not in path.parts
            and not any(part.startswith(".") for part in path.relative_to(root).parts)
        },
        key=lambda item: posix(item.relative_to(root)),
    )


def scan_tocs(root: Path) -> TocScan:
    references: dict[str, list[str]] = defaultdict(list)
    missing: list[dict[str, str]] = []
    for toc in sorted(root.rglob("toc.yml")):
        if "_site" in toc.parts:
            continue
        text = toc.read_text(encoding="utf-8")
        toc_rel = posix(toc.relative_to(root))
        for href in HREF_RE.findall(text):
            if href.startswith(("http://", "https://", "xref:")):
                continue
            clean = href.split("?", 1)[0].split("#", 1)[0]
            if not clean or clean.endswith("/"):
                continue
            resolved = (toc.parent / clean).resolve()
            try:
                rel = resolved.relative_to(root.resolve())
            except ValueError:
                missing.append({"toc": toc_rel, "href": href, "reason": "outside-repository"})
                continue
            rel_text = posix(rel)
            if rel.suffix.lower() == ".md":
                references[rel_text].append(toc_rel)
                if not resolved.exists():
                    missing.append({"toc": toc_rel, "href": href, "reason": "missing-file"})
    return TocScan(
        references={key: sorted(value) for key, value in sorted(references.items())},
        missing_targets=sorted(missing, key=lambda item: (item["toc"], item["href"])),
    )


def current_url(path: PurePosixPath) -> str:
    if str(path) == "index.md":
        return "/"
    if path.name == "index.md":
        return "/" + str(path.parent).strip("/") + "/"
    return "/" + str(path.with_suffix(".html")).strip("/")


def infer_area(path: PurePosixPath, metadata: dict[str, object]) -> str:
    metadata_area = metadata.get("area")
    if isinstance(metadata_area, str) and metadata_area:
        return metadata_area
    if str(path) == "index.md":
        return "product"
    parts = path.parts
    if not parts:
        return "product"
    if parts[0] == "reference":
        return "api" if "api" in parts else "compatibility"
    if parts[0] == "api":
        return "api"
    if len(parts) >= 2 and parts[0] == "articles":
        section = parts[1]
        return {
            "overview": "product",
            "whats-new": "compatibility",
            "fundamentals": "architecture",
            "communications": "communications",
            "contributing": "contributing",
        }.get(section, section)
    return "product"


def infer_content_type(
    path: PurePosixPath, metadata: dict[str, object], title: str
) -> str:
    metadata_type = metadata.get("content_type")
    if isinstance(metadata_type, str) and metadata_type:
        return metadata_type
    name = path.name.lower()
    parts = set(path.parts)
    if name == "index.md":
        return "index"
    if "troubleshooting" in parts:
        return "troubleshooting"
    if "reference" in parts or path.parts[0] == "reference":
        return "reference"
    if "whats-new" in parts or "release" in name or "breaking" in name:
        return "release"
    if "overview" in parts or name.startswith(("what-is-", "why-use-", "scope-")):
        return "overview"
    if "fundamentals" in parts:
        return "concept"
    if "getting-started" in parts:
        return "tutorial"
    first_word = re.split(r"[^A-Za-z]+", title.strip().lower(), maxsplit=1)[0]
    if first_word in ACTION_VERBS:
        return "how-to"
    return "concept"


def proposed_location(path: PurePosixPath) -> tuple[str, str]:
    """Return the proposed path and canonical top-level section."""
    if str(path) == "index.md":
        return "index.md", "Home"
    if path.parts[0] == "reference":
        return str(path), "Reference"
    if path.parts[0] == "api":
        return str(path), "Reference"
    if len(path.parts) < 3 or path.parts[0] != "articles":
        return str(path), "Reference"

    current = path.parts[1]
    remainder = PurePosixPath(*path.parts[2:])
    if current == "overview":
        return str(path), "Overview"
    if current == "whats-new":
        return str(PurePosixPath("articles/overview/whats-new") / remainder), "Overview"
    if current == "getting-started":
        return str(path), "Get started"
    if current == "fundamentals":
        return str(path), "Fundamentals"
    if current in BUILD_AREAS:
        return str(PurePosixPath("articles/build") / current / remainder), "Build with Helium"
    if current == "testing":
        return str(PurePosixPath("articles/build/testing") / remainder), "Build with Helium"
    if current == "extensibility":
        return str(PurePosixPath("articles/extend") / remainder), "Extend and customize"
    if current in OPERATE_AREAS:
        return str(PurePosixPath("articles/operate") / current / remainder), "Deploy and operate"
    if current == "contributing":
        if remainder.name == "index.md":
            return "articles/contribute/index.md", "Contribute"
        subgroup = "documentation" if remainder.name in DOC_CONTRIBUTION_FILES else "framework"
        return str(PurePosixPath("articles/contribute") / subgroup / remainder), "Contribute"
    return str(path), "Reference"


def priority_for(area: str, section: str, path: PurePosixPath) -> str:
    if str(path) == "index.md" or area in P0_AREAS:
        return "P0"
    if area in P1_AREAS or section == "Reference":
        return "P1"
    return "P2"


def source_hint(area: str, path: PurePosixPath) -> str:
    if area == "contributing":
        return "repository policy and workflow"
    if area in {"product", "architecture", "compatibility"}:
        return "framework specifications and accepted ADRs"
    if area == "api" or path.parts[0] == "reference":
        return "public API, constants, and generated reference inputs"
    return "framework code, tests, configuration, and specifications"


def proposed_action(completeness: str, current: str, proposed: str) -> str:
    if completeness in {"empty", "placeholder"}:
        return "REWRITE"
    if current != proposed:
        return "MOVE"
    if completeness == "outline":
        return "REWRITE"
    return "KEEP"


def inventory_repository(root: Path) -> tuple[list[dict[str, object]], TocScan]:
    toc_scan = scan_tocs(root)
    entries: list[dict[str, object]] = []
    for file_path in iter_public_markdown(root):
        relative = PurePosixPath(posix(file_path.relative_to(root)))
        text = file_path.read_text(encoding="utf-8")
        metadata, body = parse_front_matter(text)
        metrics = content_metrics(body)
        completeness = classify_completeness(body, metrics)
        title = first_h1(body) or str(metadata.get("title") or relative.stem.replace("-", " ").title())
        area = infer_area(relative, metadata)
        content_type = infer_content_type(relative, metadata, title)
        proposed_path, proposed_section = proposed_location(relative)
        current_path = str(relative)
        refs = toc_scan.references.get(current_path, [])
        entry: dict[str, object] = {
            "current_path": current_path,
            "current_url": current_url(relative),
            "title": title,
            "toc_referenced": bool(refs) or current_path == "index.md",
            "toc_files": refs,
            "orphan_candidate": not refs and current_path != "index.md",
            "front_matter": bool(metadata),
            "content_type": content_type,
            "area": area,
            "completeness": completeness,
            "word_count": metrics["word_count"],
            "heading_count": metrics["heading_count"],
            "proposed_section": proposed_section,
            "proposed_path": proposed_path,
            "proposed_url": current_url(PurePosixPath(proposed_path)),
            "action": proposed_action(completeness, current_path, proposed_path),
            "priority": priority_for(area, proposed_section, relative),
            "source": source_hint(area, relative),
            "owner": area,
            "target_version": str(metadata.get("version") or "preview"),
            "dependencies": [],
        }
        entries.append(entry)
    return entries, toc_scan


def json_yaml(data: object) -> str:
    """JSON is valid YAML 1.2 and keeps generation dependency-free."""
    return json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False) + "\n"


def migration_entries(entries: Iterable[dict[str, object]]) -> list[dict[str, object]]:
    migrations: list[dict[str, object]] = []
    for entry in entries:
        if entry["current_path"] == entry["proposed_path"]:
            continue
        migrations.append(
            {
                "current_path": entry["current_path"],
                "old_url": entry["current_url"],
                "proposed_path": entry["proposed_path"],
                "new_url": entry["proposed_url"],
                "redirect_required": True,
                "status": "planned",
                "reason": f"Move into canonical section: {entry['proposed_section']}",
            }
        )
    return sorted(migrations, key=lambda item: str(item["old_url"]))


def markdown_table(headers: list[str], rows: Iterable[Iterable[object]]) -> str:
    rendered = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        rendered.append("| " + " | ".join(str(value).replace("|", "\\|") for value in row) + " |")
    return "\n".join(rendered)


def coverage_report(entries: list[dict[str, object]], toc_scan: TocScan) -> str:
    by_status = Counter(str(item["completeness"]) for item in entries)
    by_action = Counter(str(item["action"]) for item in entries)
    by_priority = Counter(str(item["priority"]) for item in entries)
    by_section = Counter(str(item["proposed_section"]) for item in entries)
    by_type = Counter(str(item["content_type"]) for item in entries)
    by_area = Counter(str(item["area"]) for item in entries)
    empty_like = [item for item in entries if item["completeness"] in {"empty", "placeholder"}]
    orphan = [item for item in entries if item["orphan_candidate"]]
    no_front_matter = [item for item in entries if not item["front_matter"]]
    p0_rewrites = [
        item
        for item in entries
        if item["priority"] == "P0" and item["action"] in {"REWRITE", "MOVE"}
    ]

    lines = [
        "# Content coverage baseline",
        "",
        "This report is generated by `scripts/generate_content_inventory.py`. It is a planning baseline, not a claim that every classification is final. Review content type, ownership, move, merge, split, and rewrite decisions before structural migration.",
        "",
        "## Summary",
        "",
        markdown_table(
            ["Metric", "Count"],
            [
                ("Public Markdown pages", len(entries)),
                ("TOC-referenced pages", sum(1 for item in entries if item["toc_referenced"])),
                ("Orphan candidates", len(orphan)),
                ("Pages without front matter", len(no_front_matter)),
                ("Empty or placeholder pages", len(empty_like)),
                ("Planned URL moves", len(migration_entries(entries))),
                ("Broken Markdown TOC targets", len(toc_scan.missing_targets)),
            ],
        ),
        "",
        "## Completeness",
        "",
        markdown_table(["Classification", "Pages"], sorted(by_status.items())),
        "",
        "## Proposed action",
        "",
        markdown_table(["Action", "Pages"], sorted(by_action.items())),
        "",
        "## Priority",
        "",
        markdown_table(["Priority", "Pages"], sorted(by_priority.items())),
        "",
        "## Canonical section",
        "",
        markdown_table(["Section", "Pages"], sorted(by_section.items())),
        "",
        "## Editorial type",
        "",
        markdown_table(["Content type", "Pages"], sorted(by_type.items())),
        "",
        "## Area",
        "",
        markdown_table(["Area", "Pages"], sorted(by_area.items())),
        "",
        "## P0 pages requiring rewrite or move",
        "",
        markdown_table(
            ["Current path", "Completeness", "Action", "Proposed path"],
            (
                (item["current_path"], item["completeness"], item["action"], item["proposed_path"])
                for item in p0_rewrites
            ),
        )
        if p0_rewrites
        else "No P0 rewrite or move candidates were detected.",
        "",
        "## Empty and placeholder pages",
        "",
        markdown_table(
            ["Path", "Priority", "Proposed section"],
            ((item["current_path"], item["priority"], item["proposed_section"]) for item in empty_like),
        )
        if empty_like
        else "No empty or placeholder pages were detected.",
        "",
        "## Orphan candidates",
        "",
        "A page is an orphan candidate when no direct Markdown `href` in a `toc.yml` points to it. Pages intentionally reached only through contextual links require manual review before removal.",
        "",
        markdown_table(
            ["Path", "Completeness", "Action"],
            ((item["current_path"], item["completeness"], item["action"]) for item in orphan),
        )
        if orphan
        else "No orphan candidates were detected.",
        "",
        "## Missing TOC targets",
        "",
        markdown_table(
            ["TOC", "Href", "Reason"],
            ((item["toc"], item["href"], item["reason"]) for item in toc_scan.missing_targets),
        )
        if toc_scan.missing_targets
        else "No missing Markdown TOC targets were detected.",
        "",
        "## Interpretation rules",
        "",
        "- `empty`: no substantive body content.",
        "- `placeholder`: fewer than 40 words with at most one heading, or explicit placeholder language.",
        "- `outline`: fewer than 180 words but more than a placeholder.",
        "- `substantial`: at least 180 words; technical accuracy still requires review.",
        "- `MOVE`: the proposed canonical path differs from the current path.",
        "- `REWRITE`: the page is empty, a placeholder, or an outline.",
        "- `KEEP`: the page is substantial and already located in a stable canonical section.",
        "",
        "## Next use",
        "",
        "Use `content-inventory.yml` for page-level decisions and `url-migration-map.yml` before changing paths or the primary TOC. Amend individual records when manual review identifies a merge, split, archive, or removal decision that cannot be inferred mechanically.",
        "",
    ]
    return "\n".join(lines)


def generated_outputs(root: Path) -> dict[str, str]:
    entries, toc_scan = inventory_repository(root)
    inventory = {
        "inventory_version": 1,
        "classification": {
            "actions": ["KEEP", "MOVE", "REWRITE", "SPLIT", "MERGE", "CREATE", "REDIRECT", "ARCHIVE", "REMOVE"],
            "completeness": ["empty", "placeholder", "outline", "substantial"],
            "priorities": ["P0", "P1", "P2", "P3"],
        },
        "summary": {
            "pages": len(entries),
            "toc_referenced": sum(1 for item in entries if item["toc_referenced"]),
            "orphan_candidates": sum(1 for item in entries if item["orphan_candidate"]),
            "without_front_matter": sum(1 for item in entries if not item["front_matter"]),
            "empty_or_placeholder": sum(1 for item in entries if item["completeness"] in {"empty", "placeholder"}),
        },
        "pages": entries,
        "missing_toc_targets": toc_scan.missing_targets,
    }
    migration = {
        "migration_map_version": 1,
        "policy": {
            "redirect_required_for_published_moves": True,
            "redirect_status": ["planned", "implemented", "verified"],
        },
        "moves": migration_entries(entries),
    }
    return {
        "content-inventory.yml": json_yaml(inventory),
        "url-migration-map.yml": json_yaml(migration),
        "content-coverage.md": coverage_report(entries, toc_scan),
    }


def write_outputs(root: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, content in generated_outputs(root).items():
        (output_dir / name).write_text(content, encoding="utf-8")


def check_outputs(root: Path, output_dir: Path) -> int:
    expected = generated_outputs(root)
    differences: list[str] = []
    for name, content in expected.items():
        target = output_dir / name
        if not target.exists():
            differences.append(f"missing: {target}")
        elif target.read_text(encoding="utf-8") != content:
            differences.append(f"out of date: {target}")
    if differences:
        for difference in differences:
            print(f"ERROR: {difference}", file=sys.stderr)
        print(
            "Run `python3 scripts/generate_content_inventory.py` and commit the generated planning files.",
            file=sys.stderr,
        )
        return 1
    print(f"Content inventory is current ({len(expected)} generated files).")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root. Defaults to the parent of scripts/.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("planning"),
        help="Output directory relative to the repository root unless absolute.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Fail if committed output differs from the generated inventory.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    output_dir = args.output_dir
    if not output_dir.is_absolute():
        output_dir = root / output_dir
    if args.check:
        return check_outputs(root, output_dir)
    write_outputs(root, output_dir)
    print(f"Generated content inventory in {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
