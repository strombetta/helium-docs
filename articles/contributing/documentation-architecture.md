---
title: Documentation architecture
description: Learn how the Helium documentation is organized, governed, and connected to the framework source of truth.
content_type: concept
area: contributing
version: all
status: stable
last_reviewed: 2026-07-30
---

# Documentation architecture

The Helium documentation is a product interface for evaluating, adopting, building, extending, deploying, and maintaining applications that use the framework. Its structure is based on user goals and application lifecycle stages rather than repository layout, package names, or internal implementation boundaries.

This document defines the normative information architecture for `strombetta/helium-docs`. Use it when adding sections, moving pages, designing learning paths, or deciding where new content belongs.

## Scope

The documentation architecture covers:

- the relationship between the Helium framework and its public documentation;
- the canonical top-level information model;
- navigation and page hierarchy;
- editorial content types;
- learning paths;
- source-of-truth and versioning rules;
- constraints for maintaining a coherent documentation system.

It does not define detailed writing conventions, front-matter fields, or YAML syntax. See [Authoring conventions](authoring-conventions.md), [Metadata reference](metadata-reference.md), and [TOC conventions](toc-conventions.md).

## Audiences

The primary audiences are:

- technical founders evaluating a SaaS foundation;
- .NET developers building consuming applications;
- engineering teams extending and testing Helium integrations;
- operators deploying, monitoring, upgrading, and recovering applications;
- contributors maintaining the framework or documentation.

Navigation is organized by user outcome rather than professional title. A single person may evaluate, build, and operate the same application.

## Source repositories

Helium uses two repositories with distinct responsibilities.

### `strombetta/helium`

The framework repository is the source of truth for:

- released runtime behavior;
- supported public APIs and extension points;
- package and namespace boundaries;
- configuration defaults and validation;
- error codes, policy identifiers, and lifecycle events;
- migrations and hosting requirements;
- compatibility baselines and contract tests.

### `strombetta/helium-docs`

The documentation repository is the source of truth for:

- consumer-facing guidance;
- information architecture and navigation;
- tutorials, how-to guides, concepts, and troubleshooting;
- manual reference content;
- learning paths;
- editorial terminology and authoring standards;
- site build, preview, and publication behavior.

## Behavior states

Documentation must distinguish the following states:

| State | Meaning |
| --- | --- |
| Planned | Approved in a specification or architecture decision but not yet implemented. |
| Implemented | Present in source and tests but not necessarily released. |
| Released | Available in published packages or other supported artifacts. |
| Documented | Described in consumer-facing documentation for the applicable version. |

Stable documentation describes released behavior. Planned or implemented behavior may be documented only in clearly identified preview content.

## Canonical information model

The documentation uses the following top-level structure.

### Overview

Helps readers decide whether Helium is appropriate for their application. It covers product scope, supported application models, architecture, limitations, versions, and release status.

Primary question: **Is Helium appropriate for this application?**

### Get started

Provides a linear, verified path from prerequisites to a running application with an authenticated account and first organization.

Primary question: **How do I create a working Helium application?**

### Fundamentals

Explains the models and invariants required to understand the framework, including application composition, accounts, organizations, authorization, entitlements, lifecycle events, durable processing, and data ownership.

Primary question: **How does Helium work?**

### Build with Helium

Contains capability-oriented guidance for implementing application behavior. Initial capability areas include configuration, identity, onboarding, organizations, authorization, billing, entitlements, and transactional email.

Primary question: **How do I implement this SaaS capability?**

### Extend and customize

Explains supported configuration, extension, replacement, and consumer-module boundaries. It distinguishes public contracts from framework internals.

Primary question: **How do I adapt Helium without compromising upgrade compatibility?**

### Deploy and operate

Covers production configuration, persistence, migrations, deployment, security, diagnostics, durable processing, performance, upgrades, recovery, and troubleshooting.

Primary question: **How do I run and maintain a Helium application in production?**

### Reference

Provides precise, systematically structured information, including package, API, configuration, endpoint, error-code, policy, lifecycle-event, compatibility, and glossary references.

Primary question: **What is the exact supported definition?**

### Contribute

Documents contribution workflows for both the framework and the documentation system.

Primary question: **How do I make and validate a contribution?**

## Navigation model

The site uses multiple complementary navigation mechanisms.

### Homepage

