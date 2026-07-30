---
title: Framework authorization policies
description: Reference the stable Helium organization policy identifiers and Initial MVP role matrix.
uid: authorization-framework-policies
content_type: reference
area: authorization
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Authorization/FrameworkAuthorizationPolicies.cs
  - docs/api/public-design.md
---

# Framework authorization policies

Use constants from `FrameworkAuthorizationPolicies` instead of duplicating string literals.

> [!WARNING]
> The identifiers and matrix are public contracts. Framework registration and handler readiness remain in progress in WS-005.

## Policy matrix

| Constant | Identifier | Owner | Administrator | Member |
| --- | --- | --- | --- | --- |
| `OrganizationsView` | `Trombetta.SaaS.Organizations.View` | Allow | Allow | Allow |
| `OrganizationsUpdate` | `Trombetta.SaaS.Organizations.Update` | Allow | Allow | Deny |
| `MembersView` | `Trombetta.SaaS.Members.View` | Allow | Allow | Deny |
| `MembersInvite` | `Trombetta.SaaS.Members.Invite` | Allow | Allow | Deny |
| `MembersChangeRole` | `Trombetta.SaaS.Members.ChangeRole` | Allow | Allow for non-Owner targets and results | Deny |
| `MembersRemove` | `Trombetta.SaaS.Members.Remove` | Allow subject to Owner invariant | Allow for non-Owner targets | Deny |
| `OwnershipTransfer` | `Trombetta.SaaS.Ownership.Transfer` | Allow | Deny | Deny |
| `BillingView` | `Trombetta.SaaS.Billing.View` | Allow | Allow | Deny |
| `BillingManage` | `Trombetta.SaaS.Billing.Manage` | Allow | Allow | Deny |

The matrix defines minimum role authorization. Capability-specific invariants can still deny the operation.

## Reserved names

The prefix `Trombetta.SaaS.` is reserved for framework policies. Consumer policy registration must reject reserved-prefix use and collisions with framework names.

## Related documentation

- [Authorization model](model.md)
- [Roles](../organizations/roles.md)
- [Policy identifiers reference](../../reference/authorization-policies.md)
