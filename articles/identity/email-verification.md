---
title: Verify an email address
description: Consume an opaque Helium verification token through IAccountApplication.
uid: identity-verify-email
content_type: how-to
area: identity
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Identity/IAccountApplication.cs
  - src/Trombetta.SaaS.Contracts/Identity/VerifyEmailCommand.cs
  - docs/engineering/ws-004-readiness.md
---

# Verify an email address

Use `VerifyEmailAsync` to consume the opaque token delivered by the Helium transactional-email workflow.

## Prerequisites

- Registration has been accepted.
- The application has obtained the token from the supported verification link or form submission.
- The token has not been written to logs, telemetry, browser analytics, or exception messages.

## Submit the token

```csharp
var command = new VerifyEmailCommand(token);

OperationResult result =
    await accountApplication.VerifyEmailAsync(command, cancellationToken);
```

Treat the token as an opaque sensitive string. Do not parse it, derive identifiers from it, or depend on its protected representation.

## Handle invalid states

Invalid, expired, consumed, superseded, malformed, wrong-purpose, or otherwise unacceptable tokens use the stable code:

```text
token_invalid_or_expired
```

The public result deliberately does not distinguish those internal states.

## Post-commit behavior

Successful verification commits authoritative account and token state before post-commit lifecycle handlers execute. Handler or email-provider failure cannot roll back the verified account.

## Verify the result

After success:

1. read the current profile or authenticated account context;
2. confirm `IsEmailVerified` is `true`;
3. continue to sign-in or onboarding according to the application flow.

Do not verify success by inspecting token tables or protected token material.

## Troubleshooting

A token copied from an older email may have been superseded. Request the application to use the most recent supported verification action rather than attempting to classify token internals.

## Next steps

Continue to [Sign in with a password](password-sign-in.md) or review [Identity lifecycle events](lifecycle-events.md).
