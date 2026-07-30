---
title: Issue and pull-request workflow
description: Report documentation problems, prepare documentation pull requests, and complete the required technical and editorial reviews.
content_type: how-to
area: contributing
version: all
status: stable
last_reviewed: 2026-07-30
---

# Issue and pull-request workflow

Use GitHub issues and pull requests to propose, review, and publish changes to the Helium documentation. Documentation changes follow the same docs-as-code principles as framework changes: they are versioned, reviewed, validated, previewed, and linked to the technical work that makes them necessary.

## Report a documentation issue

Choose the issue category that best describes the reader problem:

- documentation is incorrect;
- documentation is missing;
- a code sample does not work;
- navigation or search makes content difficult to find;
- release, compatibility, or upgrade information is incomplete.

Include, when applicable:

- the affected page URL;
- the selected Helium documentation version;
- the expected behavior or information;
- the problem observed;
- the framework package, API, configuration, or error involved;
- a sanitized reproduction or log excerpt.

Do not include credentials, tokens, customer data, private connection strings, or other sensitive information.

## Prepare a documentation pull request

A documentation pull request should explain the user problem it solves rather than only listing changed files.

Include these sections in the description:

```markdown
## Purpose

Describe the reader problem and the intended outcome.

## Content type

- [ ] Index
- [ ] Overview
- [ ] Concept
- [ ] Tutorial
- [ ] How-to
- [ ] Reference
- [ ] Troubleshooting
- [ ] Release

## Framework relationship

Framework issue or PR:
Helium version:

## Validation

- [ ] DocFX build succeeds
- [ ] Links are valid
- [ ] Code examples were verified
- [ ] Terminology follows the glossary
- [ ] Navigation and related links were reviewed
- [ ] The rendered preview was inspected

## Release impact

- [ ] No release coordination required
- [ ] Stable release
- [ ] Preview release
- [ ] Breaking change
- [ ] Deprecation
```

Keep each pull request focused on one coherent documentation increment. Separate unrelated site engineering, content migration, and framework guidance when doing so improves review and rollback safety.

## Connect framework and documentation changes

Changes in `strombetta/helium` and `strombetta/helium-docs` use separate pull requests because the repositories have independent histories and pipelines. Link the pull requests in both directions.

In the framework pull request:

```text
Documentation: strombetta/helium-docs#<number>
```

In the documentation pull request:

```text
Framework change: strombetta/helium#<number>
Applies to: Helium <version>
```

A framework change that affects public behavior, configuration, operation, compatibility, or extension must not be released as stable until the required documentation is ready.

## Assess documentation impact

Every framework pull request should classify documentation impact.

```markdown
## Documentation impact

- [ ] No documentation impact
- [ ] Existing documentation remains correct
- [ ] Documentation update required before release
- [ ] Breaking-change or upgrade guidance required
- [ ] API reference regeneration required
- [ ] Preview documentation required

Documentation PR or issue:
```

When selecting `No documentation impact`, provide a specific rationale, such as:

> Internal refactoring; no public contracts, defaults, diagnostics, configuration, supported behavior, or operational requirements changed.

The following changes normally require documentation review:

- a new or changed public API;
- a configuration key, default, or validation rule;
- a new capability or supported workflow;
- a behavior visible to a consuming application;
- a new error, policy, event, endpoint, or diagnostic;
- a migration or deployment requirement;
- a security requirement;
- a new extension or replacement boundary;
- a deprecation or breaking change;
- a compatibility or support-policy change;
- a change to the Getting started path.

Internal refactoring, test-only changes, and implementation-only renames may not require consumer-facing updates, but their impact must still be assessed.

## Review types

### Technical review

Technical review verifies:

- behavior and terminology against the framework;
- public API names and signatures;
- configuration keys, defaults, and validation;
- prerequisites and supported versions;
- security and operational implications;
- compatibility and migration impact;
- code-sample correctness.

A subject-matter owner for the affected capability performs this review.

### Editorial review

Editorial review verifies:

- correct content type and page intent;
- information structure and clarity;
- terminology and style;
- canonical ownership of facts;
- navigation and learning-path integration;
- useful next steps;
- avoidance of duplicated or contradictory guidance.

A documentation owner or technical writer performs this review.

### Documentation-engineering review

This review is required for changes to:

- DocFX configuration;
- site templates, CSS, or JavaScript;
- metadata schemas;
- validation scripts and workflows;
- API generation;
- search, versioning, redirects, or shared components.

### Specialist review

Some changes require an additional specialist:

| Change | Additional review |
| --- | --- |
| Security guidance | Security owner |
| Migration or schema guidance | Persistence and release owner |
| Breaking change or deprecation | Compatibility and release owner |
| Deployment guidance | Operations owner |
| Public API documentation | API compatibility owner |

One person may perform several review roles in a small team, but each review perspective must still be addressed.

## Minimum approvals

| Change | Technical | Editorial | Documentation engineering |
| --- | ---: | ---: | ---: |
| Grammar or spelling correction | Optional | Required | No |
| New concept page | Required | Required | No |
| How-to guide with code | Required | Required | When automation changes |
| Generated API reference | Required | Optional | Required |
| TOC change | Area owner | Required | When rendering changes |
| DocFX or theme change | Optional | Required | Required |
| Security guidance | Specialist required | Required | No |
| Breaking change | Required | Required | Release owner |
| Redirect or removal | Area owner | Required | Required |

## Definition of Done

A documentation change is complete when:

- the reader problem and intended outcome are clear;
- the page uses the approved content type and metadata;
- public behavior is verified against the applicable framework source and release;
- code samples and commands were tested where relevant;
- terminology follows the documentation standards;
- links and cross-references resolve;
- navigation, related content, and learning paths were reviewed;
- technical and editorial approvals are complete;
- the preview was inspected when rendering or navigation changed;
- release, deprecation, compatibility, or security coordination is complete;
- no published URL was removed without a redirect or documented retirement path.

## Review the preview

For changes that affect layout or navigation, inspect the pull-request preview and verify:

- TOC placement and active-page highlighting;
- headings and `In this article` navigation;
- code blocks, tables, and callouts;
- internal and external links;
- diagrams and alternative text;
- desktop and narrow-screen rendering;
- previous and next navigation in sequential content.

Minor spelling-only changes do not require an extensive visual review when the build and diff are sufficient.

## Merge and follow-up

Merge only after required checks and reviews complete. If a documentation pull request depends on an unreleased framework change, keep the relationship explicit and coordinate publication with the target release.

After merge:

- verify the production deployment when the change is release-critical;
- update linked issues and framework pull requests;
- propagate stable fixes to the preview documentation line when separate lines exist;
- create follow-up issues for deliberately deferred work.

## Related documentation

- [Documentation architecture](documentation-architecture.md)
- [Authoring conventions](authoring-conventions.md)
- [Publication process](publication-process.md)
- [Preview environments](preview-environments.md)
