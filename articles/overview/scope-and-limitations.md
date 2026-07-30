---
title: Product scope and current limitations
description: Review the Helium Initial MVP capability boundary, excluded scenarios, consumer responsibilities, and limitations of the current preview.
uid: product-scope-and-limitations
content_type: overview
area: product
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/product/requirements.md
  - docs/architecture/technical-architecture.md
  - docs/planning/implementation-plan.md
---

# Product scope and current limitations

The Helium Initial MVP is intentionally constrained to one complete and supportable reference path. The current preview is narrower because several required workstreams and the release pipeline are not complete.

## Target Initial MVP scope

The target release includes:

- a generated ASP.NET Core SaaS application;
- account registration, verification, authentication, sessions, and recovery;
- first-organization onboarding;
- organizations, memberships, invitations, fixed roles, and ownership rules;
- validated active-organization context and server-side authorization;
- Stripe-hosted recurring subscription workflows;
- normalized local subscription state and plan entitlements;
- transactional email through a replaceable provider contract;
- personal and organization settings;
- PostgreSQL persistence, migrations, and durable work;
- health, diagnostics, container deployment guidance, and upgrade documentation.

## Current preview limitations

As of July 30, 2026:

- no supported consumer package release is published;
- no usable `dotnet new` template is available;
- organizations and authorization are still in progress;
- billing, entitlements, transactional email, reference UI, settings, deployment validation, and release publication are incomplete;
- the end-to-end local application tutorial cannot yet be executed;
- no production support or compatibility commitment applies to repository build output.

## Scenarios outside the Initial MVP

| Scenario | Initial MVP position |
| --- | --- |
| Add individual Helium modules to an arbitrary existing application | Not supported |
| Use a runtime other than .NET 10 | Not supported |
| Use a database other than PostgreSQL 18 | Not supported |
| Use a billing provider other than Stripe | Not supported |
| Deploy independent Helium microservices | Not supported |
| Require Kubernetes or official infrastructure-as-code modules | Not provided |
| Run multiple application replicas as an officially validated topology | Not provided |
| Expose a general public HTTP API from Helium | Not required |
| Configure arbitrary custom organization roles | Not required |
| Support account or organization deletion workflows | Not required |
| Provide advanced identity mechanisms such as enterprise federation | Not required |

`Not required` means the scenario is outside the Initial MVP commitment; it must not be assumed to work or to receive compatibility coverage.

## Consumer responsibilities

Even after release, consumers remain responsible for:

- product-specific code and data;
- infrastructure and deployment;
- configuration and secret management;
- external provider accounts and credentials;
- TLS termination and network controls;
- monitoring and incident response;
- PostgreSQL operations, backups, and recovery;
- testing their product modules against framework upgrades.

## Framework boundaries

Consumers must use documented public contracts and supported composition paths. Internal assemblies, persistence entities, provider SDK types, undocumented namespaces, and arbitrary partial package combinations are not supported extension surfaces.

## When to defer adoption

Defer production adoption until Helium publishes coordinated packages, the official project template, release compatibility metadata, deployment validation, migration guidance, and known limitations for a concrete release.

## Next steps

Review [Supported versions](supported-versions.md) and [Get started](../getting-started/index.md).