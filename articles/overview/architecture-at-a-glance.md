---
title: Architecture at a glance
description: Understand the Helium modular-monolith topology, package boundaries, data ownership, durable processing, and operational responsibilities.
uid: architecture-at-a-glance
content_type: concept
area: architecture
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/architecture/technical-architecture.md
  - docs/architecture/decisions/application-architecture.md
  - docs/architecture/decisions/persistence-and-migrations.md
---

# Architecture at a glance

Helium targets a package-based modular monolith deployed as one ASP.NET Core application with external PostgreSQL. Logical capability boundaries remain explicit even though the Initial MVP is deployed as one process.

## Model

```text
Browser or client
        |
TLS termination or reverse proxy
        |
Consumer-owned ASP.NET Core application
        |
        +-- Helium runtime and hosting
        +-- Identity and onboarding
        +-- Organizations and authorization
        +-- Billing and entitlements
        +-- Transactional communications
        +-- Durable background processing
        +-- Reference presentation
        +-- Consumer product modules
        |
External PostgreSQL
        |
        +-- Helium-owned schema and migrations
        +-- Consumer-owned product persistence
```

Stripe and the transactional-email provider are external integrations. Consumer logging and monitoring systems receive operational signals from the application.

## Component boundaries

The official package composition separates:

- supported public contracts;
- the coordinated consumer meta-package;
- ASP.NET Core hosting integration;
- PostgreSQL persistence and migrations;
- reference Razor presentation;
- internal capability assemblies;
- consumer testing support;
- project-template tooling.

Internal implementation assemblies are not supported consumer extension surfaces merely because a type is technically public.

## Data ownership

Helium owns framework state such as accounts, organizations, memberships, framework authorization data, normalized subscription state, entitlements, durable work, and framework migrations.

The consuming application owns product-specific domain data and its migration stream. Product modules should cross the framework boundary through stable scalar identifiers, value objects, and public contracts rather than through Helium persistence entities.

## Lifecycle and durable work

Local framework state changes commit before external side effects are performed. Provider work uses PostgreSQL-backed durable records, retry behavior, leasing, deduplication, and failure states.

The Initial MVP does not require a message broker. Wake-up signals are optimizations; durable database state remains authoritative.

## Invariants

The architecture is designed around these invariants:

- organization-scoped operations require validated organization context;
- authentication alone does not grant organization access;
- server-side authorization protects outcomes;
- billing-provider objects do not become authorization contracts;
- entitlements use normalized local state rather than request-time Stripe calls;
- framework and product persistence ownership remain separate;
- framework artifacts participate in one coordinated release train.

## Security implications

The principal architecture risks are cross-organization data exposure, invalid authorization composition, forged or duplicate provider events, secret disclosure, migration failures, and accidental dependency on unsupported internals.

Security controls must therefore exist at request, application-service, data-access, provider-boundary, and operational-diagnostics layers.

## Current implementation state

The repository contains the solution and package graph, public-contract compatibility controls, PostgreSQL persistence and migration foundations, durable processing, and identity/onboarding implementation. Organizations and authorization are still in progress, while several later capability and release workstreams remain pending.

## Related tasks

- [Supported application model](supported-application-model.md)
- [Packages and modules](../fundamentals/packages-and-modules.md)
- [Data ownership](../fundamentals/data-ownership.md)
- [Deploy and operate](../operate/index.md)