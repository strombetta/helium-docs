---
title: Memberships, roles, and authorization
description: Understand the relationship between organization membership, fixed framework roles, validated context, policies, and capability invariants.
uid: fundamentals-memberships-roles-authorization
content_type: concept
area: authorization
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/organizations-context-and-authorization-specification.md
  - docs/api/public-design.md
---

# Memberships, roles, and authorization

Authentication, membership, role, policy, and entitlement answer different questions. A protected operation may require all of them.

> [!IMPORTANT]
> The authorization model is specified but the complete WS-005 implementation is still in progress.

## Model

A membership is the relationship between one account and one organization. A current membership carries exactly one fixed framework role:

- `Owner`;
- `Administrator`;
- `Member`.

Removed membership is retained as history and grants no authority. Roles are semantic values and must not be compared by numeric or declaration order.

## Framework authorization

Framework policies evaluate current authoritative state. The Initial MVP policy model covers organization viewing and update, member viewing and administration, ownership transfer, and billing access.

| Capability | Owner | Administrator | Member |
| --- | --- | --- | --- |
| View organization | Allow | Allow | Allow |
| Update organization | Allow | Allow | Deny |
| View, invite, or manage ordinary members | Allow | Allow with target restrictions | Deny |
| Transfer ownership | Allow | Deny | Deny |
| View or manage billing | Allow | Allow | Deny |

Capability invariants can impose additional restrictions after a policy allows the caller.

## Ownership invariant

Every organization must retain at least one current Owner. Ownership transfer promotes the selected current member and demotes the acting Owner to Administrator atomically while preserving any additional Owners.

## Consumer policies

Consumer applications may define additive product policies that require framework policies or entitlements. Consumer policies must not redefine framework roles, weaken framework authorization, infer membership from claims, or treat UI visibility as enforcement.

## Failure conditions

Expected denials include unauthenticated access, missing context, absent or removed membership, insufficient role, stale version token, cross-organization target, last-Owner violation, or an unmet capability invariant.

## Security implications

A positive framework policy decision does not bypass data scoping, optimistic concurrency, ownership invariants, subscription state, or entitlement checks. Authorization must protect server-side outcomes, not only navigation or page visibility.

## Related tasks

- [Organizations and tenant context](organizations-and-tenant-context.md)
- [Plans, subscriptions, and entitlements](plans-subscriptions-entitlements.md)
- [Authorization](../authorization/index.md)
