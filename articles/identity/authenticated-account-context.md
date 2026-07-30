---
title: Read the authenticated account context
description: Read authoritative request-scoped account identity through IAuthenticatedAccountAccessor.
uid: identity-authenticated-account-context
content_type: how-to
area: identity
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Identity/IAuthenticatedAccountAccessor.cs
  - src/Trombetta.SaaS.Contracts/Identity/AccountContext.cs
  - docs/engineering/ws-004-readiness.md
---

# Read the authenticated account context

Use `IAuthenticatedAccountAccessor` to read the framework-authenticated account for the current request.

## Prerequisites

- The request runs after the Helium authentication middleware.
- Resolve the accessor from the request scope.
- Do not cache the accessor or its value across requests.

## Read the current account

```csharp
AccountContext? account = authenticatedAccountAccessor.Current;

if (account is null)
{
    // Return the application's unauthenticated response.
}
```

`AccountContext` exposes `AccountId`, normalized `Email`, and `IsEmailVerified`.

## Authority boundary

Only the value populated by the framework-provided accessor is authoritative. Constructing an `AccountContext`, receiving an account identifier from a client, or reading an arbitrary claim does not establish authentication.

The account context establishes account identity only. It does not prove organization membership, organization role, billing authority, or entitlement access.

## Verify the result

For an authenticated request, verify that:

- `Current` is non-null;
- the account identifier remains stable for the request;
- verification state reflects current framework persistence;
- organization-scoped work still requires validated organization context and authorization.

For an anonymous, revoked, forged, stale, or expired session, `Current` must be `null`.

## Troubleshooting

When `Current` is unexpectedly null, inspect middleware ordering, cookie and session validation, schema compatibility, and dependency health. Do not reconstruct authority from the cookie or claims as a fallback.

## Next steps

Continue to [Onboarding state](../onboarding/state.md) or [Organizations and tenant context](../fundamentals/organizations-and-tenant-context.md).
