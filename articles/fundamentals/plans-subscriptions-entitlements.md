---
title: Plans, subscriptions, and entitlements
description: Understand how Helium separates product plans, provider commerce facts, normalized subscription state, and product-access decisions.
uid: fundamentals-plans-subscriptions-entitlements
content_type: concept
area: billing
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/architecture/decisions/application-architecture.md
  - docs/api/public-design.md
  - docs/planning/implementation-plan.md
---

# Plans, subscriptions, and entitlements

Plans describe product offerings. Subscription state describes the organization's normalized commerce state. Entitlements answer whether a product capability is available. These concepts are related but not interchangeable.

> [!WARNING]
> Billing and entitlement workstreams have not started. This page describes the accepted public model, not an executable preview capability.

## Plan model

A plan uses a stable provider-neutral key, display name, free or paid kind, supported billing intervals, optional trial duration, and a set of entitlement keys. Stripe Price IDs belong to adapter configuration and do not appear in the plan contract.

## Subscription authority

Stripe is authoritative for provider-side commerce facts. Helium maintains a normalized local subscription snapshot for application behavior. Known target states include `none`, `trialing`, `active`, `past_due`, `paused`, `canceled`, `incomplete`, and `unknown`.

Protected request-time access decisions must not call Stripe. Delayed or duplicate provider events are processed durably and update local state before application-facing evaluation changes.

## Entitlement evaluation

An entitlement uses a stable key such as `features.export`. Evaluation combines:

- organization state;
- configured plan;
- normalized local subscription state;
- applicable access-period boundaries.

The result is provider-neutral and includes an opaque entitlement-set version. Unknown configured keys are configuration errors, not ordinary denied decisions.

## Invariants

- One organization has at most one active subscription in the Initial MVP.
- Provider identifiers do not become domain identifiers.
- Free-plan entitlements are evaluated independently of paid-subscription state.
- Paid entitlements are denied conservatively when state is unavailable or inactive.
- Role authorization and entitlement evaluation remain separate checks.

## Failure conditions

Expected failures include missing billing configuration, unknown plan or entitlement key, unavailable normalized state, idempotency conflict, provider dependency failure, and indeterminate external outcome.

## Security implications

Client-visible plan or subscription state does not authorize access. Server-side operations must evaluate the validated organization, required framework or consumer policy, current normalized subscription state, and required entitlement.

## Related tasks

- [Memberships, roles, and authorization](memberships-roles-authorization.md)
- [Billing and subscriptions](../billing/index.md)
- [Entitlements](../entitlements/index.md)
