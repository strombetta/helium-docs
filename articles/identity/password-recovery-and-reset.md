---
title: Recover and reset a password
description: Request enumeration-resistant password recovery and consume an opaque reset token.
uid: identity-password-recovery-reset
content_type: how-to
area: identity
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Identity/IAccountApplication.cs
  - src/Trombetta.SaaS.Contracts/Identity/RequestPasswordResetCommand.cs
  - src/Trombetta.SaaS.Contracts/Identity/ResetPasswordCommand.cs
  - docs/engineering/ws-004-readiness.md
---

# Recover and reset a password

The recovery flow has two separate operations: accept a recovery request without disclosing account existence, then consume the delivered opaque token with a new password.

## Prerequisites

- Resolve `IAccountApplication`.
- Configure durable transactional-email delivery.
- Keep email addresses, reset tokens, and passwords out of ordinary logs and telemetry.

## Request recovery

```csharp
var request = new RequestPasswordResetCommand("alex@example.com");

OperationResult<RecoveryAccepted> result =
    await accountApplication.RequestPasswordResetAsync(
        request,
        cancellationToken);
```

Registered and unregistered addresses produce the same safe accepted shape where the request itself is valid. The result does not disclose whether email was sent.

## Reset the password

```csharp
var command = new ResetPasswordCommand(
    token,
    "<new-password>");

OperationResult result =
    await accountApplication.ResetPasswordAsync(
        command,
        cancellationToken);
```

Invalid, expired, consumed, superseded, or incompatible tokens return `token_invalid_or_expired` without exposing the internal classification.

## Session consequences

Successful reset replaces the credential and revokes existing sessions. Old passwords and previously issued cookies must no longer authenticate.

## Verify the result

After reset:

1. confirm the reset operation succeeded;
2. confirm an existing session no longer produces an authenticated account context;
3. sign in using only the replacement password;
4. confirm the reset token cannot be replayed.

## Troubleshooting

An accepted recovery result is not evidence that an account exists or that delivery completed. Use bounded durable-delivery diagnostics for provider failures.

## Next steps

Review [Sign in with a password](password-sign-in.md) and [Authentication sessions](authentication-sessions.md).
