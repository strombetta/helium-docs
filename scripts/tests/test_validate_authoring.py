from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_authoring import (
    DEFAULT_CONTENT_TYPES,
    DEFAULT_SCHEMA,
    DEFAULT_VOCABULARY,
    validate_files,
)


VALID_DOCUMENT = """---
title: Organization context
description: Understand how Helium validates the active organization for an authenticated account.
content_type: concept
area: organizations
version: 1.x
status: stable
last_reviewed: 2026-07-30
---

# Organization context

An organization context scopes organization-owned operations.

## Model

The context contains a validated organization identifier.
"""


class AuthoringValidatorTests(unittest.TestCase):
    def validate(self, content: str, managed_lines: str = "docs/page.md\n"):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            document = root / "docs" / "page.md"
            document.parent.mkdir(parents=True)
            document.write_text(content, encoding="utf-8")
            managed_file_list = root / "managed-files.txt"
            managed_file_list.write_text(managed_lines, encoding="utf-8")
            return validate_files(
                root=root,
                managed_file_list=managed_file_list,
                schema_path=DEFAULT_SCHEMA,
                vocabulary_path=DEFAULT_VOCABULARY,
                content_types_path=DEFAULT_CONTENT_TYPES,
            )

    def error_messages(self, content: str) -> list[str]:
        return [issue.message for issue in self.validate(content) if issue.severity == "error"]

    def test_valid_document_has_no_errors(self):
        issues = self.validate(VALID_DOCUMENT)
        self.assertEqual([], [issue for issue in issues if issue.severity == "error"])

    def test_missing_required_field_is_reported(self):
        content = VALID_DOCUMENT.replace("area: organizations\n", "")
        self.assertTrue(any("Missing required front-matter field 'area'" in message for message in self.error_messages(content)))

    def test_unsupported_vocabulary_value_is_reported(self):
        content = VALID_DOCUMENT.replace("status: stable", "status: experimental")
        self.assertTrue(any("unsupported value 'experimental'" in message for message in self.error_messages(content)))

    def test_title_must_match_h1(self):
        content = VALID_DOCUMENT.replace("# Organization context", "# Active organization")
        self.assertTrue(any("must match H1" in message for message in self.error_messages(content)))

    def test_heading_level_jump_is_reported(self):
        content = VALID_DOCUMENT.replace("## Model", "### Model")
        self.assertTrue(any("skips from H1 to H3" in message for message in self.error_messages(content)))

    def test_duplicate_managed_path_is_reported(self):
        issues = self.validate(VALID_DOCUMENT, "docs/page.md\ndocs/page.md\n")
        self.assertTrue(any("Duplicate managed path" in issue.message for issue in issues))


if __name__ == "__main__":
    unittest.main()
