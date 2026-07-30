---
title: Metadata reference
description: Reference for the front-matter fields and controlled vocabularies used by Helium documentation.
content_type: reference
area: contributing
version: all
status: stable
last_reviewed: 2026-07-30
---

# Metadata reference

Manual pages in `strombetta/helium-docs` use YAML front matter to identify their purpose, ownership domain, applicable version, support state, and review status. This page defines the human-readable metadata contract. Automated schema validation is implemented separately.

Use only documented fields and controlled values. Add a new value only when a concrete navigation, search, validation, ownership, or release requirement needs it.

## Minimum front matter

Every published manual page uses these fields:

```yaml
---
title: Protect ASP.NET Core endpoints
description: Protect application endpoints by applying Helium authorization policies.
content_type: how-to
area: authorization
version: 1.x
status: stable
last_reviewed: 2026-07-30
---
```

## Required fields

### `title`

The page title used by navigation, search, and HTML metadata.

Requirements:

- normally matches the page `H1` exactly;
- uses sentence case;
- describes the subject or task clearly;
- starts with a verb for how-to pages;
- avoids repeating `Helium` when the site context is sufficient.

### `description`

A short description used in search results, cards, and HTML metadata.

Requirements:

- explains what the reader can do or understand;
- remains meaningful outside the local TOC context;
- does not repeat the title without adding information;
- uses one concise sentence in most cases;
- avoids promotional or unsupported claims.

### `content_type`

Identifies the page's dominant editorial purpose.

Allowed values:

| Value | Purpose |
| --- | --- |
| `index` | Orient readers within a section or capability. |
| `overview` | Explain what an area provides and when it applies. |
| `concept` | Explain a model, relationship, lifecycle, invariant, or behavior. |
| `tutorial` | Teach through a complete and ordered scenario. |
| `how-to` | Show how to complete one specific task. |
| `reference` | Provide exact and systematically structured information. |
| `troubleshooting` | Diagnose a symptom and resolve it using evidence. |
| `release` | Explain release changes, compatibility, deprecations, or upgrades. |

A page has one `content_type`. Supporting sections do not create additional types.

### `area`

Identifies the primary functional or documentation domain that owns the page.

Initial allowed values:

| Group | Values |
| --- | --- |
| Product and onboarding | `product`, `getting-started`, `architecture` |
| Application capabilities | `configuration`, `identity`, `onboarding`, `organizations`, `authorization`, `billing`, `entitlements`, `communications` |
| Extension and operation | `extensibility`, `persistence`, `durable-processing`, `hosting`, `deployment`, `diagnostics`, `security`, `testing`, `performance` |
| Documentation systems | `troubleshooting`, `compatibility`, `api`, `contributing` |

Select one primary area even when a page links to several domains. Cross-domain relationships belong in the page content and related links.

### `version`

Identifies the documentation line to which the page applies.

Initial allowed values:

| Value | Meaning |
| --- | --- |
| `all` | Version-independent documentation, primarily contribution guidance or stable general concepts. |
| `1.x` | Applies to the Helium 1.x documentation line. |
| `preview` | Applies only to unreleased or preview behavior. |

Do not use patch versions for ordinary pages. Add a new version value only when that documentation line exists.

### `status`

Identifies the support state of the documented feature or behavior.

| Value | Meaning |
| --- | --- |
| `stable` | Supported for ordinary use in the applicable release line. |
| `preview` | Available for evaluation and subject to change. |
| `deprecated` | Still available but scheduled for replacement or removal. |
| `legacy` | Maintained primarily for compatibility with an older supported path. |
| `unsupported` | Documented for clarity but outside the supported product scope. |

`status` does not represent whether the document is a draft or has completed editorial review.

### `last_reviewed`

The date on which a responsible reviewer last verified the page against the applicable framework behavior and documentation standards.

Format:

```yaml
last_reviewed: YYYY-MM-DD
```

Do not update this field for spelling changes, formatting-only changes, or automated migrations that do not include substantive technical review.

## Conditional fields

### `uid`

A stable logical identifier that can survive file moves.

```yaml
uid: authorization-protect-endpoints
```

Use lowercase words separated by hyphens. Do not include the content type, version, or complete file path. UIDs must be unique.

UIDs are initially recommended for:

- fundamental concepts;
- manual reference pages;
- pages used by learning paths;
- highly linked task pages.

### `level`

Use primarily for tutorials, learning paths, and selected how-to guides.

Allowed values:

