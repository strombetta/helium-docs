---
title: Accounts and authenticated account context
description: Understand account lifecycle, server sessions, and the authoritative request-scoped account context used by Helium operations.
uid: fundamentals-account-context
content_type: concept
area: identity
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/ws-004-readiness.md
  - docs/api/public-design.md
---

# Accounts and authenticated account context

Identity owns account authentication state. It verifies who is signed in, but it does not independently grant access to an organization or product capability.

## Account model

The implemented preview supports registration, profile access, email verification, password sign-in, persistent and ordinary server sessions, sign-out, recovery, reset, password change, and first-organization onboarding.

Account identifiers are stable UUID-backed values. Email, credential, token, and session persistence remain internal implementation details.

## Authenticated account context

Request processing uses an authoritative immutable account context resolved from current account and session state. It is not reconstructed from arbitrary claims, route values, email input, or consumer code.

A valid context represents the current authenticated account only. It does not contain organization membership, role, billing authority, or entitlement access.

## Session behavior

Ordinary and persistent sessions have bounded idle and absolute lifetimes. Sliding renewal cannot exceed the absolute lifetime. Sign-out revokes the current session, and password reset or security invalidation revokes existing sessions.

## Invariants

- Registration normalization does not create duplicate equivalent accounts.
- Verification and recovery tokens are purpose-specific, single-use, and time-bounded.
- Password reset and change preserve credential and session consistency.
- Account context is derived from authoritative state on each protected request.
- Authentication does not imply organization authorization.

## Failure conditions

Expected states include unauthenticated access, invalid or expired token, generic invalid credentials, lockout, revoked or stale session, unverified account, rate limiting, and temporary dependency failure.

## Security implications

Public results avoid account enumeration. Passwords, token values, cookie contents, stored hashes, connection secrets, and unrestricted exception details must not appear in results, lifecycle payloads, logs, or telemetry.

## Implementation status

Identity, sessions, account context, first-organization onboarding, durable identity email, and lifecycle producers have passed the WS-004 readiness review against the PostgreSQL-backed hosted path.

## Related tasks

- [Organizations and tenant context](organizations-and-tenant-context.md)
- [Operation results and errors](operation-results-and-errors.md)
- [Identity and accounts](../identity/index.md)
