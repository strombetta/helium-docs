---
title: Organizations and tenant context
description: Understand organizations as governance boundaries and how Helium validates an active organization before organization-scoped operations.
uid: fundamentals-organization-context
content_type: concept
area: organizations
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/organizations-context-and-authorization-specification.md
  - docs/api/public-design.md
---

# Organizations and tenant context

An organization is the Helium governance boundary used for memberships, framework roles, billing, entitlements, and organization-scoped operations. The term tenant describes isolation; organization is the precise domain term.

> [!IMPORTANT]
> The organizations, context, and authorization workstream is in progress. The model below is normative for implementation but is not yet a complete released capability.

## Organization context

A validated context contains:

- the authoritative authenticated account;
- the selected organization;
- the current membership;
- the current framework role.

The selected organization is only a preference. It may be represented through protected request-bound state, but it must be revalidated against current membership before protected operations.

## Context lifecycle

1. Identity resolves the authoritative account context.
2. Hosting extracts an organization candidate or stored preference.
3. Organizations validates that the organization exists and is active.
4. Organizations validates a current membership for the account.
5. The current role is loaded from authoritative local state.
6. Helium exposes an immutable request-scoped organization context.

If validation fails, the preference is ignored or cleared and no organization authority is granted.

## Invariants

- An organization identifier from a route, header, cookie, or form is not authority.
- A membership must belong to both the account and organization.
- Removed membership grants no context or permission.
- Organization-scoped operations ultimately use an explicit validated `OrganizationId`.
- Consumer product data must be scoped independently using the validated organization identity.

## Failure conditions

Context is unavailable when the account is unauthenticated, the organization is absent or inactive, the membership is absent or removed, the stored preference is stale, or an authoritative dependency cannot be evaluated safely.

## Security implications

Cross-organization requests must not reveal whether a protected resource exists. Context resolution and data filtering must be enforced server-side; UI selection and navigation state are not isolation controls.

## Implementation status

First-organization onboarding already creates an organization, Owner membership, and active preference atomically. General organization discovery, selection, context validation, membership administration, and authorization remain part of WS-005 implementation.

## Related tasks

- [Memberships, roles, and authorization](memberships-roles-authorization.md)
- [Framework and consumer data ownership](data-ownership.md)
- [Organizations and tenancy](../organizations/index.md)
