---
title: Memberships
description: Understand current and removed organization memberships, public administration contracts, pagination, concurrency, and implementation status.
uid: organizations-memberships
content_type: concept
area: organizations
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Organizations/IMembershipApplication.cs
  - docs/engineering/organizations-context-and-authorization-specification.md
---

# Memberships

A membership is the historical relationship between one account and one organization. Only a current membership carries a framework role and can participate in validated organization context.

> [!WARNING]
> The membership-administration operations documented here are accepted public contracts, but their WS-005 implementation and readiness verification are still in progress.

## Model

- `MembershipId` identifies the relationship.
- `OrganizationId` and `AccountId` are immutable membership ownership values.
- Current memberships use `Owner`, `Administrator`, or `Member`.
- Removed memberships are retained as history and grant no authority.
- One account can have at most one current membership in an organization.

## Administration contract

`IMembershipApplication` defines member listing, invitation listing and issuance, invitation revocation and acceptance, role change, member removal, and ownership transfer. Member and invitation lists use cursor pagination with a default page size of 50 and maximum of 200.

Mutations use opaque version-token preconditions where specified. Stale values return `concurrency_conflict`.

## Invariants

- An operation cannot mutate a membership owned by another organization.
- Ordinary role change cannot assign or remove `Owner`; ownership uses the dedicated transfer workflow.
- No mutation may leave the organization without an Owner.
- Self-service organization departure is outside the Initial MVP.
- Membership and required lifecycle work commit atomically.

## Current implementation status

Organization persistence and current-account membership discovery are implemented. Member listing, role change, removal, invitations, ownership transfer, context invalidation, and final readiness evidence remain in progress.

## Related tasks

- [Roles](roles.md)
- [Invitations](invitations.md)
- [Ownership transfer](ownership-transfer.md)
