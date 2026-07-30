---
title: Publication process
description: Build, preview, review, and publish Helium documentation in coordination with framework releases.
content_type: how-to
area: contributing
version: all
status: stable
last_reviewed: 2026-07-30
---

# Publication process

Helium documentation is built and published through GitHub Actions and Azure Static Web Apps. Every pull request is validated before merge, and documentation that affects a framework release is coordinated with the corresponding packages, migrations, compatibility information, and upgrade guidance.

## Current publication flow

The current workflow is:

```text
Pull request
→ restore tools and documentation assets
→ build DocFX with warnings treated as errors
→ validate Markdown links
→ deploy a pull-request preview when deployment credentials are available

Merge to main
→ build the documentation
→ deploy the production site
```

The validation and deployment workflows use the .NET SDK selected by `global.json`, restore local tools, restore the documentation fonts, and run DocFX against `docfx.json`.

## Validate a pull request

Before publication, the pull request must pass:

- DocFX build;
- DocFX warning validation;
- internal Markdown link validation;
- any metadata, navigation, terminology, or code-sample checks introduced by the repository;
- required technical and editorial review.

Run the same canonical validation locally when possible. Do not redefine a different local success criterion from the CI workflow.

## Review the preview

When an Azure Static Web Apps preview is available, inspect the rendered result rather than relying only on the Markdown diff.

Review, as applicable:

- global and local navigation;
- page title, breadcrumb, and active TOC item;
- heading hierarchy and `In this article` navigation;
- code blocks, commands, output, and line wrapping;
- tables and callouts;
- diagrams, images, and alternative text;
- internal and external links;
- previous and next links in tutorials or learning paths;
- narrow-screen behavior;
- `Edit this page` and issue-reporting links when implemented.

A minor spelling-only change may rely on the diff and automated checks when it cannot affect rendering.

## Merge to the publication branch

The default publication branch is `main`. Merge only after:

- required checks pass;
- required reviewers approve;
- related framework and documentation work is linked;
- any release dependency is understood;
- URL and redirect impact is resolved.

Merging to `main` triggers the production build and deployment.

## Verify production publication

For release-critical or navigation changes, verify the production site after deployment.

Confirm:

- the expected version and status are visible;
- changed pages and redirects resolve;
- search and navigation expose the content correctly;
- code samples and downloads point to released artifacts;
- no preview-only guidance appears as stable content.

If the deployment credential is unavailable, the workflow reports a warning and skips deployment. A successful build alone does not prove that production publication occurred.

## Documentation states before the first stable release

Before Helium has a stable release, `main` may publish the documentation for the active preview. Pages that describe unreleased behavior must show `status: preview` and must not imply stable support.

The site should present the preview state consistently in page metadata, status banners, release information, and compatibility guidance.

## Stable and preview lines

After the first stable release, the target model is:

```text
main
→ current stable documentation

next
→ next release or preview documentation
```

The exact branch and deployment implementation is introduced only when multiple documentation lines exist. Until then, do not create version branches without an active publication requirement.

Stable fixes should be applied to the stable line and propagated to the preview line when the same content remains applicable.

## Coordinate with a framework release

Documentation is part of the release definition, not a post-release optional task.

Before a stable release, confirm that:

- generated API reference matches the release candidate;
- package and configuration references are current;
- release notes are complete;
- significant changes appear in What's new;
- breaking changes and deprecations are documented;
- upgrade guidance identifies required consumer actions;
- the compatibility matrix is current;
- known limitations are current;
- Getting started succeeds from a clean environment;
- migration and deployment guidance matches the release candidate;
- the version selector and status labels are prepared;
- the documentation preview has been approved.

Recommended release order:

```text
Release candidate available
→ documentation validated against the release candidate
→ stable documentation prepared
→ packages and artifacts published
→ stable documentation promoted
→ release announcement published
```

Do not publish stable instructions that require artifacts that are not yet available. Preview documentation may describe preview artifacts when clearly labeled.

## Publish breaking changes

A breaking change requires:

- the previous behavior;
- the new behavior;
- affected applications and versions;
- required code, configuration, or schema changes;
- a verification procedure;
- rollback or recovery considerations when applicable;
- links to the relevant API and upgrade guide.

The release must not be considered documentation-ready when the breaking-change impact is known but the migration path is not documented.

## Publish deprecations

A deprecation identifies:

- what is deprecated;
- the version in which deprecation begins;
- the reason;
- the supported replacement;
- migration instructions;
- the planned removal version when committed.

Do not delete the original page immediately. Add a deprecation notice and direct readers to the replacement. Preserve old URLs through the supported lifecycle.

## Security publication

Security fixes follow an embargoed process.

Before disclosure:

- keep issues and pull requests private;
- prepare advisory, affected-version, mitigation, and upgrade content without publishing it;
- avoid documentation changes that reveal the vulnerability early;
- coordinate package, advisory, and documentation release.

At disclosure, publish the security fix, advisory, affected versions, required action, and safe verification guidance together. Do not include exploit detail that is unnecessary for mitigation.

## Emergency corrections

Use an expedited correction when published documentation could cause:

- a security weakness;
- data loss or destructive schema action;
- an unsupported production configuration;
- a blocked installation or upgrade;
- incorrect compatibility decisions.

The correction still requires a focused technical review and automated validation. Reduce unrelated scope rather than bypassing quality checks.

## Roll back or correct forward

Prefer a corrective follow-up when the published structure and URLs remain safe. Roll back a documentation deployment when the publication:

- exposes confidential or embargoed information;
- directs readers to destructive or insecure actions;
- makes the site substantially unusable;
- contains broad broken navigation that cannot be corrected immediately.

When rolling back, preserve the corrective issue and reapply valid independent changes in a new pull request.

## Page moves and removals

A published page must not disappear without an explicit migration decision.

For a move:

```text
Old URL
→ permanent redirect
→ new canonical URL
```

For removed or unsupported behavior, retain a page or redirect that explains:

- the applicable version;
- why the content is no longer current;
- the supported replacement or upgrade path;
- where previous-version documentation can be found when maintained.

Keep redirects for at least the support lifecycle of the affected version. Preserve widely used URLs indefinitely when practical.

## Scheduled maintenance

Scheduled workflows may validate:

- external links;
- stale `last_reviewed` dates;
- orphan pages and redirects;
- drift between framework constants and manual reference;
- generated API freshness;
- accessibility of rendered pages;
- package and dependency security.

These checks complement pull-request validation and should create actionable reports rather than silently changing content.

## Related documentation

- [Issue and pull-request workflow](issues-and-pull-requests.md)
- [Preview environments](preview-environments.md)
- [Validate links and cross-references](link-validation.md)
- [Documentation architecture](documentation-architecture.md)
