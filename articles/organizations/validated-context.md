---
title: Validated organization context
description: Understand the immutable request-scoped OrganizationContext and the authoritative checks required to construct it.
uid: organizations-validated-context
content_type: concept
area: organizations
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Organizations/IOrganizationContextAccessor.cs
  - src/Trombetta.SaaS.Contracts/Organizations/OrganizationContext.cs
  - docs/engineering/organizations-context-and-authorization-specification.md
---

# Validated organization context

`OrganizationContext` represents the current account's validated membership and role for one organization during one request.

> [!WARNING]
> The public context types are established, but request resolution, hosting integration, invalidation, and readiness verification remain in progress in WS-005.

## Model

A context contains `AccountId`, `OrganizationId`, `MembershipId`, and the current `OrganizationRole`. Consumers read it through `IOrganizationContextAccessor.Current`.

A valid context requires current framework state to confirm:

- an authoritative authenticated account;
- an existing active organization;
- a current membership;
- membership ownership by the account and organization;
- the current semantic role loaded from local persistence.

## Authority boundary

Consumers cannot set or replace the current framework context. Constructing an `OrganizationContext` value, receiving an identifier from a client, or reading a claim does not establish authority.

The context establishes membership scope, not complete authorization. Protected operations must still evaluate the applicable framework or consumer policy and capability-specific invariants.

## Failure conditions

Missing membership, removed membership, stale preference, forged input, inaccessible organization, malformed selection, and validation dependency failure all fail closed and produce no usable context.

## Related tasks

- [Active organization selection](active-organization.md)
- [Evaluate organization authorization](../authorization/evaluate.md)
