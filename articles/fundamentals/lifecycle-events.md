---
title: Lifecycle events
description: Understand supported post-commit lifecycle facts, handler registration, at-least-once delivery, event versioning, and consumer transaction boundaries.
uid: fundamentals-lifecycle-events
content_type: concept
area: architecture
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/api/public-design.md
  - docs/engineering/ws-004-readiness.md
  - docs/engineering/ws-003-readiness.md
---

# Lifecycle events

Lifecycle events notify consumer code after authoritative framework state has committed. They are reactions to facts, not commands and not an alternative authorization or transaction mechanism.

## Supported catalog

The Initial MVP public catalog is closed and starts with version `1` payloads for:

- `AccountVerified`;
- `OrganizationCreated`;
- `OrganizationMembershipChanged`;
- `OrganizationOwnershipTransferred`;
- `OrganizationSubscriptionChanged`;
- `OrganizationEntitlementsChanged`.

The payload type name is the stable, ordinal, case-sensitive event identity. Consumers cannot publish framework lifecycle events directly.

## Envelope and handlers

Each immutable envelope contains an event ID, event type and version, UTC occurrence time, correlation and optional causation identifiers, optional subject identifiers, and a provider-neutral payload.

Consumer handlers implement a typed lifecycle interface and are registered explicitly through the Helium builder. Registration is deterministic and does not use unrestricted assembly scanning.

## Delivery semantics

- Authoritative state and lifecycle delivery intent commit atomically.
- Handlers run after commit in independent dependency-injection scopes.
- Delivery is durable and at least once.
- The same event ID is preserved across retries.
- Duplicate invocation is possible.
- One failing handler must not permanently block independent handlers.
- No global ordering is guaranteed.

## Consumer transaction boundary

A handler may use a consumer-owned transaction for consumer-owned data. Helium does not provide automatic atomicity between framework state and consumer state. Handlers must therefore be idempotent and tolerate replay.

## Invariants

Payloads use stable identifiers and provider-neutral values. They exclude EF Core entities, provider SDK models, tokens, cookies, claims, outbox records, worker internals, and mutable state graphs.

## Failure conditions

Transient handler failures are eligible for bounded retry. Terminal failures remain operationally observable. Handler failure cannot roll back committed framework state.

## Security implications

Subject identifiers and correlation data are not authorization grants. A handler must re-evaluate current authority when its action requires current state rather than relying only on an event that may be delayed or replayed.

## Implementation status

Lifecycle contracts, registration, durable execution infrastructure, and identity/onboarding producers for `AccountVerified` and `OrganizationCreated` are implemented. Organization administration, billing, and entitlement producers depend on incomplete downstream workstreams.

## Related tasks

- [Durable processing](durable-processing.md)
- [Framework and consumer data ownership](data-ownership.md)
- [Transactional email](../communications/index.md)
