# Authoring infrastructure

This directory contains the machine-readable authoring policy for Helium documentation.

The human-readable rules are documented in [`articles/contributing`](../articles/contributing/index.md). Files in this directory support validation and page creation; they do not replace the contributor documentation.

## Contents

- `front-matter.schema.json` defines supported metadata fields and their basic types.
- `vocabulary.yml` defines controlled values used by front matter.
- `content-types.yml` defines the purpose and expected sections of each editorial content type.
- `ownership.yml` maps documentation areas to logical owners. GitHub handles are added separately through `CODEOWNERS`.
- `managed-files.txt` lists pages currently subject to blocking authoring validation during the staged migration.
- `templates/` contains starting points for each editorial content type.

The `.yml` policy files use JSON-compatible YAML. JSON is a valid YAML 1.2 representation and allows validation with the Python standard library, without adding a package dependency to the documentation build.

## Staged enforcement

Authoring validation initially applies only to files in `managed-files.txt`. Add a page to that list after its metadata and heading structure have been reviewed.

The managed set must only grow. When all published Markdown has been migrated, validation will scan the complete documentation corpus and `managed-files.txt` will be removed.

## Validate locally

Run:

```bash
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
python3 scripts/validate_authoring.py
```

The validator returns a nonzero exit code for blocking errors and prints each error with its source path.