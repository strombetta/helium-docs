---
title: Overview
description: Evaluate the Helium preview, its supported application model, architecture, technology baseline, scope, and current implementation status.
uid: product-overview
content_type: index
area: product
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/planning/implementation-plan.md
  - docs/architecture/technical-architecture.md
---

# Overview

Use this section to determine whether the Helium Initial MVP direction fits your application before you depend on framework artifacts or plan an adoption project.

> [!IMPORTANT]
> Helium is under active development. No supported consumer release or installable project-template package is currently available. The Overview documents the accepted architecture, implemented foundations, target Initial MVP, and current limitations.

## Start here

- [What is Helium?](what-is-helium.md) — Understand the product direction and current availability.
- [Supported application model](supported-application-model.md) — Review the one adoption and deployment model targeted by the Initial MVP.
- [Supported versions](supported-versions.md) — Check the accepted runtime and database compatibility baseline.

## Evaluate the product direction

- [Why use Helium?](why-use-helium.md)
- [Helium and `Trombetta.SaaS` naming](naming.md)
- [Architecture at a glance](architecture-at-a-glance.md)
- [Product scope and current limitations](scope-and-limitations.md)

## Current implementation status

The framework implementation plan recorded the following workstream state on July 30, 2026:

| Area | Status |
| --- | --- |
| Architecture and engineering foundation | Complete |
| Public contracts and module composition | Complete |
| Persistence, migrations, and durable processing | Complete |
| Identity and onboarding | Complete |
| Organizations, context, and authorization | In progress |
| Billing, subscription state, and entitlements | Not started |
| Transactional email and lifecycle reactions | Not started |
| Reference UI, settings, and project template | Not started |
| Configuration, observability, security, and deployment | Not started |
| Packaging, releases, compatibility, and upgrades | Not started |

This table reports engineering progress. It is not a release-support declaration. A capability is not available to consumers merely because an internal workstream is complete.

## Next steps

Review the [product scope and current limitations](scope-and-limitations.md). Then check [Get started](../getting-started/index.md) for the prerequisites that can be prepared before the first supported template release.