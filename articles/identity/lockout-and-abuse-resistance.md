---
title: Account lockout and abuse resistance
description: Understand generic credential failures, sign-in lockout, bounded operation limits, and enumeration resistance.
uid: identity-lockout-abuse-resistance
content_type: concept
area: identity
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/password-sign-in-and-sessions.md
  - docs/engineering/identity-and-onboarding-specification.md
  - docs/engineering/ws-004-readiness.md
---

# Account lockout and abuse resistance

Identity operations use generic responses and bounded rate controls to reduce account enumeration, credential attacks, token abuse, and resource exhaustion.

## Model

The Initial MVP sign-in policy locks an account after five consecutive failed attempts for 15 minutes. A successful authentication resets the failure count.

Public sign-in behavior normally uses `invalid_credentials` for unknown accounts, incorrect passwords, non-disclosable account state, and lockout. Recovery and registration use equivalent accepted result shapes for existing and non-existing addresses.

## Invariants

- Public behavior does not reveal whether an unknown email is registered.
- Lockout does not become an account-discovery endpoint.
- Rate limits use independent, purpose-specific dimensions.
- Expired limiter entries are cleaned with bounded work.
- Credential, token, and provider details are absent from public results.
- Unknown future error codes remain ordinary strings that consumers handle safely.

## Failure conditions

Rate limiting can affect registration, verification reminders, recovery, sign-in, token consumption, profile mutation, and onboarding according to the operation's policy. A limit response must not expose protected account state.

## Consumer responsibilities

Apply appropriate request-size limits, CSRF protection, HTTPS, secure secret handling, and UI throttling. Do not replace framework enforcement with client-side controls or vary public messages based on database lookup results.

## Implementation status

WS-004 verifies exact and concurrent lockout behavior, limiter boundaries, independent dimensions, rollover, real-capacity behavior, and bounded cleanup through hosted and focused tests.

## Related tasks

- [Register an account](account-registration.md)
- [Sign in with a password](password-sign-in.md)
- [Identity security considerations](security-considerations.md)
