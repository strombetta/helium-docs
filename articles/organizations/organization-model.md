---
title: Organization model
description: Understand Helium organizations, memberships, invitations, ownership, active preference, and tenant-boundary terminology.
uid: organizations-model
content_type: concept
area: organizations
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/organizations-context-and-authorization-specification.md
  - docs/api/public-design.md
---

# Organization model

An organization is the Helium-owned governance boundary for memberships, framework roles, active context, billing authority, and other organization-scoped framework capabilities.

## Model

- An organization has a stable `OrganizationId`, a mutable name, an opaque version token, and the Initial MVP state `active`.
- A membership links one account to one organization and carries one semantic framework role.
- An invitation is a single-use, email-bound offer to create a membership. It is not itself membership authority.
- Ownership is represented by one or more current memberships with role `Owner`; there is no separate primary-owner field.
- The active-organization preference is navigation state only. It must be revalidated before protected use.

Use **organization** for framework contracts and persisted state. Use **tenant** only when describing the security-isolation property of organization-scoped data.

## Invariants

- Every organization has at least one current Owner.
- One account has at most one current membership in an organization.
- Removed membership history grants no context or authority.
- Role authority comes from current framework state, not claims, routes, headers, or cookies.
- Organization-owned reads and mutations require explicit authoritative organization scope.
- General creation of additional organizations after onboarding is not part of the Initial MVP public API.

## Current implementation status

Organization persistence, first-organization creation, membership discovery, organization retrieval, and organization-name updates are implemented preview foundations. Invitation administration, general member administration, active context, authorization, ownership transfer, and complete isolation verification remain in WS-005.

## Related tasks

- [Discover and retrieve organizations](create-and-retrieve.md)
- [Update organization settings](settings.md)
- [Validated organization context](validated-context.md)
