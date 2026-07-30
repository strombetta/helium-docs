#!/usr/bin/env python3
"""Validate front matter and heading structure for managed documentation files."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = REPOSITORY_ROOT / ".authoring" / "front-matter.schema.json"
DEFAULT_VOCABULARY = REPOSITORY_ROOT / ".authoring" / "vocabulary.yml"
DEFAULT_CONTENT_TYPES = REPOSITORY_ROOT / ".authoring" / "content-types.yml"
DEFAULT_MANAGED_FILES = REPOSITORY_ROOT / ".authoring" / "managed-files.txt"

FIELD_PATTERN = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):(?:\s*(.*))?$")
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


@dataclass(frozen=True)
class Issue:
    path: Path
    message: str
    severity: str = "error"
    line: int | None = None

    def format(self, root: Path) -> str:
        try:
            display_path = self.path.relative_to(root)
        except ValueError:
            display_path = self.path
        location = f"{display_path}:{self.line}" if self.line else str(display_path)
        return f"{self.severity.upper()}: {location}: {self.message}"


def load_json_compatible_yaml(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Policy file does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Policy file is not valid JSON-compatible YAML: {path}: {exc}") from exc

    if not isinstance(value, dict):
        raise ValueError(f"Policy file must contain an object: {path}")
    return value


def parse_scalar(raw_value: str) -> Any:
    value = raw_value.strip()
    if value == "":
        return ""
    if value == "true":
        return True
    if value == "false":
        return False
    if value == "null":
        return None
    if value.startswith("[") or value.startswith('"'):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1].replace("''", "'")
    return value


def parse_front_matter(path: Path) -> tuple[dict[str, Any], str, list[Issue]]:
    issues: list[Issue] = []
    try:
        text = path.read_text(encoding="utf-8-sig")
    except FileNotFoundError:
        return {}, "", [Issue(path, "Managed file does not exist.")]

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text, [Issue(path, "File must begin with YAML front matter delimited by '---'.", line=1)]

    closing_index: int | None = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        return {}, text, [Issue(path, "Front matter is missing its closing '---' delimiter.", line=1)]

    metadata: dict[str, Any] = {}
    current_list_key: str | None = None

    for index, line in enumerate(lines[1:closing_index], start=2):
        stripped = line.strip()
        if stripped == "" or stripped.startswith("#"):
            continue

        if line.startswith(("  - ", "    - ")):
            if current_list_key is None:
                issues.append(Issue(path, "List item does not follow a metadata field.", line=index))
                continue
            value = parse_scalar(stripped[2:].strip())
            current_value = metadata[current_list_key]
            if not isinstance(current_value, list):
                issues.append(Issue(path, f"Field '{current_list_key}' is not a list.", line=index))
                continue
            current_value.append(value)
            continue

        if line.startswith((" ", "\t")):
            issues.append(Issue(path, "Nested front-matter objects are not supported; use scalar or list fields.", line=index))
            current_list_key = None
            continue

        match = FIELD_PATTERN.match(line)
        if match is None:
            issues.append(Issue(path, "Invalid front-matter field syntax.", line=index))
            current_list_key = None
            continue

        key, raw_value = match.groups()
        if key in metadata:
            issues.append(Issue(path, f"Duplicate front-matter field '{key}'.", line=index))
            current_list_key = None
            continue

        if raw_value is None or raw_value.strip() == "":
            metadata[key] = []
            current_list_key = key
        else:
            metadata[key] = parse_scalar(raw_value)
            current_list_key = None

    body = "\n".join(lines[closing_index + 1 :])
    return metadata, body, issues


def python_type_matches(value: Any, expected_type: str) -> bool:
    if expected_type == "string":
        return isinstance(value, str)
    if expected_type == "array":
        return isinstance(value, list)
    if expected_type == "boolean":
        return isinstance(value, bool)
    if expected_type == "object":
        return isinstance(value, dict)
    return True


def validate_schema(path: Path, metadata: dict[str, Any], schema: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    required = schema.get("required", [])
    properties = schema.get("properties", {})

    for field in required:
        if field not in metadata:
            issues.append(Issue(path, f"Missing required front-matter field '{field}'."))

    if schema.get("additionalProperties") is False:
        for field in metadata:
            if field not in properties:
                issues.append(Issue(path, f"Unsupported front-matter field '{field}'."))

    for field, value in metadata.items():
        definition = properties.get(field)
        if not isinstance(definition, dict):
            continue

        expected_type = definition.get("type")
        if isinstance(expected_type, str) and not python_type_matches(value, expected_type):
            issues.append(Issue(path, f"Field '{field}' must have type {expected_type}."))
            continue

        if isinstance(value, str):
            minimum = definition.get("minLength")
            maximum = definition.get("maxLength")
            pattern = definition.get("pattern")
            if isinstance(minimum, int) and len(value) < minimum:
                issues.append(Issue(path, f"Field '{field}' must contain at least {minimum} characters."))
            if isinstance(maximum, int) and len(value) > maximum:
                issues.append(Issue(path, f"Field '{field}' must contain at most {maximum} characters."))
            if isinstance(pattern, str) and re.fullmatch(pattern, value) is None:
                issues.append(Issue(path, f"Field '{field}' does not match required pattern {pattern}."))

        if isinstance(value, list) and definition.get("uniqueItems") is True:
            normalized = [json.dumps(item, sort_keys=True) for item in value]
            if len(normalized) != len(set(normalized)):
                issues.append(Issue(path, f"Field '{field}' must not contain duplicate values."))

        if isinstance(value, list):
            item_definition = definition.get("items")
            if isinstance(item_definition, dict):
                item_type = item_definition.get("type")
                for item in value:
                    if isinstance(item_type, str) and not python_type_matches(item, item_type):
                        issues.append(Issue(path, f"Every value in '{field}' must have type {item_type}."))
                        break

    reviewed = metadata.get("last_reviewed")
    if isinstance(reviewed, str):
        try:
            date.fromisoformat(reviewed)
        except ValueError:
            issues.append(Issue(path, "Field 'last_reviewed' must be a valid ISO date in YYYY-MM-DD format."))

    return issues


def validate_vocabulary(path: Path, metadata: dict[str, Any], vocabulary: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    for field, allowed_values in vocabulary.items():
        if field not in metadata or not isinstance(allowed_values, list):
            continue
        value = metadata[field]
        values = value if isinstance(value, list) else [value]
        for item in values:
            if item not in allowed_values:
                allowed = ", ".join(str(candidate) for candidate in allowed_values)
                issues.append(Issue(path, f"Field '{field}' contains unsupported value '{item}'. Allowed values: {allowed}."))
    return issues


def extract_headings(body: str) -> list[tuple[int, str, int]]:
    headings: list[tuple[int, str, int]] = []
    fence: str | None = None

    for line_number, line in enumerate(body.splitlines(), start=1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence is not None:
            continue

        match = HEADING_PATTERN.match(line)
        if match:
            markers, title = match.groups()
            headings.append((len(markers), title.strip().rstrip("#").strip(), line_number))

    return headings


def validate_headings(path: Path, body: str, metadata: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    headings = extract_headings(body)
    h1_headings = [heading for heading in headings if heading[0] == 1]

    if len(h1_headings) != 1:
        issues.append(Issue(path, f"File must contain exactly one H1 heading; found {len(h1_headings)}."))
    elif metadata.get("title") != h1_headings[0][1]:
        issues.append(Issue(path, f"Front-matter title '{metadata.get('title')}' must match H1 '{h1_headings[0][1]}'."))

    previous_level: int | None = None
    for level, title, line_number in headings:
        if previous_level is not None and level > previous_level + 1:
            issues.append(Issue(path, f"Heading '{title}' skips from H{previous_level} to H{level}.", line=line_number))
        previous_level = level

    return issues


def validate_content_type_sections(
    path: Path,
    body: str,
    metadata: dict[str, Any],
    content_types: dict[str, Any],
) -> list[Issue]:
    issues: list[Issue] = []
    content_type = metadata.get("content_type")
    definition = content_types.get(content_type)
    if not isinstance(definition, dict):
        return issues

    headings = {title for level, title, _ in extract_headings(body) if level == 2}
    for section in definition.get("required_sections", []):
        if section not in headings:
            issues.append(
                Issue(
                    path,
                    f"Content type '{content_type}' normally requires an H2 section named '{section}'.",
                    severity="warning",
                )
            )
    return issues


def read_managed_files(path: Path, root: Path) -> tuple[list[Path], list[Issue]]:
    issues: list[Issue] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return [], [Issue(path, "Managed-file list does not exist.")]

    files: list[Path] = []
    seen: set[str] = set()
    for line_number, line in enumerate(lines, start=1):
        value = line.strip()
        if value == "" or value.startswith("#"):
            continue
        if value in seen:
            issues.append(Issue(path, f"Duplicate managed path '{value}'.", line=line_number))
            continue
        seen.add(value)
        files.append(root / value)
    return files, issues


def validate_files(
    root: Path,
    managed_file_list: Path,
    schema_path: Path,
    vocabulary_path: Path,
    content_types_path: Path,
) -> list[Issue]:
    try:
        schema = load_json_compatible_yaml(schema_path)
        vocabulary = load_json_compatible_yaml(vocabulary_path)
        content_types = load_json_compatible_yaml(content_types_path)
    except ValueError as exc:
        return [Issue(root, str(exc))]

    files, issues = read_managed_files(managed_file_list, root)
    for path in files:
        metadata, body, parse_issues = parse_front_matter(path)
        issues.extend(parse_issues)
        if any(issue.severity == "error" for issue in parse_issues):
            continue
        issues.extend(validate_schema(path, metadata, schema))
        issues.extend(validate_vocabulary(path, metadata, vocabulary))
        issues.extend(validate_headings(path, body, metadata))
        issues.extend(validate_content_type_sections(path, body, metadata, content_types))
    return issues


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPOSITORY_ROOT)
    parser.add_argument("--managed-file-list", type=Path, default=DEFAULT_MANAGED_FILES)
    parser.add_argument("--schema", type=Path, default=DEFAULT_SCHEMA)
    parser.add_argument("--vocabulary", type=Path, default=DEFAULT_VOCABULARY)
    parser.add_argument("--content-types", type=Path, default=DEFAULT_CONTENT_TYPES)
    parser.add_argument("--warnings-as-errors", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    arguments = build_parser().parse_args(argv)
    root = arguments.root.resolve()
    issues = validate_files(
        root=root,
        managed_file_list=arguments.managed_file_list.resolve(),
        schema_path=arguments.schema.resolve(),
        vocabulary_path=arguments.vocabulary.resolve(),
        content_types_path=arguments.content_types.resolve(),
    )

    for issue in sorted(issues, key=lambda item: (str(item.path), item.line or 0, item.severity, item.message)):
        print(issue.format(root))

    errors = [issue for issue in issues if issue.severity == "error"]
    warnings = [issue for issue in issues if issue.severity == "warning"]
    if errors or (arguments.warnings_as_errors and warnings):
        print(f"Authoring validation failed with {len(errors)} error(s) and {len(warnings)} warning(s).")
        return 1

    managed_files, _ = read_managed_files(arguments.managed_file_list.resolve(), root)
    print(f"Authoring validation succeeded for {len(managed_files)} managed file(s) with {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
