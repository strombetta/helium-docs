---
title: Read and update an account profile
description: Read the authenticated account profile and update its display name through IAccountApplication.
uid: identity-account-profiles
content_type: how-to
area: identity
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Identity/IAccountApplication.cs
  - src/Trombetta.SaaS.Contracts/Identity/AccountProfile.cs
  - src/Trombetta.SaaS.Contracts/Identity/UpdateAccountProfileCommand.cs
---

# Read and update an account profile

Use the account application contract to read the current authenticated profile and update the display name supported by the Initial MVP.

## Prerequisites

- The request must have an authoritative authenticated account context.
- Resolve `IAccountApplication` from the request scope.
- Apply server-side authorization to the endpoint or UI action that exposes profile data.

## Read the profile

```csharp
OperationResult<AccountProfile> result =
    await accountApplication.GetProfileAsync(cancellationToken);
```

`AccountProfile` exposes the account identifier, read-only email address, verification state, and display name. Credential, token, session, and persistence details are excluded.

## Update the display name

```csharp
var command = new UpdateAccountProfileCommand("Alex Smith");

OperationResult<AccountProfile> result =
    await accountApplication.UpdateProfileAsync(command, cancellationToken);
```

Use the returned profile as the authoritative post-operation snapshot. Do not update the identity tables directly or infer success from submitted input.

## Email-address scope

The Initial MVP does not expose an email-address change operation. The profile email is read-only through this contract.

## Verify the result

After a successful update, verify that:

- `result.Value` identifies the authenticated account;
- the returned display name matches the accepted value;
- email and verification state remain authoritative framework values.

A missing authenticated account returns a controlled operation failure rather than a profile for another account.

## Troubleshooting

Use field errors for invalid display names. Preserve `CorrelationId` when the operation returns dependency or indeterminate failures.

## Next steps

Review [Authenticated account context](authenticated-account-context.md) and [Identity security considerations](security-considerations.md).
