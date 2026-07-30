---
title: Active organization selection
description: Understand the target ASP.NET Core selection contract and why an active-organization preference is never authorization authority.
uid: organizations-active-selection
content_type: concept
area: organizations
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/api/public-design.md
  - docs/engineering/organizations-context-and-authorization-specification.md
---

# Active organization selection

Active organization selection is an ASP.NET Core hosting concern that stores a navigation preference after validating current membership.

> [!WARNING]
> `IActiveOrganizationSelection`, protected preference storage, stale-selection clearing, and hosted validation remain in progress in WS-005.

## Model

The target contract exposes `SelectAsync(HttpContext, OrganizationId, CancellationToken)` and `ClearAsync(HttpContext, CancellationToken)`.

Selection must validate the current authenticated account and current membership before storing a preference. The preference may use a protected cookie or equivalent request-bound mechanism, but it is not a durable capability token.

## Resolution rules

- Zero valid memberships produce no organization context.
- One valid membership may be selected deterministically according to the supported hosting flow.
- Multiple valid memberships require explicit selection.
- An explicit operation organization identifier takes precedence over a stored preference and is validated independently.
- Removed, malformed, forged, or inaccessible selections are ignored or cleared.
- Membership and role changes must affect subsequent protected operations without reauthentication.

## Security boundary

Routes, forms, headers, claims, cookies, and stored preferences cannot establish membership or role. Selection grants no framework policy, entitlement, ownership, or consumer permission by itself.

## Related tasks

- [Validated organization context](validated-context.md)
- [Authorization model](../authorization/model.md)
