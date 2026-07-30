from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path, PurePosixPath


MODULE_PATH = Path(__file__).resolve().parents[1] / "generate_content_inventory.py"
SPEC = importlib.util.spec_from_file_location("generate_content_inventory", MODULE_PATH)
assert SPEC and SPEC.loader
inventory = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inventory)


class ContentInventoryTests(unittest.TestCase):
    def test_parse_front_matter_supports_scalars_and_lists(self) -> None:
        metadata, body = inventory.parse_front_matter(
            """---
 title: Example page
 content_type: concept
 audience:
   - developer
   - operator
 migration_required: true
 ---
 # Example page
 """.replace("\n ", "\n")
        )
        self.assertEqual("Example page", metadata["title"])
        self.assertEqual(["developer", "operator"], metadata["audience"])
        self.assertTrue(metadata["migration_required"])
        self.assertIn("# Example page", body)

    def test_completeness_classification(self) -> None:
        empty_metrics = inventory.content_metrics("")
        self.assertEqual("empty", inventory.classify_completeness("", empty_metrics))

        placeholder = "# Placeholder\n\nTODO"
        self.assertEqual(
            "placeholder",
            inventory.classify_completeness(placeholder, inventory.content_metrics(placeholder)),
        )

        substantial = "# Page\n\n" + "word " * 200
        self.assertEqual(
            "substantial",
            inventory.classify_completeness(substantial, inventory.content_metrics(substantial)),
        )

    def test_proposed_location_maps_capabilities_and_operations(self) -> None:
        self.assertEqual(
            ("articles/build/authorization/protect-endpoints.md", "Build with Helium"),
            inventory.proposed_location(
                PurePosixPath("articles/authorization/protect-endpoints.md")
            ),
        )
        self.assertEqual(
            ("articles/operate/deployment/containers.md", "Deploy and operate"),
            inventory.proposed_location(PurePosixPath("articles/deployment/containers.md")),
        )
        self.assertEqual(
            ("articles/extend/providers.md", "Extend and customize"),
            inventory.proposed_location(PurePosixPath("articles/extensibility/providers.md")),
        )

    def test_current_url_handles_index_pages(self) -> None:
        self.assertEqual("/", inventory.current_url(PurePosixPath("index.md")))
        self.assertEqual(
            "/articles/overview/",
            inventory.current_url(PurePosixPath("articles/overview/index.md")),
        )
        self.assertEqual(
            "/articles/overview/what-is-helium.html",
            inventory.current_url(PurePosixPath("articles/overview/what-is-helium.md")),
        )

    def test_toc_scan_finds_missing_markdown_targets(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            section = root / "articles" / "sample"
            section.mkdir(parents=True)
            (section / "existing.md").write_text("# Existing\n", encoding="utf-8")
            (section / "toc.yml").write_text(
                """items:
- name: Existing
  href: existing.md
- name: Missing
  href: missing.md
""",
                encoding="utf-8",
            )
            result = inventory.scan_tocs(root)
            self.assertIn("articles/sample/existing.md", result.references)
            self.assertEqual(1, len(result.missing_targets))
            self.assertEqual("missing-file", result.missing_targets[0]["reason"])


if __name__ == "__main__":
    unittest.main()
