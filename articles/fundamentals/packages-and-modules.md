---
title: Packages and modules
description: Distinguish Helium distribution artifacts, logical capability modules, supported public packages, and repository-internal assemblies.
uid: fundamentals-packages-modules
content_type: concept
area: architecture
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/architecture/decisions/package-and-artifact-structure.md
  - docs/engineering/project-structure.md
---

# Packages and modules

Helium uses packages to distribute a coordinated framework and modules to express ownership and dependency boundaries. A logical module does not automatically require an independent NuGet package.

## Artifact classes

| Class | Examples | Consumer relationship |
| --- | --- | --- |
| Supported public artifacts | `Trombetta.SaaS`, `Trombetta.SaaS.Contracts`, `Trombetta.SaaS.Testing`, `Trombetta.SaaS.Templates` | Intended for documented consumer use when released. |
| Supported implementation artifacts | `Trombetta.SaaS.Runtime`, `Trombetta.SaaS.Hosting.AspNetCore`, `Trombetta.SaaS.Persistence.PostgreSql`, `Trombetta.SaaS.Presentation.Razor` | Supported as parts of the complete reference composition, not arbitrary standalone adoption surfaces. |
| Repository-internal artifacts | Identity, Organizations, Billing, Communications, and shared Infrastructure assemblies | Implementation details; not supported consumer dependencies. |

## Logical modules

Logical capability boundaries include Identity, Organizations, Authorization, Billing, Entitlements, Communications, and Settings. Technical subsystem boundaries include Hosting, Persistence, Durable Processing, Observability, and Presentation.

The package graph is deliberately smaller than the logical model. This avoids a package for every capability and prevents an unbounded compatibility matrix.

## Supported dependency rule

Consumer code should depend on documented public artifacts and namespaces. Publication of an implementation package or the technical visibility of a CLR type does not make that type a supported contract.

## Invariants

- Official artifacts use one coordinated version.
- The aggregate package is a composition entry point, not a copy of implementation code.
- Internal assemblies remain non-packable or are carried only as implementation details of a supported package.
- Generated applications must not reference repository-internal projects.
- Package restore must not modify consumer code, configuration, or databases.

## Failure conditions

Unsupported states include mixing incompatible artifact versions, referencing internal capability assemblies, inferring package independence from namespace names, or copying migrations and framework source into an application.

## Implementation status

The repository project and package topology is implemented and enforced through architecture, package, and consumer-fixture validation. The future `Trombetta.SaaS.Templates` artifact boundary exists, but no supported project template is available yet.

## Related tasks

- [Public contracts and internal implementation](public-contracts.md)
- [Project template availability](../getting-started/install-template.md)
- [Reference](../../reference/index.md)
