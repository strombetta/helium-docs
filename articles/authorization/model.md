---
title: Authorization model
description: Understand Helium deny-by-default organization authorization, evaluation stages, current-state authority, and capability invariants.
uid: authorization-model
content_type: concept
area: authorization
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/architecture/decisions/organization-context-and-authorization.md
  - docs/engineering/organizations-context-and-authorization-specification.md
---

# Authorization model

Helium authorization is organization-scoped, deny-by-default, and based on current authoritative framework state.

> [!WARNING]
> This is the accepted WS-005 target model. Runtime policy evaluation and complete verification are not yet ready.

## Evaluation stages

A protected operation evaluates distinct stages:

1. authenticated account;
2. validated organization context;
3. current membership and role;
4. the named framework or consumer policy;
5. entitlement requirements where applicable;
6. ownership, version, target, and transition-specific invariants.

Passing one stage does not imply that later stages pass. UI visibility, route selection, cookie state, claims, and client-submitted roles are not authorization grants.

## Current-state authority

Authorization uses the current account, organization, membership, and role from local authoritative state. Membership removal and role change must affect later protected operations without a new login.

Unknown, malformed, unregistered, incomplete, or dependency-failed policy evaluation denies access. Positive authorization is not cached beyond a boundary that can preserve current-state semantics.

## Framework and consumer responsibilities

Framework policies protect Helium-owned operations. Consuming applications define additive product policies and protect consumer-owned records. A consumer policy may require framework policy and entitlement outcomes, but cannot replace or weaken framework handlers.

## Related tasks

- [Validated organization context](../organizations/validated-context.md)
- [Framework authorization policies](framework-policies.md)
- [Organization isolation](../organizations/isolation.md)
