---
title: Protect ASP.NET Core endpoints
description: Prepare ASP.NET Core endpoint protection with stable Helium framework policies and validated organization context.
uid: authorization-protect-endpoints
content_type: how-to
area: authorization
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/organizations-context-and-authorization-specification.md
  - src/Trombetta.SaaS.Contracts/Authorization/FrameworkAuthorizationPolicies.cs
---

# Protect ASP.NET Core endpoints

Apply stable framework or consumer policies to every server-side endpoint that reads or mutates organization-scoped state.

> [!WARNING]
> ASP.NET Core requirements, handlers, middleware-order validation, and WS-005 readiness remain in progress. The examples show the accepted integration shape only.

## Prerequisites

- Register Helium and ASP.NET Core authorization in the supported composition root.
- Place authentication and organization-context middleware in the documented order.
- Use a stable policy constant or a validated consumer-owned policy name.

## Apply the policy

```csharp
[Authorize(Policy = FrameworkAuthorizationPolicies.MembersView)]
public async Task<IResult> GetMembersAsync(
    OrganizationId organizationId,
    CancellationToken cancellationToken)
{
    // Load members through the organization-scoped application contract.
    return Results.Ok();
}
```

Endpoint metadata does not replace capability-specific checks. The operation must still validate target ownership, version tokens, invitation state, last-Owner rules, and entitlements where required.

## Avoid client-side authority

Do not authorize from route values, hidden fields, headers, claims, cookies, or disabled UI controls. An explicit route organization identifier is a candidate scope that must be validated against current membership.

## Verify the result

Test authenticated and anonymous callers, all three framework roles, removed memberships, foreign organization identifiers, stale active preferences, unknown policies, and dependency outages. Confirm denied requests cannot read protected resource details.

## Next steps

Review [Protect application operations](protect-operations.md) and [Authorization troubleshooting](troubleshooting.md).
