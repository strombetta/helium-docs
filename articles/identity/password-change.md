---
title: Change the current password
description: Change the authenticated account password through IAccountApplication and preserve session consistency.
uid: identity-change-password
content_type: how-to
area: identity
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Identity/IAccountApplication.cs
  - src/Trombetta.SaaS.Contracts/Identity/ChangePasswordCommand.cs
  - docs/engineering/ws-004-readiness.md
---

# Change the current password

Use `ChangePasswordAsync` when the authenticated account knows its current password and wants to replace it.

## Prerequisites

- The request has an authoritative authenticated account context.
- Resolve `IAccountApplication` from the request scope.
- Collect both passwords through a protected request without logging them.

## Submit the change

```csharp
var command = new ChangePasswordCommand(
    "<current-password>",
    "<new-password>");

OperationResult result =
    await accountApplication.ChangePasswordAsync(
        command,
        cancellationToken);
```

The new password uses the same Initial MVP policy as registration and reset. Password values are significant as supplied and are not trimmed.

## Credential and session behavior

The operation validates the current credential and changes the stored credential atomically. A failed operation preserves the old credential and session state. A successful security transition applies the framework's session-revocation policy.

## Verify the result

After success:

1. confirm the old password no longer authenticates;
2. confirm the new password authenticates;
3. confirm stale sessions do not remain authoritative;
4. confirm no password value appears in diagnostics.

## Troubleshooting

Return the controlled operation error rather than differentiating internal credential state. Use the correlation identifier for operator investigation.

## Next steps

Review [Sign out and revoke sessions](sign-out-and-revocation.md) and [Identity security considerations](security-considerations.md).
