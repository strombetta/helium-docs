---
title: Application composition
description: Understand how a consumer-owned ASP.NET Core host explicitly composes Helium, product modules, middleware, endpoints, persistence, and workers.
uid: fundamentals-application-composition
content_type: concept
area: architecture
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/architecture/decisions/application-architecture.md
  - docs/api/public-design.md
  - docs/engineering/ws-004-readiness.md
---

# Application composition

The consuming application owns one explicit ASP.NET Core composition root. Helium provides registration and hosting contracts, but it does not own the application's complete startup model.

## Composition model

The composition root is responsible for:

- registering Helium services and product modules;
- binding and validating configuration;
- selecting infrastructure adapters;
- configuring authentication and authorization middleware;
- connecting PostgreSQL persistence;
- registering reference or consumer presentation endpoints;
- enabling approved durable workers;
- composing health and observability services;
- coordinating startup and shutdown.

## Hosting sequence

The implemented hosted identity and onboarding path is exercised through the supported registration and pipeline entry points:

```text
AddTrombettaSaaS
UseTrombettaSaaS
MapTrombettaSaaS
```

Exact configuration and endpoint guidance will remain preview until the consumer package and project template are published.

## Explicit composition

Helium does not use a global service locator, hidden static initialization, dynamic plugin loading, or unrestricted scanning of loaded assemblies as the supported model. Bounded discovery may be used internally only when it is deterministic, testable, and part of a documented registration mechanism.

## Invariants

- Underlying framework projects do not depend on the aggregate `Trombetta.SaaS` package.
- Consumer modules depend on supported public contracts, not internal implementation assemblies.
- Capability packages do not silently mutate global application behavior.
- Configuration is validated before protected runtime behavior begins.
- Startup does not implicitly apply framework database migrations.

## Failure conditions

Typical composition failures include missing required configuration, incompatible schema state, invalid middleware ordering, duplicate registrations, unsupported adapter combinations, or mixing artifact versions.

## Security implications

Authentication middleware, account context, organization context, and authorization must be composed in the documented order. A registered service or visible endpoint does not bypass server-side authorization or capability invariants.

## Implementation status

Core composition, hosted identity sessions, account context, PostgreSQL integration, and bounded durable-worker hosting exist in the framework repository. The generated consumer host and full reference presentation are not yet released.

## Related tasks

- [Reference application architecture](reference-architecture.md)
- [Accounts and authenticated account context](accounts-and-account-context.md)
- [Project template availability](../getting-started/install-template.md)
