---
title: Organization lifecycle events
description: Understand the supported organization lifecycle facts, atomic outbox production, at-least-once delivery, and current WS-005 status.
uid: organizations-lifecycle-events
content_type: concept
area: organizations
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/api/public-design.md
  - docs/engineering/organizations-context-and-authorization-specification.md
  - docs/architecture/decisions/public-lifecycle-extension-points.md
---

# Organization lifecycle events

Helium defines committed post-transaction facts for material organization transitions. Consumer handlers run after commit with at-least-once delivery.

> [!WARNING]
> `OrganizationCreated` is produced by the implemented onboarding foundation. Membership-change, ownership-transfer, invitation communication, cache invalidation, and complete WS-005 reaction readiness remain in progress.

## Supported facts

- `OrganizationCreated` after successful first-organization onboarding.
- `OrganizationMembershipChanged` after invitation acceptance, role change, or member removal.
- `OrganizationOwnershipTransferred` after successful ownership transfer.

Event identity remains stable across retries and duplicate delivery. Payloads contain approved public identifiers and values, not persistence entities, tokens, cookie state, provider SDK objects, or internal authorization details.

## Transaction boundary

Authoritative organization state and required outbox work commit atomically. Rolled-back transitions create no executable lifecycle or communication work. Consumer handler failure cannot roll back committed framework state.

## Handler responsibilities

Consumer handlers use independent consumer-owned transactions, tolerate duplicate delivery, use event identity for idempotency, and avoid treating delivery order as globally guaranteed.

## Related tasks

- [Lifecycle events](../fundamentals/lifecycle-events.md)
- [Durable processing](../fundamentals/durable-processing.md)
