---
title: Reference application architecture
description: Understand the supported Helium modular-monolith topology and the responsibilities of the application host, framework modules, and external systems.
uid: fundamentals-reference-architecture
content_type: concept
area: architecture
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/architecture/decisions/application-architecture.md
  - docs/architecture/technical-architecture.md
---

# Reference application architecture

The Helium Initial MVP targets one package-based modular monolith: a consumer-owned ASP.NET Core application composes Helium and product-specific modules in one process and deployable unit.

## Model

```text
Browser or client
        |
TLS termination or reverse proxy
        |
Consumer-owned ASP.NET Core application
        |
        +-- Helium hosting and runtime
        +-- Identity and onboarding
        +-- Organizations and authorization
        +-- Billing and entitlements
        +-- Transactional communications
        +-- Durable processing
        +-- Reference presentation
        +-- Consumer product modules
        |
External PostgreSQL
```

Stripe and a transactional-email provider are external integrations. Logging, monitoring, backup, recovery, and infrastructure remain consumer responsibilities.

## Architectural boundaries

Capability modules own domain state and invariants. Technical subsystems provide hosting, persistence, processing, presentation, and observability. Executing in one process does not permit one module to mutate another module's state directly.

The Initial MVP does not require independently deployed framework services, a distributed event bus, dynamic plugin loading, a mandatory cache cluster, or a proprietary Helium control plane.

## Invariants

- Each authoritative state category has one owning capability.
- Cross-module behavior uses explicit contracts.
- Security-sensitive checks use current authoritative state.
- Presentation does not own business invariants.
- Provider SDK types stay inside provider adapters.
- Consumer product state remains outside Helium-owned persistence.
- Official artifacts use coordinated versions.

## Failure conditions

Architecture-level failures include circular dependencies, hidden global registration, direct table integration, copied framework source, request-time provider checks for authorization, or product code depending on internal assemblies.

## Security implications

One process is not one trust boundary. Organization context, authorization, persistence scoping, provider authenticity, secret handling, and durable-work diagnostics require separate controls even when all modules run together.

## Implementation status

The repository contains the solution and package graph, public-contract controls, PostgreSQL persistence and migrations, durable processing, and identity/onboarding implementation. Organizations and authorization are in progress. Billing, entitlements, reference presentation, project templates, deployment validation, and release publication are not complete.

## Related tasks

- [Supported application model](../overview/supported-application-model.md)
- [Application composition](application-composition.md)
- [Framework and consumer data ownership](data-ownership.md)
