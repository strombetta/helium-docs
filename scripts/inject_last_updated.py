#!/usr/bin/env python3
"""Inject per-page last-updated metadata into generated DocFX HTML."""

from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path, PurePosixPath
from typing import Mapping


DEFAULT_MANIFEST = Path("last-updated.json")
DEFAULT_SITE = Path("_site")
LAST_UPDATED_MARKER = "data-helium-last-updated"
H1_RE = re.compile(r"(<h1\b[^>]*>.*?</h1>)", re.IGNORECASE | re.DOTALL)


def format_en_us(iso_date: str) -> str:
    """Format an ISO calendar date as an en-US long date."""
    parsed = date.fromisoformat(iso_date)
    return f"{parsed.strftime('%B')} {parsed.day}, {parsed.year}"


def output_file(site: Path, url_path: str) -> Path:
    """Resolve a manifest URL path to its generated HTML file."""
    relative = PurePosixPath(url_path.lstrip("/"))
    if url_path.endswith("/"):
        relative /= "index.html"
    return site.joinpath(*relative.parts)


def page_files(site: Path, manifest: Mapping[str, str]) -> dict[Path, str]:
    """Deduplicate manifest URL aliases into generated HTML files."""
    pages: dict[Path, str] = {}
    for url_path, updated in manifest.items():
        candidate = output_file(site, url_path)
        current = pages.get(candidate)
        if current is not None and current != updated:
            raise ValueError(f"Conflicting dates for {candidate}: {current} and {updated}")
        pages[candidate] = updated
    return pages


def render_last_updated(iso_date: str) -> str:
    """Return semantic last-updated markup for one page."""
    return (
        f'<p class="helium-last-updated" {LAST_UPDATED_MARKER}>'
        f'Last updated: <time datetime="{iso_date}">{format_en_us(iso_date)}</time>'
        "</p>"
    )


def inject_markup(html: str, iso_date: str) -> str:
    """Insert last-updated markup after the first H1, preserving idempotency."""
    if LAST_UPDATED_MARKER in html:
        return html

    match = H1_RE.search(html)
    if not match:
        raise ValueError("Generated page does not contain an H1 element")

    markup = render_last_updated(iso_date)
    return html[: match.end()] + "\n" + markup + html[match.end() :]


def inject_site(site: Path, manifest: Mapping[str, str]) -> int:
    """Inject metadata into every generated page represented by the manifest."""
    updated_count = 0
    missing: list[Path] = []

    for page, iso_date in page_files(site, manifest).items():
        if not page.is_file():
            missing.append(page)
            continue

        html = page.read_text(encoding="utf-8")
        updated_html = inject_markup(html, iso_date)
        if updated_html != html:
            page.write_text(updated_html, encoding="utf-8")
            updated_count += 1

    if missing:
        paths = ", ".join(str(path) for path in missing[:5])
        suffix = "" if len(missing) <= 5 else f" and {len(missing) - 5} more"
        raise FileNotFoundError(f"Generated pages missing: {paths}{suffix}")

    return updated_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root. Defaults to the parent of the scripts directory.",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=DEFAULT_MANIFEST,
        help="Manifest path, relative to the repository root by default.",
    )
    parser.add_argument(
        "--site",
        type=Path,
        default=DEFAULT_SITE,
        help="Generated site directory, relative to the repository root by default.",
    )
    return parser.parse_args()


def resolve(root: Path, path: Path) -> Path:
    return path if path.is_absolute() else root / path


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    manifest_path = resolve(root, args.manifest)
    site = resolve(root, args.site)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise TypeError("Last-updated manifest must be a JSON object")
    count = inject_site(site, manifest)
    print(f"Injected last-updated metadata into {count} page(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
