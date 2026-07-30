---
title: Sign out and revoke sessions
description: Revoke the current ASP.NET Core session and understand operations that revoke all account sessions.
uid: identity-sign-out-revoke
content_type: how-to
area: identity
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Hosting.AspNetCore/IPasswordSessionManager.cs
  - docs/engineering/password-sign-in-and-sessions.md
  - docs/engineering/ws-004-readiness.md
---

# Sign out and revoke sessions

Use `IPasswordSessionManager.SignOutAsync` to revoke the session associated with the current ASP.NET Core request.

## Prerequisites

- The request runs through the Helium authentication pipeline.
- Resolve `IPasswordSessionManager` from the request scope.
- Pass the current `HttpContext`.

## Sign out the current session

```csharp
OperationResult result =
    await sessionManager.SignOutAsync(
        httpContext,
        cancellationToken);
```

A successful operation revokes the server-side session and clears the framework-managed authentication state for the response.

## Account-wide revocation

The public sign-out operation targets the current session. Password reset and framework security invalidation revoke all existing sessions for the account. Consumers do not enumerate, mutate, or delete internal session rows.

## Verify the result

After sign-out:

1. issue a new request without reusing application test state;
2. confirm `IAuthenticatedAccountAccessor.Current` is `null`;
3. confirm protected operations return the application's unauthenticated outcome.

A replayed old cookie must not recreate an authenticated context.

## Troubleshooting

When a browser still displays authenticated UI after sign-out, distinguish cached presentation from a new protected server request. Authorization decisions must rely on current server state.

## Next steps

Review [Authentication sessions](authentication-sessions.md) and [Identity security considerations](security-considerations.md).
