---
title: Organization isolation
description: Understand the explicit-scope, fail-closed isolation model for framework-owned organization data and system execution.
uid: organizations-isolation
content_type: concept
area: organizations
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/organizations-context-and-authorization-specification.md
  - docs/architecture/decisions/organization-context-and-authorization.md
---

# Organization isolation

Organization isolation requires authoritative scope at application, persistence, worker, webhook, and maintenance boundaries. A global query filter alone is not sufficient.

> [!WARNING]
> The persistence model includes explicit organization ownership, but complete adversarial isolation verification and every system-execution path remain in progress in WS-005.

## Enforcement model

- Organization-owned records have explicit non-null ownership or an enforceable relational path.
- Internal stores and queries require an explicit `OrganizationId` or validated scope.
- Reads, mutations, deletes, and bulk operations include authoritative organization predicates.
- Protected rows are not loaded globally and filtered in memory.
- Cross-module `IQueryable`, public framework entities, and generic unscoped repositories are unsupported.
- Workers and webhooks resolve scope through verified local relationships rather than provider metadata or arbitrary payload fields.

## Non-disclosure

Foreign and inaccessible identifiers use not-found-equivalent outcomes when distinguishing them would expose protected state. Logs and metrics use bounded categories and avoid protected organization details as dimensions.

## Consumer responsibility

Helium does not automatically isolate consumer-owned tables. Consuming applications must use validated organization context, explicit ownership columns, scoped queries, server-side authorization, and adversarial tests for their own product data.

## Related tasks

- [Framework and consumer data ownership](../fundamentals/data-ownership.md)
- [Authorization model](../authorization/model.md)
