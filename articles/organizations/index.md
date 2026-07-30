---
title: Organizations and tenancy
description: Use Helium organization contracts while WS-005 progresses from implemented persistence and settings foundations to complete context, membership administration, and authorization readiness.
uid: organizations
content_type: index
area: organizations
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/organizations-context-and-authorization-specification.md
  - docs/planning/implementation-plan.md
---

# Organizations and tenancy

Use these topics to understand and integrate Helium organization boundaries, current memberships, settings, active selection, invitations, ownership, isolation, and lifecycle facts.

> [!IMPORTANT]
> WS-005 is in progress. Organization persistence, membership discovery, organization retrieval and name updates, and the first-organization creation foundation are implemented. Active organization context, authorization, invitations, member administration, ownership transfer, complete isolation verification, and lifecycle integration remain in progress.

## Start here

- [Organization model](organization-model.md) — Understand the framework-owned governance and tenant boundary.
- [Create and retrieve organizations](create-and-retrieve.md) — Use the implemented discovery and retrieval surface.
- [Organization settings](settings.md) — Update the supported organization name with optimistic concurrency.

## Membership and governance contracts

- [Memberships](memberships.md)
- [Invitations](invitations.md)
- [Owner, Administrator, and Member roles](roles.md)
- [Ownership transfer](ownership-transfer.md)

## Context and isolation contracts

- [Active organization selection](active-organization.md)
- [Validated organization context](validated-context.md)
- [Organization isolation](isolation.md)
- [Organization lifecycle events](lifecycle-events.md)

## Next steps

Continue to [Authorization](../authorization/index.md) for the deny-by-default policy model and current implementation status.
