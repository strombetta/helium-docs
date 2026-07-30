---
title: Owner, Administrator, and Member roles
description: Understand the closed Initial MVP organization role model and the invariants that constrain role administration.
uid: organizations-roles
content_type: concept
area: organizations
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/api/public-design.md
  - docs/engineering/organizations-context-and-authorization-specification.md
---

# Owner, Administrator, and Member roles

Helium defines three semantic framework roles for the Initial MVP. The set is closed and must not be treated as an ordinal hierarchy.

## Owner

An Owner may perform the framework operations allowed by the policy matrix, including ownership transfer. Owner is not an unrestricted superuser: capability-specific invariants, version tokens, current membership, and organization scope still apply.

## Administrator

An Administrator may update organization settings and administer eligible non-Owner members according to the policy matrix. An Administrator cannot assign, demote, change, or remove an Owner.

## Member

A Member can view the organization but is denied framework administration and billing-management policies unless a separate documented framework policy allows the operation.

## Role-transition rules

- Ordinary role change supports only `Administrator` and `Member` target roles.
- `TransferOwnershipAsync` is the only operation that promotes the selected membership to Owner and demotes the acting Owner.
- Removing or changing roles must preserve at least one current Owner.
- Current role is loaded from authoritative framework state and changes take effect without requiring reauthentication.
- Consumer roles and permissions are separate additive product concepts; they cannot redefine framework roles.

## Current implementation status

The public role types and normative matrix are established. Complete member administration, ownership transfer, active-context refresh, and policy evaluation remain in WS-005.

## Related tasks

- [Framework authorization policies](../authorization/framework-policies.md)
- [Memberships](memberships.md)
- [Ownership transfer](ownership-transfer.md)
