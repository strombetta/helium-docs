from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path, PurePosixPath


MODULE_PATH = Path(__file__).resolve().parents[1] / "generate_last_updated.py"
SPEC = importlib.util.spec_from_file_location("generate_last_updated", MODULE_PATH)
assert SPEC and SPEC.loader
last_updated = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = last_updated
SPEC.loader.exec_module(last_updated)


class LastUpdatedTests(unittest.TestCase):
    def test_output_urls_include_index_aliases(self) -> None:
        self.assertEqual(
            ("/", "/index.html"),
            last_updated.output_urls(PurePosixPath("index.md")),
        )
        self.assertEqual(
            ("/articles/overview/", "/articles/overview/index.html"),
            last_updated.output_urls(PurePosixPath("articles/overview/index.md")),
        )
        self.assertEqual(
            ("/articles/overview/what-is-helium.html",),
            last_updated.output_urls(
                PurePosixPath("articles/overview/what-is-helium.md")
            ),
        )

    def test_iter_public_pages_excludes_toc_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "index.md").write_text("# Home\n", encoding="utf-8")
            section = root / "articles" / "overview"
            section.mkdir(parents=True)
            (section / "index.md").write_text("# Overview\n", encoding="utf-8")
            (section / "toc.yml").write_text("items: []\n", encoding="utf-8")
            (section / "data.json").write_text("{}\n", encoding="utf-8")

            paths = [
                path.relative_to(root).as_posix()
                for path in last_updated.iter_public_pages(root)
            ]

            self.assertEqual(["articles/overview/index.md", "index.md"], paths)

    def test_git_last_updated_uses_last_file_commit(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            page = root / "index.md"
            page.write_text("# Home\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(root), "add", "index.md"], check=True)
            env = os.environ.copy()
            env.update(
                {
                    "GIT_AUTHOR_NAME": "Docs Test",
                    "GIT_AUTHOR_EMAIL": "docs@example.com",
                    "GIT_COMMITTER_NAME": "Docs Test",
                    "GIT_COMMITTER_EMAIL": "docs@example.com",
                    "GIT_AUTHOR_DATE": "2026-08-04T10:00:00+02:00",
                    "GIT_COMMITTER_DATE": "2026-08-04T10:00:00+02:00",
                }
            )
            subprocess.run(
                ["git", "-C", str(root), "commit", "-q", "-m", "Add page"],
                check=True,
                env=env,
            )

            self.assertEqual(
                "2026-08-04",
                last_updated.git_last_updated(root, Path("index.md")),
            )

    def test_write_manifest_serializes_page_dates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / "articles" / "guide.md"
            page.parent.mkdir(parents=True)
            page.write_text("# Guide\n", encoding="utf-8")

            manifest = last_updated.build_manifest(
                root,
                pages=[page],
                date_resolver=lambda _root, _path: "2026-08-04",
            )
            destination = root / "manifest.json"
            destination.write_text(json.dumps(manifest), encoding="utf-8")

            self.assertEqual(
                {"/articles/guide.html": "2026-08-04"},
                json.loads(destination.read_text(encoding="utf-8")),
            )


if __name__ == "__main__":
    unittest.main()
