---
title: Combine roles and entitlements
description: Understand why organization role authorization and product entitlement evaluation are separate additive decisions.
uid: authorization-roles-entitlements
content_type: concept
area: authorization
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/api/public-design.md
  - docs/engineering/organizations-context-and-authorization-specification.md
---

# Combine roles and entitlements

Framework roles answer whether the current membership may perform an organization-governance operation. Entitlements answer whether the organization currently has access to a product capability.

> [!WARNING]
> WS-005 authorization and WS-006 entitlement implementation are not ready. This page defines the accepted composition boundary.

## Separate decisions

A role decision must not infer subscription or plan access. An entitlement decision must not infer membership administration authority.

A protected paid operation generally requires:

1. authenticated account;
2. validated organization context;
3. an allowed organization or consumer policy;
4. an allowed entitlement decision;
5. operation-specific target and version invariants.

Each stage can deny independently and should produce a bounded safe result.

## Billing policies

`Billing.View` and `Billing.Manage` are framework role policies. They govern who may inspect or administer normalized billing state; they do not prove that a plan or entitlement is active.

## Request-time boundary

Protected request authorization uses authoritative local organization and entitlement state. It must not call Stripe or another provider synchronously to decide access.

## Consumer composition

A consumer policy may require a framework policy, explicit framework roles, a product-specific requirement, and a consumer entitlement check. It cannot weaken the framework policy or replace the provider-neutral entitlement evaluator.

## Related tasks

- [Framework authorization policies](framework-policies.md)
- [Entitlements](../entitlements/index.md)
- [Billing](../billing/index.md)
