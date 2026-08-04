#!/usr/bin/env python3
"""Generate per-page last-updated metadata from the Git history."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Callable, Iterable


PUBLIC_ROOTS = ("articles", "api", "reference")
PUBLIC_SUFFIXES = {".md", ".yml", ".yaml"}
DEFAULT_OUTPUT = Path("last-updated.json")


def posix(path: Path) -> str:
    return path.as_posix()


def iter_public_pages(root: Path) -> list[Path]:
    """Return source files that DocFX can publish as standalone pages."""
    candidates: list[Path] = []
    for filename in ("index.md", "404.md"):
        path = root / filename
        if path.is_file():
            candidates.append(path)

    for public_root in PUBLIC_ROOTS:
        directory = root / public_root
        if not directory.is_dir():
            continue
        candidates.extend(
            path
            for path in directory.rglob("*")
            if path.is_file()
            and path.suffix.lower() in PUBLIC_SUFFIXES
            and path.name.lower() not in {"toc.yml", "toc.yaml"}
        )

    return sorted(
        set(candidates),
        key=lambda path: posix(path.relative_to(root)),
    )


def output_urls(path: PurePosixPath) -> tuple[str, ...]:
    """Return URL path variants that can identify a generated DocFX page."""
    html_path = path.with_suffix(".html")
    canonical = "/" + str(html_path).lstrip("/")

    if str(path) == "index.md":
        return ("/", "/index.html")
    if path.name == "index.md":
        directory = "/" + str(path.parent).strip("/") + "/"
        return (directory, canonical)
    return (canonical,)


def git_last_updated(root: Path, relative_path: Path) -> str | None:
    """Return the last commit date for a file as YYYY-MM-DD."""
    command = [
        "git",
        "-C",
        str(root),
        "log",
        "-1",
        "--follow",
        "--format=%cI",
        "--",
        posix(relative_path),
    ]
    result = subprocess.run(
        command,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git log failed")

    timestamp = result.stdout.strip()
    if not timestamp:
        return None
    return timestamp[:10]


def fallback_date(path: Path) -> str:
    """Provide a deterministic date for an uncommitted local page."""
    source_date_epoch = os.environ.get("SOURCE_DATE_EPOCH")
    if source_date_epoch:
        timestamp = datetime.fromtimestamp(int(source_date_epoch), tz=timezone.utc)
    else:
        timestamp = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    return timestamp.date().isoformat()


def build_manifest(
    root: Path,
    pages: Iterable[Path] | None = None,
    date_resolver: Callable[[Path, Path], str | None] = git_last_updated,
) -> dict[str, str]:
    manifest: dict[str, str] = {}
    for source in pages if pages is not None else iter_public_pages(root):
        relative = source.relative_to(root)
        updated = date_resolver(root, relative) or fallback_date(source)
        for url in output_urls(PurePosixPath(posix(relative))):
            manifest[url] = updated
    return dict(sorted(manifest.items()))


def write_manifest(root: Path, output: Path) -> Path:
    destination = output if output.is_absolute() else root / output
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        json.dumps(build_manifest(root), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return destination


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root. Defaults to the parent of the scripts directory.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Manifest path, relative to the repository root by default.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    destination = write_manifest(root, args.output)
    print(f"Generated {destination.relative_to(root)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
