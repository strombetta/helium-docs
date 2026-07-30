---
title: Contribute to Helium
description: Choose how to contribute to the Helium framework or its documentation and follow the applicable development and review workflow.
content_type: index
area: contributing
version: all
status: stable
last_reviewed: 2026-07-30
---

# Contribute to Helium

Helium accepts contributions to both the framework and its documentation. The two areas use related docs-as-code and review practices, but they have different source repositories, validation requirements, and ownership boundaries.

## Choose a contribution path

### Contribute to the documentation

Use the documentation contribution path when you want to:

- correct or add consumer-facing guidance;
- improve navigation or learning paths;
- add or update code samples;
- maintain manual or generated reference content;
- change DocFX, the site theme, validation, preview, or publication behavior.

Start with:

- [Documentation architecture](documentation-architecture.md) to understand where content belongs;
- [Authoring conventions](authoring-conventions.md) to write and structure pages;
- [TOC conventions](toc-conventions.md) to change navigation;
- [Metadata reference](metadata-reference.md) to apply front matter;
- [Issue and pull-request workflow](issues-and-pull-requests.md) to prepare a contribution.

Then use:

- [Build the documentation locally](build-locally.md);
- [Validate links and cross-references](link-validation.md);
- [Preview environments](preview-environments.md);
- [Publication process](publication-process.md).

### Contribute to the framework

Use the framework contribution path when you want to change runtime behavior, public contracts, packages, migrations, tests, build policy, or release artifacts.

Start with:

- [Build Helium from source](build-from-source.md);
- [Run repository validation](repository-validation.md);
- [Coding and namespace conventions](coding-and-namespace-conventions.md);
- [Architecture Decision Records](architecture-decisions.md);
- [Public API compatibility policy](public-api-compatibility.md);
- [Testing policy](testing-policy.md);
- [Packaging and versioning](packaging-and-versioning.md);
- [Release process](release-process.md).

A framework change that affects consumers normally requires a linked documentation issue or pull request. See [Issue and pull-request workflow](issues-and-pull-requests.md).

## Repository responsibilities

| Repository | Primary responsibility |
| --- | --- |
| `strombetta/helium` | Framework behavior, public contracts, packages, migrations, tests, and release artifacts. |
| `strombetta/helium-docs` | Consumer documentation, navigation, learning paths, reference presentation, validation, and publication. |

Keep cross-repository changes linked in both directions. A stable framework feature is not release-ready until its required consumer documentation is complete.

## Contribution expectations

Every contribution should:

- solve a specific developer, operator, or contributor problem;
- remain within the approved product and documentation architecture;
- include appropriate technical and editorial review;
- pass repository validation;
- preserve compatibility and published URLs where applicable;
- avoid exposing secrets, customer information, or embargoed security details.

## Report a problem

Use a GitHub issue when you identify incorrect or missing documentation, a broken example, a navigation problem, or a release and compatibility gap. Include the affected page, applicable version, expected information, and sanitized evidence.

See [Issue and pull-request workflow](issues-and-pull-requests.md) for the required details and review process.
