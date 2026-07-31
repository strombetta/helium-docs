---
title: Ownership transfer
description: Understand the dedicated atomic Owner-only organization ownership-transfer contract and its implementation status.
uid: organizations-ownership-transfer
content_type: concept
area: organizations
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Organizations/IMembershipApplication.cs
  - docs/api/public-design.md
  - docs/engineering/organizations-context-and-authorization-specification.md
---

# Ownership transfer

Ownership transfer is a dedicated organization operation. Ordinary role mutation must not reproduce or bypass it.

> [!WARNING]
> The public contract is established, but atomic ownership-transfer implementation and readiness verification remain in progress in WS-005.

## Target transition

A successful `TransferOwnershipAsync` operation:

1. validates that the acting membership is a current Owner;
2. validates that the target is an eligible current membership in the same organization;
3. checks the expected organization version;
4. promotes the selected membership to Owner;
5. demotes the acting Owner to Administrator;
6. preserves any other existing Owners;
7. records the supported lifecycle facts in the same transaction.

The result contains the committed previous-owner snapshot, new-owner snapshot, and new organization version.

## Invariants

- Only a current Owner may initiate transfer.
- The target must belong to the explicit organization.
- The organization never commits a state without an Owner.
- Stale organization versions return `concurrency_conflict`.
- Cross-organization targets use not-found-equivalent behavior.
- Active context and authorization must reflect committed roles without reauthentication.

## Related tasks

- [Roles](roles.md)
- [Memberships](memberships.md)
- [Organization lifecycle events](lifecycle-events.md)
