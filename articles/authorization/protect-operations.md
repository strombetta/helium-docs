---
title: Protect application operations
description: Structure server-side application operations so policy evaluation and capability invariants are enforced before mutation.
uid: authorization-protect-operations
content_type: how-to
area: authorization
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/organizations-context-and-authorization-specification.md
  - src/Trombetta.SaaS.Contracts/Authorization/IOrganizationAuthorizationEvaluator.cs
---

# Protect application operations

Protect organization-scoped product and framework operations at the server-side execution boundary. UI visibility is not sufficient.

> [!WARNING]
> The WS-005 evaluator and policy implementation remain in progress. Use this structure as integration guidance, not as a readiness claim.

## Prerequisites

- Resolve an authoritative account and validated organization context.
- Identify the exact policy required by the operation.
- Keep consumer-owned persistence and transactions separate from Helium internals.

## Enforce the operation boundary

1. Validate structural input without loading foreign organization data.
2. Evaluate the required framework or consumer policy.
3. Load the target through an organization-scoped query.
4. Apply capability-specific ownership, version, entitlement, and transition invariants.
5. Perform the mutation in the owning transaction.
6. Record consumer-owned durable work or lifecycle reactions using stable idempotency identities.

Do not authorize from submitted roles, cached UI state, route values, or a previously positive decision from another request.

## Handle denial

Return a bounded authorization or not-found-equivalent result according to the disclosure model. Preserve correlation identifiers for diagnostics but omit protected resource state and raw exceptions.

## Verify the result

Test Owner, Administrator, Member, removed membership, foreign organization, stale version, dependency outage, and concurrent state-change cases. Confirm that denied paths do not read or mutate cross-organization records.

## Next steps

Review [Organization isolation](../organizations/isolation.md) and [Define consumer policies](consumer-policies.md).
