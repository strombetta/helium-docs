---
title: TOC conventions
description: Follow the structural and naming rules for Helium documentation tables of contents.
content_type: reference
area: contributing
version: all
status: stable
last_reviewed: 2026-07-30
---

# TOC conventions

The table of contents defines the canonical documentation hierarchy, local navigation order, and parent-child relationships. Use these conventions when adding, moving, renaming, or grouping pages in a `toc.yml` file.

The TOC does not define every relationship between pages. Learning paths, contextual links, related content, and search metadata are maintained separately.

## Canonical top-level structure

The primary documentation hierarchy is:

1. Overview;
2. Get started;
3. Fundamentals;
4. Build with Helium;
5. Extend and customize;
6. Deploy and operate;
7. Reference;
8. Contribute.

Do not introduce another top-level taxonomy based on packages, namespaces, professional roles, or perceived difficulty.

## Normal depth

The normal visible depth is three levels:

```text
Section
└── Area
    └── Page
```

A fourth level requires a clear usability reason and documentation-architecture review. When an area contains many pages, prefer a substantive index page that groups links by task or concept instead of adding another TOC layer.

## Container nodes

Every significant section and area node must link to an index page.

Preferred:

```yaml
- name: Authorization
  href: authorization/index.md
  items:
  - name: Authorization model
    href: authorization/model.md
```

Avoid a non-clickable label whose only purpose is grouping.

An index page must explain the scope of its section, recommend a starting point, and link to common tasks, concepts, troubleshooting, and reference content. It must not be empty or repeat the TOC verbatim.

## Naming

Use sentence case and concise, descriptive names.

Preferred:

- `Organizations and tenancy`
- `Protect ASP.NET Core endpoints`
- `Operation error codes`

Avoid:

- title case;
- unexplained abbreviations;
- package or namespace names when the reader is looking for a capability;
- generic containers such as `General`, `Miscellaneous`, `Other`, or `Advanced`.

Use action-oriented names for procedures. Start how-to page names with a verb such as `Configure`, `Create`, `Protect`, `Apply`, `Deploy`, `Test`, or `Upgrade`.

## Ordering

Order pages according to reader progression, not automatically by filename or alphabetically.

Within an area, use this order when applicable:

1. index or overview;
2. foundational concepts;
3. common tasks;
4. specialized scenarios;
5. security and testing guidance;
6. troubleshooting links;
7. reference links.

A tutorial follows its required execution order.

## Expansion behavior

Only the branch containing the current page should normally be expanded. Do not set `expanded: true` on every top-level section.

Explicit expansion may be used for a short, linear tutorial when showing the complete sequence improves orientation. It must not expose the complete documentation tree by default.

## Relationship to physical files

Directory structure should reflect primary ownership and maintainability, but it does not independently determine navigation.

A page belongs in the TOC area that best matches its user intent. For example:

- a conceptual explanation of durable processing belongs in Fundamentals;
- worker leasing and recovery procedures belong in Deploy and operate;
- exact durable-work identifiers belong in Reference.

Avoid duplicating the same page under several TOC branches. Use contextual links and learning paths instead.

## Page moves

Before moving a published page:

1. record the current path and public URL;
2. select the new canonical path;
3. preserve the existing UID when one exists;
4. add a permanent redirect from the previous URL;
5. update internal links and TOC entries;
6. verify that the old and new URLs behave as intended;
7. verify that no page becomes orphaned.

Do not remove a published URL solely because the information architecture changed.

## Page renames

Rename a TOC label without renaming the file when the existing URL remains suitable. Rename the file only when the path is misleading or conflicts with the target architecture.

When a file is renamed, apply the page-move procedure and preserve redirects.

## Duplicate placement

A page may appear in more than one navigation context only when all of the following are true:

- the page has one canonical URL;
- duplicate placement materially improves discoverability;
- breadcrumb behavior remains unambiguous;
- the page does not appear to have two owners;
- documentation-architecture review approves the exception.

Prefer a link from an index page over duplicate TOC placement.

## Reference navigation

Manual reference and generated API reference are separate areas.

Manual reference includes:

- packages;
- configuration;
- endpoints;
- operation error codes;
- authorization policies;
- lifecycle events;
- transactional message types;
- compatibility;
- known limitations;
- glossary.

Generated API reference includes namespaces, types, members, signatures, and XML documentation. Do not place conceptual or task-oriented articles inside the generated API hierarchy.

## Contribute navigation

Contribution content must distinguish:

- contributing to the framework;
- contributing to the documentation.

The current physical directory may contain both groups during migration, but the index and target TOC should make the distinction explicit.

## Validation requirements

A TOC change must pass these checks:

- every `href` resolves;
- every significant node has an index page;
- no finished navigation destination is empty;
- no unintended duplicate entry exists;
- normal depth does not exceed three levels;
- page names follow sentence case and action naming rules;
- moved pages have redirects;
- public pages are reachable from the TOC, a learning path, or an approved reference index;
- no deprecated top-level taxonomy is reintroduced.

## Review checklist

Before requesting review, confirm that:

- the new location matches the page's primary user intent;
- the order supports reader progression;
- the index page describes the area boundary;
- sibling page names use parallel grammar;
- the change does not expose implementation structure as the primary navigation;
- the affected learning paths and contextual links were reviewed;
- URL and redirect impact was assessed.

## Related documentation

- [Documentation architecture](documentation-architecture.md)
- [Authoring conventions](authoring-conventions.md)
- [Metadata reference](metadata-reference.md)
