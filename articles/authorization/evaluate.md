---
title: Evaluate organization authorization
description: Prepare programmatic policy evaluation through IOrganizationAuthorizationEvaluator without depending on HttpContext.
uid: authorization-evaluate
content_type: how-to
area: authorization
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Authorization/IOrganizationAuthorizationEvaluator.cs
  - src/Trombetta.SaaS.Contracts/Authorization/AuthorizationDecision.cs
  - docs/engineering/organizations-context-and-authorization-specification.md
---

# Evaluate organization authorization

`IOrganizationAuthorizationEvaluator` is the provider-neutral contract for programmatic organization authorization outside an ASP.NET Core endpoint handler.

> [!WARNING]
> The contract is established, but evaluator implementation and WS-005 readiness remain in progress. Do not treat this page as production-availability confirmation.

## Prerequisites

- The current execution has an authoritative authenticated account.
- The operation supplies an explicit `OrganizationId`.
- Use a constant from `FrameworkAuthorizationPolicies`.
- Preserve capability-specific invariant checks after policy evaluation.

## Evaluate a policy

```csharp
AuthorizationDecision decision = await authorizationEvaluator.AuthorizeAsync(
    organizationId,
    FrameworkAuthorizationPolicies.OrganizationsUpdate,
    cancellationToken);

if (!decision.IsAllowed)
{
    return OperationResult.Failure(
        OperationErrorCodes.Forbidden,
        correlationId);
}
```

Adapt result construction to the supported `OperationResult` factories in the consuming codebase. Do not expose internal denial diagnostics to unauthorized callers.

## Interpret the decision

`AuthorizationDecision` contains the evaluated policy, organization identifier, optional effective role, allowed state, and a safe denial code. A positive decision does not satisfy version-token, target-membership, ownership, invitation, billing, or entitlement invariants.

## Verify the result

Verify that:

- unknown or malformed policy names deny;
- foreign organization identifiers do not disclose protected state;
- role changes and membership removal affect subsequent evaluation;
- dependency failure denies rather than using stale positive authority;
- the evaluation path does not require `HttpContext`.

## Next steps

Continue to [Protect application operations](protect-operations.md) or [Protect ASP.NET Core endpoints](protect-endpoints.md).
