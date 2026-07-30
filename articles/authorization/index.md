---
title: Authorization
description: Understand and prepare for Helium deny-by-default organization authorization while WS-005 context resolution and policy implementation remain in progress.
uid: authorization
content_type: index
area: authorization
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/api/public-design.md
  - docs/engineering/organizations-context-and-authorization-specification.md
  - docs/planning/implementation-plan.md
---

# Authorization

Use these topics to understand Helium framework policies, provider-neutral evaluation, endpoint and operation protection, role and entitlement composition, and consumer-owned additive policies.

> [!WARNING]
> The public authorization contracts and normative policy matrix are established, but validated organization context, framework handlers, evaluator behavior, endpoint adapters, consumer composition guards, and readiness verification remain in progress in WS-005.

## Start here

- [Authorization model](model.md) — Understand the deny-by-default evaluation stages.
- [Framework authorization policies](framework-policies.md) — Use stable identifiers and the Initial MVP role matrix.
- [Evaluate organization authorization](evaluate.md) — Prepare integration against the provider-neutral evaluator.

## Integration guidance

- [Protect application operations](protect-operations.md)
- [Protect ASP.NET Core endpoints](protect-endpoints.md)
- [Combine roles and entitlements](roles-and-entitlements.md)
- [Define consumer policies](consumer-policies.md)

## Troubleshooting

Use [Authorization troubleshooting](troubleshooting.md) to diagnose missing context, policy denial, stale membership state, and configuration failures.
