---
title: Public contracts and internal implementation
description: Identify the supported Helium API boundary and avoid depending on internal modules, persistence entities, provider SDK models, and runtime details.
uid: fundamentals-public-contracts
content_type: concept
area: api
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/api/public-design.md
  - docs/architecture/decisions/package-and-artifact-structure.md
---

# Public contracts and internal implementation

Helium exposes a deliberately small, provider-neutral in-process .NET API. The implementation is larger than the supported consumer surface.

## Supported contract test

A type is part of the supported public API only when it is:

1. declared in a supported public namespace;
2. documented for consumer use or implementation;
3. included in the public API compatibility baseline;
4. intended for direct consumer use, configuration, hosting integration, testing, or extension.

Technical visibility alone is insufficient.

## Contract categories

- **Consumer-used contracts:** Helium implements them and application code calls them.
- **Consumer-implemented contracts:** application code implements them and Helium calls them.
- **Configuration contracts:** startup options and validated settings.
- **Data contracts:** immutable identifiers, commands, results, and snapshots.
- **Hosting integration:** ASP.NET Core registration and request integration.
- **Testing support:** supported fixtures and fakes for consumer tests.

Consumer-implemented interfaces are especially compatibility-sensitive because adding a required member can break every implementation.

## Internal implementation

Unsupported consumer dependencies include EF Core entities and contexts, `IQueryable`, Npgsql types, Stripe or email-provider SDK models, inbox and outbox records, worker identities, internal exceptions, Razor Page models, cryptographic token formats, and internal diagnostic payloads.

## Invariants

- Public contracts are immutable and provider-neutral.
- Organization-scoped operations receive explicit organization identity.
- Public identifiers have no embedded meaning or ordering.
- Version tokens and cursors are opaque.
- Expected failures use operation results rather than provider exceptions.
- Public APIs do not expose persistence transactions or tracked entities.

## Failure conditions

A consumer leaves the supported boundary when it references an internal assembly, parses an opaque token, depends on internal routes or DOM structure, directly accesses framework tables, or assumes every public CLR type is versioned for consumer use.

## Security implications

The narrow boundary prevents persistence, provider, credential, and diagnostic details from leaking into product code. It also ensures that authentication claims, provider objects, and UI visibility do not become authorization contracts.

## Implementation status

Public artifact and namespace inventories, API baselines, architecture tests, package validation, and an isolated consumer fixture are implemented. Capability-specific contracts continue to become executable as their workstreams complete.

## Related tasks

- [.NET API](../../api/index.md)
- [Operation results and errors](operation-results-and-errors.md)
- [Extend and customize](../extensibility/index.md)
