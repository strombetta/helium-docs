---
title: Identity lifecycle events
description: React to the supported AccountVerified post-commit lifecycle event with an idempotent consumer handler.
uid: identity-lifecycle-events
content_type: concept
area: identity
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/api/public-design.md
  - docs/engineering/ws-004-readiness.md
  - src/Trombetta.SaaS.Contracts/Lifecycle/AccountVerified.cs
---

# Identity lifecycle events

The public identity lifecycle surface contains the version 1 `AccountVerified` event. Consumers can register post-commit handlers; they cannot publish authoritative framework lifecycle events.

## Model

The event is delivered in a `LifecycleEventEnvelope<AccountVerified>` containing stable event metadata and the verified account identifier and instant.

Register a handler explicitly through the Helium builder:

```csharp
builder.AddLifecycleEventHandler<
    AccountVerified,
    AccountVerifiedHandler>();
```

Handlers are scoped, consumer-implemented, and invoked by the framework after authoritative state commits.

## Delivery semantics

Delivery is durable and at least once. The same `EventId` is retained across retries of one lifecycle fact. A handler may run more than once and must make its consumer-owned effects idempotent.

Handler failure cannot roll back email verification. Each handler owns its transaction for consumer data, and Helium does not provide automatic atomicity between framework and consumer persistence.

## Invariants

- Consumers cannot publish or fabricate authoritative events.
- Payloads contain provider-neutral public values.
- Passwords, tokens, cookies, and provider data are excluded.
- No global ordering is guaranteed.
- Event version and type are compatibility-sensitive.
- One failing handler must not permanently block independent handlers.

## Failure conditions

Transient handler failures are eligible for bounded retry. Exhausted or terminal failures remain operationally observable. Consumers must not reconstruct critical current account state solely from event arrival order.

## Related tasks

- [Verify an email address](email-verification.md)
- [Lifecycle events](../fundamentals/lifecycle-events.md)
- [Durable processing](../fundamentals/durable-processing.md)
