---
title: Authentication sessions
description: Understand Helium ordinary and persistent session lifetimes, renewal, validation, and authoritative state.
uid: identity-authentication-sessions
content_type: concept
area: identity
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/password-sign-in-and-sessions.md
  - src/Trombetta.SaaS.Hosting.AspNetCore/IPasswordSessionManager.cs
  - docs/engineering/ws-004-readiness.md
---

# Authentication sessions

Helium uses ASP.NET Core cookies backed by authoritative server-side session and account state. Cookie possession alone is not sufficient when the persisted session is expired, revoked, stale, or incompatible with current account security state.

## Model

| Session type | Idle lifetime | Absolute lifetime |
| --- | --- | --- |
| Ordinary | 8 hours | 24 hours |
| Persistent | 14 days | 30 days |

Sliding renewal can extend the idle boundary but never the absolute lifetime.

## Request validation

For protected requests, hosting reconstructs the current account from framework-issued authentication state and validates it against current persistence. Forged, stale, revoked, malformed, or missing sessions do not create an authenticated account context.

## Invariants

- Session and cookie identifiers are internal contracts.
- The current account is resolved authoritatively for each protected request.
- Explicit sign-out revokes the current session.
- Password reset and security invalidation revoke all existing sessions.
- Temporary dependency failure is not silently converted into an ordinary valid or invalid session.
- Session renewal cannot exceed the absolute expiration boundary.

## Failure conditions

Relevant states include idle expiry, absolute expiry, explicit revocation, password or security-version change, account unavailability, cookie forgery, and temporary persistence failure.

## Security considerations

Use HTTPS and the framework cookie configuration. Do not log cookie contents, session identifiers, claims principals, or authentication tickets. UI visibility is not an authorization boundary; organization access still requires validated membership and policy evaluation.

## Implementation status

The WS-004 hosted test path verifies real HTTPS cookies, ordinary and persistent expiration, renewal, absolute clamping, sign-out, revocation, replay rejection, and temporary validation dependency failure.

## Related tasks

- [Sign in with a password](password-sign-in.md)
- [Sign out and revoke sessions](sign-out-and-revocation.md)
- [Authenticated account context](authenticated-account-context.md)
