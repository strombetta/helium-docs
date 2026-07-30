---
title: Operation results and errors
description: Understand the provider-neutral result, error, correlation, field-validation, retryability, and exception conventions used by Helium APIs.
uid: fundamentals-operation-results-errors
content_type: concept
area: api
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/api/public-design.md
  - docs/engineering/ws-004-readiness.md
---

# Operation results and errors

Expected application failures are returned as provider-neutral operation results. Exceptions are reserved for cancellation, programming defects, violated framework preconditions, or unexpected infrastructure failure before a safe result can be produced.

## Result model

A result communicates:

- whether the operation succeeded;
- an immutable value for successful generic operations;
- one safe operation error for expected failure;
- a correlation identifier in every outcome.

A successful result has no error. A failed result has no value. Sensitive details and raw exceptions are excluded.

## Error model

An operation error contains:

- a stable code;
- a category;
- a safe message;
- retryability guidance;
- bounded field errors where validation applies.

Known categories include validation, authentication, authorization, not found, conflict, concurrency, configuration, dependency, rate limit, and indeterminate. Consumers must handle unknown future category values safely.

## Retryability

| Value | Meaning |
| --- | --- |
| `Never` | Repeating the same request is not expected to succeed. |
| `SafeAfterDelay` | Retry may succeed after a bounded delay. |
| `AfterStateRefresh` | Refresh authoritative state before retrying. |
| `Indeterminate` | Reconcile the outcome before repeating an operation that may already have taken effect. |

Cancellation is not an operation error and remains `OperationCanceledException`.

## Error disclosure

Unknown credentials use a generic result. Inaccessible cross-organization resources must be externally indistinguishable from absent resources when distinction would disclose protected information.

Field errors identify safe input problems; they must not include passwords, tokens, provider secrets, internal table names, query text, or stack information.

## Optimistic concurrency

Mutable public resources use an opaque version token. Consumers pass the last observed token and replace it with the returned token after success. Tokens have equality semantics only and must not be parsed, ordered, or synthesized.

## Failure conditions

Application code should not catch provider or persistence exceptions and infer business meaning. Expected provider and storage outcomes must be translated into controlled errors or durable failure categories by the owning framework boundary.

## Implementation status

Common result conventions and identity/onboarding error behavior are implemented and exercised through hosted and PostgreSQL-backed tests. Later capability catalogs will add stable codes without changing the common model.

## Related tasks

- [Public contracts and internal implementation](public-contracts.md)
- [Troubleshooting](../troubleshooting/index.md)
- [Reference](../../reference/index.md)