The homepage is a task-oriented landing page. It presents primary entry points, search, learning paths, capability shortcuts, release status, and reference links. It must not redirect directly to an overview page or reproduce the complete table of contents.

### Global header

The global header contains:

- the Helium documentation brand;
- search;
- the selected documentation version;
- a link to the framework repository.

The header must not duplicate the complete documentation hierarchy.

### Table of contents

The left navigation represents the canonical hierarchy. It is the source of truth for section order and parent-child relationships. Only the branch containing the current page should normally be expanded.

### Breadcrumb

The breadcrumb shows the current page's location in the canonical hierarchy. It supports orientation but does not replace the table of contents.

### In-page navigation

Long pages expose an `In this article` list generated from meaningful `H2` and selected `H3` headings.

### Index pages

Every significant section or capability node links to an index page. An index page explains the section boundary, recommends a starting point, groups common tasks and concepts, and links to troubleshooting and reference content. It must not be an empty container or a duplicate of the TOC.

### Sequential navigation

Previous and next links are used only for genuinely sequential experiences, such as tutorials, learning paths, and version-specific upgrade procedures. Non-sequential pages use curated `Next steps` links instead.

## Content hierarchy

Each page has one dominant editorial intent and one canonical content type.

| Content type | Primary purpose |
| --- | --- |
| `index` | Orient readers within a section or capability. |
| `overview` | Explain what an area provides, why it exists, and when it applies. |
| `concept` | Explain a model, lifecycle, invariant, relationship, or behavior. |
| `tutorial` | Teach through a complete, ordered, verifiable scenario. |
| `how-to` | Show how to complete one specific task. |
| `reference` | Provide exact and systematically structured information. |
| `troubleshooting` | Diagnose a symptom and guide the reader to evidence-based resolution. |
| `release` | Explain release changes, deprecations, breaking changes, and upgrade impact. |

A page may contain supporting material from another type, but it must not combine several primary intents. For example, a configuration reference defines options and defaults; a separate how-to guide explains how to configure a specific deployment.

## Learning paths

A learning path is a curated sequence of canonical pages that leads to a verifiable capability. It is not another content hierarchy and does not own duplicated copies of pages.

The initial learning paths are:

- Evaluate Helium;
- Create your first Helium application;
- Build a multi-tenant SaaS application;
- Deploy and operate Helium.

Each learning path declares:

- audience and prerequisites;
- final outcome;
- ordered modules;
- intermediate verification points;
- completion criteria;
- relevant next paths.

## Canonical ownership of information

Each normative fact has one owning location.

| Information | Canonical location |
| --- | --- |
| Configuration default and valid values | Configuration reference |
| Public type or member signature | Generated API reference |
| Architectural model or invariant | Concept page |
| Steps for completing a task | How-to guide or tutorial |
| Symptom, evidence, and remediation | Troubleshooting page |
| Compatibility or support guarantee | Compatibility and support reference |
| Release-specific behavior change | Release or upgrade documentation |

Other pages link to the canonical source instead of restating the full information. Short contextual summaries are allowed when they help complete the current task.

## Structural constraints

The documentation follows these constraints:

- the normal visible TOC depth is three levels: section, area, page;
- section and area nodes link to substantive index pages;
- generic containers such as `General`, `Miscellaneous`, and `Advanced` are not used;
- package and namespace structure does not determine the primary navigation;
- generated API documentation and manual reference remain distinct;
- troubleshooting is organized by observable symptom;
- page moves preserve published URLs through redirects;
- stable UIDs remain unchanged when files move;
- empty placeholder pages are not published as finished navigation destinations;
- the documentation does not present implementation details as supported contracts.

## Changing the architecture

A structural change requires:

1. a documented user or maintenance problem;
2. an assessment of affected pages, URLs, learning paths, and search behavior;
3. a proposed target structure;
4. technical and editorial review;
5. an update to this architecture document and related conventions;
6. an explicit migration and redirect plan;
7. validation that no public page becomes unreachable.

Small page additions that follow the established model do not require a separate architecture decision.

## Related documentation

- [Authoring conventions](authoring-conventions.md)
- [TOC conventions](toc-conventions.md)
- [Metadata reference](metadata-reference.md)
- [Issue and pull-request workflow](issues-and-pull-requests.md)
- [Publication process](publication-process.md)
