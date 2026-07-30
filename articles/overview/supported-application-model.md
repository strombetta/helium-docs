---
title: Supported application model
description: Understand the single application, PostgreSQL, package, ownership, and deployment model targeted by the Helium Initial MVP.
uid: architecture-supported-application-model
content_type: overview
area: architecture
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/architecture/technical-architecture.md
  - docs/architecture/decisions/application-architecture.md
  - docs/architecture/decisions/package-and-artifact-structure.md
---

# Supported application model

The Helium Initial MVP targets one official reference architecture for newly created SaaS applications. This constraint keeps the application, migration, deployment, compatibility, and support model testable.

> [!IMPORTANT]
> The target model is accepted architecture, but the official project template and end-to-end consumer release are not yet available.

## Application shape

The reference application is a package-based modular monolith with:

- one ASP.NET Core application host;
- one application process for HTTP handling and bounded background work;
- coordinated `Trombetta.SaaS` framework artifacts;
- an external PostgreSQL database;
- Helium-owned persistence and migrations;
- separate consumer-owned product modules and persistence;
- in-process contracts and lifecycle notifications;
- PostgreSQL-backed durable inbox and outbox processing.

A required message broker, distributed cache cluster, proprietary runtime, or Helium-operated control plane is outside the Initial MVP topology.

## Consumer-owned composition

The generated application is intended to contain the consumer-owned composition root, branding, product-domain code, environment configuration examples, and container packaging. It references versioned framework packages and does not contain copied Helium implementation source.

The coordinated meta-package is `Trombetta.SaaS`. Supported consumer contracts are exposed through `Trombetta.SaaS.Contracts`; consumer test support is reserved for `Trombetta.SaaS.Testing`; the future template package is `Trombetta.SaaS.Templates`.

## Persistence model

The target path uses PostgreSQL 18. Helium owns its framework schema and migration stream. Product-specific data remains outside Helium persistence entities and should use a separate consumer-owned persistence boundary.

Applications must not depend on Helium database entities, internal `DbContext` types, Npgsql implementation types, or provider SDK models as public contracts.

## Deployment model

The validated production target is intended to be:

- an OCI-compatible Linux application container;
- a consumer-controlled Linux host;
- external PostgreSQL;
- TLS termination through a reverse proxy or equivalent edge;
- Stripe for Initial MVP billing;
- a transactional-email provider adapter;
- consumer-owned logging, monitoring, backups, and recovery.

## Adoption model

The official Initial MVP adoption path is a newly generated application. Arbitrary module-by-module integration into an existing application is a longer-term direction and is not part of the initial support commitment.

Published implementation packages such as `Trombetta.SaaS.Runtime` or `Trombetta.SaaS.Persistence.PostgreSql` are components of the complete reference composition, not independent general-purpose adoption surfaces.

## Current availability

The solution and package boundaries exist, but `Trombetta.SaaS.Templates` does not yet provide a project template. Reference presentation, complete capability integration, deployment validation, package publication, and release-to-release upgrade evidence also remain pending.

## Next steps

Review [Architecture at a glance](architecture-at-a-glance.md), [Supported versions](supported-versions.md), and [Product scope and current limitations](scope-and-limitations.md).