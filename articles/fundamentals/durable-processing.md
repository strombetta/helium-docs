---
title: Durable processing
description: Understand PostgreSQL-backed inbox, outbox, leases, retries, deduplication, terminal failure, and at-least-once execution in Helium.
uid: fundamentals-durable-processing
content_type: concept
area: durable-processing
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/ws-003-readiness.md
  - docs/architecture/decisions/persistence-and-migrations.md
---

# Durable processing

Helium uses PostgreSQL-backed durable records for external side effects, lifecycle handlers, provider events, and other work that must survive process failure. The database record is authoritative; in-memory wake-up signals are only optimizations.

## Model

- **Outbox work** records an effect requested by committed local framework state.
- **Inbox work** records accepted external input and deduplicates repeated delivery.
- **Leasing** grants bounded ownership of work to one worker attempt.
- **Retry state** records the next eligible attempt after transient failure.
- **Terminal state** preserves work that cannot complete automatically.

## Transaction boundary

Framework state and required outbox work share one authoritative local commit. If the transaction rolls back, neither state nor work becomes visible. External provider calls and consumer handler transactions occur after commit.

## Delivery semantics

Execution is at least once. Duplicate provider delivery, process interruption, lease expiry, and retry can cause repeated invocation. Work handlers must use stable identities and idempotent behavior where side effects may already have occurred.

No global ordering guarantee exists across work categories, accounts, organizations, handlers, or processes.

## Retry and failure

Expected outcomes are classified as complete, retryable, terminal, or indeterminate. Retry is bounded. An indeterminate external outcome requires reconciliation when repeating the operation could duplicate a side effect.

Terminal failure remains durable and operationally visible; it must not be silently discarded or represented as success.

## Invariants

- Work is appended inside the transaction that creates the authoritative state transition.
- One logical work item retains stable identifiers across transaction retry and execution retry.
- Lease ownership is fenced so stale workers cannot commit later transitions.
- Inbox deduplication distinguishes equivalent duplicates from conflicting duplicates.
- Worker shutdown is bounded and does not erase durable state.

## Failure conditions

Relevant failures include dependency unavailability, rate limits, renderer or handler defects, lease loss, process termination, uncertain provider outcome, incompatible payload, and exhausted retry policy.

## Security implications

Durable payloads, logs, and inspection output must not expose credentials, raw tokens, cookies, provider secrets, or unrestricted exception text. Operational identities are not consumer authorization contracts.

## Implementation status

WS-003 is complete. Canonical validation demonstrates atomic state/outbox behavior, inbox deduplication, leasing, retry and terminal transitions, clean and upgrade migrations, compatibility checks, and PostgreSQL 18 execution. Multi-replica production certification is not claimed.

## Related tasks

- [Lifecycle events](lifecycle-events.md)
- [Persistence and migrations](../persistence/index.md)
- [Durable processing operations](../durable-processing/index.md)
