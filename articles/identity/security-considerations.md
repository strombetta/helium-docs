---
title: Identity security considerations
description: Apply the security boundaries required for Helium credentials, tokens, sessions, errors, logs, and account context.
uid: identity-security-considerations
content_type: reference
area: security
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/identity-and-onboarding-specification.md
  - docs/engineering/ws-004-readiness.md
  - docs/api/public-design.md
---

# Identity security considerations

Use this checklist when exposing Helium identity operations through application endpoints or UI.

## Credentials and tokens

- Accept credentials only over HTTPS.
- Never log passwords, verification tokens, reset tokens, cookie contents, protected payloads, or stored hashes.
- Treat token strings as opaque and purpose-specific.
- Do not parse, inspect, persist, or compare token internals in consumer code.
- Keep sensitive commands out of automatic request and object logging.

## Enumeration resistance

- Preserve the equivalent accepted shapes for registration and recovery.
- Preserve `invalid_credentials` for non-disclosable sign-in states.
- Do not add account-existence flags, delivery-status details, or provider errors to public responses.
- Return safe field errors and retain the operation correlation identifier.

## Session security

- Use the framework hosting and cookie pipeline.
- Do not create or validate framework session cookies manually.
- Revalidate server-side account and session state for protected requests.
- Treat cached UI state as non-authoritative.
- Require current organization context and policy evaluation separately from authentication.

## Request protection

- Apply CSRF protection to cookie-authenticated mutations.
- Enforce request-size and content-type limits.
- Use framework and application abuse controls together.
- Keep redirect targets local or explicitly allowlisted.
- Avoid reflecting submitted identity values in unrestricted diagnostics.

## Data and diagnostics

- Store consumer product data separately from framework identity persistence.
- Use stable account identifiers at supported boundaries.
- Redact email addresses where they are not required operationally.
- Bound log dimensions and exception text.
- Restrict operator diagnostics by role and environment.

## Verification evidence

The WS-004 readiness suite covers token replay and races, cookie forgery and replay, lockout, rate controls, session expiry and renewal, rollback, provider failure classification, and redaction across public results and generated diagnostics.

## Related documentation

- [Account lockout and abuse resistance](lockout-and-abuse-resistance.md)
- [Authentication sessions](authentication-sessions.md)
- [Security](../security/index.md)
