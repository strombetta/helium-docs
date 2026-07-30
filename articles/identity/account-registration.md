---
title: Register an account
description: Submit an enumeration-resistant account registration request through IAccountApplication.
uid: identity-register-account
content_type: how-to
area: identity
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Identity/IAccountApplication.cs
  - src/Trombetta.SaaS.Contracts/Identity/RegisterAccountCommand.cs
  - docs/engineering/ws-004-readiness.md
---

# Register an account

Use `IAccountApplication.RegisterAsync` to accept an email address, password, and display name without exposing whether an equivalent account already exists.

## Prerequisites

- Resolve `IAccountApplication` from the application service provider.
- Configure the Helium identity persistence and durable transactional-email path.
- Collect the password without logging, tracing, or retaining it outside the request.

## Submit the request

```csharp
var command = new RegisterAccountCommand(
    "alex@example.com",
    "<password>",
    "Alex");

OperationResult<RegistrationAccepted> result =
    await accountApplication.RegisterAsync(command, cancellationToken);
```

`RegisterAccountCommand` is sensitive. Its string representation redacts the email, password, and display name, but the application must still avoid automatic request-body logging.

## Handle the result

A successful result contains the marker `RegistrationAccepted`. The same safe accepted shape is used for a new address and an existing normalized-equivalent address. It does not disclose an account identifier, existence flag, verification status, token, delivery result, or provider detail.

Expected validation or rate-limit failures use `OperationError`. Preserve `CorrelationId` for diagnostics and render only the safe public message and field errors.

## Password policy

The preview policy accepts 12 through 128 Unicode characters. Passwords are not trimmed, leading and trailing characters are significant, and no mandatory uppercase, lowercase, digit, or symbol composition rule exists. The complete normalized email address cannot appear in the password.

## Verify the result

Confirm that the operation returned either:

- a successful `RegistrationAccepted` marker; or
- a bounded validation, configuration, dependency, or rate-limit error.

Do not verify account existence through direct database access. The user completes the supported path by consuming the verification action delivered by Helium.

## Troubleshooting

When repeated registration requests return the same accepted shape, that behavior is intentional and prevents account enumeration. Diagnose missing email through durable-work and provider diagnostics rather than changing the public response.

## Next steps

Continue to [Verify an email address](email-verification.md).
