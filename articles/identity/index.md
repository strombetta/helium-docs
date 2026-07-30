---
title: Identity and accounts
description: Use the implemented Helium preview contracts for registration, verification, profiles, password sessions, recovery, account context, and identity lifecycle events.
uid: identity
content_type: index
area: identity
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/ws-004-readiness.md
  - docs/api/public-design.md
---

# Identity and accounts

Use these topics to integrate the account lifecycle implemented and verified by the Helium preview.

> [!IMPORTANT]
> The contracts and hosted behavior documented here exist in the framework repository, but coordinated consumer packages and the official project template are not yet published. Treat code examples as preview API guidance rather than installation instructions.

## Start here

- [Register an account](account-registration.md) — Submit an enumeration-resistant registration request.
- [Verify an email address](email-verification.md) — Consume the opaque verification token delivered by Helium.
- [Sign in with a password](password-sign-in.md) — Create an ordinary or persistent ASP.NET Core session.
- [Read the authenticated account context](authenticated-account-context.md) — Use authoritative request-scoped account state.

## Common tasks

- [Read and update an account profile](account-profiles.md)
- [Sign out and revoke sessions](sign-out-and-revocation.md)
- [Recover and reset a password](password-recovery-and-reset.md)
- [Change the current password](password-change.md)

## Key concepts

- [Authentication sessions](authentication-sessions.md)
- [Lockout and abuse resistance](lockout-and-abuse-resistance.md)
- [Identity lifecycle events](lifecycle-events.md)
- [Identity security considerations](security-considerations.md)

## Onboarding

After verification and sign-in, use [Onboarding](../onboarding/index.md) to discover state and create the account's first organization atomically.

## Troubleshooting

Identity operations return provider-neutral `OperationResult` values. Start with [Operation results and errors](../fundamentals/operation-results-and-errors.md) and preserve the returned correlation identifier when collecting diagnostics.

## Reference

The supported surface is limited to documented types in `Trombetta.SaaS.Contracts.Identity` and `Trombetta.SaaS.Hosting.AspNetCore`. Persistence entities, credentials, tokens, session identifiers, cookie contents, claims construction, and provider implementation types are not public contracts.
