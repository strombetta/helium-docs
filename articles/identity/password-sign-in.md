---
title: Sign in with a password
description: Create an ordinary or persistent ASP.NET Core session with IPasswordSessionManager.
uid: identity-password-sign-in
content_type: how-to
area: identity
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Hosting.AspNetCore/IPasswordSessionManager.cs
  - src/Trombetta.SaaS.Hosting.AspNetCore/PasswordSignInCommand.cs
  - docs/engineering/ws-004-readiness.md
---

# Sign in with a password

Use `IPasswordSessionManager.SignInAsync` inside an ASP.NET Core request to validate credentials and issue a framework-managed server session.

## Prerequisites

- Helium hosting middleware and authentication services are registered in the supported order.
- Resolve `IPasswordSessionManager` from the request scope.
- Pass the current `HttpContext`; do not construct an authentication ticket or cookie yourself.

## Submit credentials

```csharp
var command = new PasswordSignInCommand(
    "alex@example.com",
    "<password>",
    isPersistent: false);

OperationResult<AuthenticatedSession> result =
    await sessionManager.SignInAsync(
        httpContext,
        command,
        cancellationToken);
```

Set `isPersistent` to `true` only when the user explicitly requests a persistent session.

## Handle failures safely

Unknown accounts, incorrect passwords, non-disclosable account state, and lockout normally return:

```text
invalid_credentials
```

`account_not_verified` may be returned only after correct credential proof where it does not introduce additional account-enumeration disclosure.

## Session result

A successful `AuthenticatedSession` exposes the account identifier, expiration instant, and persistence flag. Session identifiers, cookie contents, claims construction, password hashes, and storage records are internal.

## Verify the result

Verify that:

- the result is successful;
- `ExpiresAt` is a UTC instant in the future;
- the next authenticated request has a non-null `IAuthenticatedAccountAccessor.Current` value.

Do not treat possession of the returned account identifier as authentication for another request.

## Troubleshooting

Repeated failures may activate lockout. Preserve the generic public response and use bounded operator diagnostics rather than returning account-specific detail.

## Next steps

Review [Authentication sessions](authentication-sessions.md) and [Authenticated account context](authenticated-account-context.md).
