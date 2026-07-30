---
title: Transactional onboarding
description: Understand the atomic first-organization transaction, concurrency behavior, post-commit lifecycle work, and rollback guarantees.
uid: onboarding-transactional-behavior
content_type: concept
area: onboarding
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/identity-and-onboarding-specification.md
  - docs/engineering/ws-004-readiness.md
  - docs/architecture/decisions/persistence-and-migrations.md
---

# Transactional onboarding

First-organization onboarding is one coordinated framework transaction. It is designed to prevent an externally visible organization without its initial Owner and to preserve one coherent winner under concurrent requests.

## Model

A successful transition atomically persists:

1. the organization;
2. the authenticated account's Owner membership;
3. the server-side active-organization preference;
4. the durable `OrganizationCreated` lifecycle work;
5. the framework state that prevents repeated first-organization creation.

External lifecycle handlers run after commit.

## Transaction boundary

Framework-owned onboarding state shares the internal framework transaction. Consumer-owned data does not participate automatically. A consumer lifecycle handler uses its own transaction after the framework commit and must tolerate at-least-once delivery.

## Invariants

- No organization is externally observable without its initial Owner.
- Failure before commit leaves none of the onboarding aggregate visible.
- A complete transaction retry preserves stable organization, membership, event, and work identities.
- Concurrent attempts create at most one first organization for the account.
- Handler failure cannot roll back committed onboarding.
- Consumers do not mutate onboarding tables or coordinate the internal transaction.

## Failure conditions

Validated rollback points include eligibility, organization creation, membership creation, active preference, lifecycle append, and commit. Dependency failure after commit affects post-commit work, not the authoritative onboarding result.

## Security implications

The acting account comes from authoritative authenticated account context. Organization name input cannot select another account, fabricate an Owner, or establish authority outside the committed membership.

## Related tasks

- [Create the first organization](first-organization.md)
- [Lifecycle events](../fundamentals/lifecycle-events.md)
- [Durable processing](../fundamentals/durable-processing.md)
