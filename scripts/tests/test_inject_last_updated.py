from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "inject_last_updated.py"
SPEC = importlib.util.spec_from_file_location("inject_last_updated", MODULE_PATH)
assert SPEC and SPEC.loader
injector = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = injector
SPEC.loader.exec_module(injector)


class InjectLastUpdatedTests(unittest.TestCase):
    def test_format_en_us_uses_long_month_name(self) -> None:
        self.assertEqual("August 4, 2026", injector.format_en_us("2026-08-04"))

    def test_output_file_resolves_directory_and_html_urls(self) -> None:
        site = Path("_site")
        self.assertEqual(site / "index.html", injector.output_file(site, "/"))
        self.assertEqual(
            site / "articles" / "overview" / "index.html",
            injector.output_file(site, "/articles/overview/"),
        )
        self.assertEqual(
            site / "articles" / "overview" / "what-is-helium.html",
            injector.output_file(site, "/articles/overview/what-is-helium.html"),
        )

    def test_inject_markup_is_semantic_and_idempotent(self) -> None:
        original = "<article><h1>Example</h1><p>Body</p></article>"
        updated = injector.inject_markup(original, "2026-08-04")
        self.assertIn("data-helium-last-updated", updated)
        self.assertIn(
            '<time datetime="2026-08-04">August 4, 2026</time>',
            updated,
        )
        self.assertEqual(updated, injector.inject_markup(updated, "2026-08-04"))

    def test_inject_site_updates_each_page_once_for_aliases(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory) / "_site"
            section = site / "articles" / "overview"
            section.mkdir(parents=True)
            page = section / "index.html"
            page.write_text("<html><h1>Overview</h1></html>", encoding="utf-8")
            manifest = {
                "/articles/overview/": "2026-07-31",
                "/articles/overview/index.html": "2026-07-31",
            }
            self.assertEqual(1, injector.inject_site(site, manifest))
            result = page.read_text(encoding="utf-8")
            self.assertEqual(1, result.count(injector.LAST_UPDATED_MARKER))

    def test_inject_site_reports_missing_generated_pages(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory) / "_site"
            site.mkdir()
            with self.assertRaises(FileNotFoundError):
                injector.inject_site(site, {"/missing.html": "2026-08-04"})


if __name__ == "__main__":
    unittest.main()