| Value | Meaning |
| --- | --- |
| `beginner` | Requires no previous Helium experience and follows the primary supported path. |
| `intermediate` | Assumes completion of Getting started and combines several Helium concepts. |
| `advanced` | Requires detailed knowledge of extension, architecture, operation, or compatibility boundaries. |

Level does not determine TOC placement.

### `audience`

Identifies an audience when that distinction changes prerequisites, terminology, or task framing.

Initial allowed values:

- `developer`;
- `technical-lead`;
- `operator`;
- `contributor`.

Example:

```yaml
audience:
  - developer
  - operator
```

Do not add audience metadata merely because several roles might read the page.

### `keywords`

Adds search terms and established synonyms that do not appear naturally in the title or description.

```yaml
keywords:
  - tenant context
  - current organization
```

Do not repeat common terms already used throughout the page or add broad SEO keywords.

### `owner`

Identifies a stable team, functional area, or repository alias responsible for review.

```yaml
owner: authorization
```

Prefer stable ownership identifiers over individual names.

### `source`

Identifies framework artifacts closely associated with the page.

```yaml
source:
  - Trombetta.SaaS
  - Trombetta.SaaS.Hosting.AspNetCore
```

Use this field when it supports ownership, drift detection, or automated review routing. It is not required for general overview content.

### `document_status`

Represents editorial workflow and is separate from product support state.

Allowed values when used:

- `draft`;
- `review`;
- `published`;
- `archived`.

A preview feature can have a published document. A stable feature can have a document that is still in review.

## Release and compatibility fields

Use these fields only for release, deprecation, compatibility, and upgrade content.

### `introduced_in`

The first release that contains the behavior.

```yaml
introduced_in: 1.2
```

### `deprecated_in`

The release in which the contract or behavior became deprecated.

```yaml
deprecated_in: 1.4
```

### `replacement`

The supported replacement for deprecated behavior.

```yaml
replacement: ConsumerAuthorizationPolicyBuilder
```

### `removal_planned`

The release in which removal is expected, when a commitment exists.

```yaml
removal_planned: 2.0
```

### `change_type`

Identifies release impact.

Initial values:

- `feature`;
- `fix`;
- `breaking`;
- `deprecation`;
- `security`.

### `upgrade_from` and `upgrade_to`

Identify the source and target lines for an upgrade guide.

```yaml
upgrade_from: 1.x
upgrade_to: 2.0
```

### `migration_required`

Indicates whether consumer action is required.

```yaml
migration_required: true
```

## Fields not duplicated in front matter

Do not manually add information that is already derived reliably from another source.

### TOC position

The table of contents owns section order and hierarchy. Do not add `section`, `subsection`, or `order` fields to ordinary pages.

### URL

The build and file layout determine the URL. Do not add a manual `url` field unless a future publishing requirement explicitly uses it.

### Product name

DocFX global metadata identifies the product as Helium. Do not repeat `product: helium` on every page while the site documents one product.

## Example: concept page

```yaml
---
title: Active organization context
description: Understand how Helium selects and validates the active organization for an authenticated account.
uid: organizations-active-context
content_type: concept
area: organizations
version: 1.x
status: stable
last_reviewed: 2026-07-30
keywords:
  - tenant context
  - current organization
---
```

## Example: how-to page

```yaml
---
title: Protect ASP.NET Core endpoints
description: Protect application endpoints by applying Helium authorization policies.
uid: authorization-protect-endpoints
content_type: how-to
area: authorization
version: 1.x
status: stable
level: intermediate
audience:
  - developer
last_reviewed: 2026-07-30
---
```

## Example: troubleshooting page

```yaml
---
title: Stripe webhooks are rejected
description: Diagnose Stripe webhook signature and endpoint configuration failures.
uid: troubleshooting-stripe-webhook-rejection
content_type: troubleshooting
area: billing
version: 1.x
status: stable
audience:
  - developer
  - operator
last_reviewed: 2026-07-30
keywords:
  - invalid signature
  - webhook secret
---
```

## Validation expectations

Automated validation should eventually check:

- required fields are present;
- values use controlled vocabularies;
- dates use valid ISO format;
- UIDs are unique;
- `title` matches the page `H1`;
- deprecated content identifies a replacement or explains why none exists;
- version metadata is compatible with the publication line;
- `last_reviewed` is reported when it exceeds the review threshold.

During migration, legacy exceptions may be allowlisted. New or substantively rewritten pages must comply with the current metadata contract.

## Related documentation

- [Documentation architecture](documentation-architecture.md)
- [Authoring conventions](authoring-conventions.md)
- [TOC conventions](toc-conventions.md)
