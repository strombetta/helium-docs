---
title: Framework and consumer data ownership
description: Understand which state, schemas, migrations, transactions, and operational responsibilities belong to Helium and which belong to the consuming application.
uid: fundamentals-data-ownership
content_type: concept
area: persistence
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/architecture/decisions/application-architecture.md
  - docs/architecture/decisions/persistence-and-migrations.md
---

# Framework and consumer data ownership

Helium and the consuming application share one runtime composition but retain separate ownership of state, persistence models, migrations, and operational responsibilities.

## Helium-owned state

Helium owns framework capabilities and their persistence, including account authentication, onboarding, organizations, memberships, framework roles, authorization mechanisms, normalized subscription state, entitlements, transactional communications, durable work, framework contracts, and framework migrations.

Framework state uses one internal EF Core context and one coordinated migration stream in a dedicated configurable PostgreSQL schema. The default schema name is `trombetta_saas`.

## Consumer-owned state

The consuming application owns product-specific entities, workflows, policies, routes, UI, persistence contexts, migration streams, infrastructure, deployment configuration, backups, recovery, monitoring, and integrations not owned by Helium.

Consumer product tables must use a separate schema or database. Sharing the same physical PostgreSQL database does not create a shared persistence model or transaction contract.

## Boundary model

Consumer records may persist stable scalar Helium identifiers such as account or organization UUID values. They must not use foreign keys to internal framework entities as a supported integration contract, directly mutate framework tables, or add consumer entities to the internal framework context.

Helium does not automatically participate in consumer transactions. Consumer lifecycle handlers use consumer-owned transactions and must tolerate at-least-once delivery.

## Migration ownership

Framework migrations are compiled, ordered, forward-only release artifacts. Consumers do not scaffold, copy, edit, reorder, or regenerate them. Consumer migrations remain independent and must not alter framework-owned objects.

Normal application startup validates compatibility but does not apply pending framework migrations implicitly.

## Invariants

- One module owns each authoritative framework state category.
- Consumer code depends on supported contracts, not persistence entities.
- Framework and consumer migration histories remain separate.
- Consumer data does not enter the framework migration stream.
- Framework data changes do not call consumer services or external providers from migrations.
- Schema configuration is static for one application instance.

## Failure conditions

Unsupported states include direct SQL integration with framework tables, consumer triggers or row-level-security policies on framework objects, shared tracked entities, implicit cross-boundary transactions, edited released migrations, or a runtime serving against an incompatible schema.

## Security implications

Separation limits accidental privilege expansion and cross-organization leakage. Production environments should use distinct schema ownership, migration, and runtime privileges and avoid granting ordinary runtime credentials DDL authority.

## Implementation status

The framework context, configurable schema, migration catalog, explicit migration host, compatibility inspection, least-privilege validation, transaction coordination, and PostgreSQL 18 tests are implemented. Consumer deployment and migration runbooks remain future documentation work.

## Related tasks

- [Reference application architecture](reference-architecture.md)
- [Durable processing](durable-processing.md)
- [Persistence](../persistence/index.md)
