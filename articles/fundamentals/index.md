---
title: Fundamentals
description: Understand Helium architecture, composition, contracts, domain boundaries, lifecycle behavior, durable processing, and data ownership.
uid: fundamentals
content_type: index
area: architecture
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/architecture/decisions/application-architecture.md
  - docs/api/public-design.md
  - docs/planning/implementation-plan.md
---

# Fundamentals

Use these conceptual topics to understand how Helium fits together before you implement product capabilities or depend on framework contracts.

> [!IMPORTANT]
> Helium is in preview. Some fundamentals describe verified implementation, while others describe accepted target contracts for workstreams that are still in progress. Each page identifies its current implementation status.

## Start here

- [Reference application architecture](reference-architecture.md) — Understand the supported modular-monolith topology.
- [Packages and modules](packages-and-modules.md) — Distinguish distribution artifacts from logical capability boundaries.
- [Application composition](application-composition.md) — Understand the consumer-owned composition root.
- [Public contracts and internal implementation](public-contracts.md) — Identify supported dependencies and unsupported internals.

## Identity and organization model

- [Accounts and authenticated account context](accounts-and-account-context.md)
- [Organizations and tenant context](organizations-and-tenant-context.md)
- [Memberships, roles, and authorization](memberships-roles-authorization.md)
- [Plans, subscriptions, and entitlements](plans-subscriptions-entitlements.md)

## Cross-cutting behavior

- [Operation results and errors](operation-results-and-errors.md)
- [Lifecycle events](lifecycle-events.md)
- [Durable processing](durable-processing.md)
- [Framework and consumer data ownership](data-ownership.md)

## Next steps

Continue to [Build with Helium](../build/index.md) for capability guidance or use the [Reference](../../reference/index.md) section for exact contracts and values.
