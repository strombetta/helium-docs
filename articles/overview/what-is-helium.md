---
title: What is Helium?
description: Understand the Helium product direction, the target SaaS capabilities, the framework dependency model, and current preview availability.
uid: product-what-is-helium
content_type: overview
area: product
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/product/definition.md
  - docs/product/requirements.md
  - docs/planning/implementation-plan.md
---

# What is Helium?

Helium is the code name for a modular, self-hosted, versioned, and extensible SaaS application framework for .NET. Its stable technical identity is `Trombetta.SaaS`.

> [!IMPORTANT]
> Helium is currently a development preview. The repository contains implemented framework foundations and capability work, but no supported consumer release or official application template has been published.

## What Helium is designed to provide

The target Initial MVP brings recurring SaaS concerns into one coordinated framework:

- account registration, verification, authentication, sessions, and recovery;
- first-organization onboarding;
- organizations, memberships, invitations, roles, and ownership;
- validated organization context and server-side authorization;
- Stripe subscription billing and normalized local subscription state;
- plan-based entitlements;
- transactional email and durable provider processing;
- persistence, migrations, health information, diagnostics, and deployment guidance;
- public contracts, testing support, and documented extension points.

These capabilities use shared concepts and lifecycle rules. Authentication identifies an account; membership grants access to an organization; roles authorize organization operations; subscription state and entitlements determine product access.

## How Helium fits into an application

The Initial MVP is a package-based modular monolith. A consuming application is expected to reference coordinated `Trombetta.SaaS` artifacts rather than copy framework implementation source.

The application remains consumer-owned. Product modules, product data, configuration, secrets, infrastructure, monitoring, backups, and recovery remain the responsibility of the organization operating the application.

Helium owns the common framework implementation, its public contracts, framework persistence, migrations, and supported upgrade path. Product-specific code depends on documented contracts rather than internal entities or provider SDK models.

## Current availability

As of July 30, 2026, engineering foundations, public contracts, PostgreSQL persistence and durable processing, and identity/onboarding workstreams are recorded as complete. Organizations and authorization are in progress. Billing, entitlements, transactional email, reference presentation, project templates, deployment validation, and release publication remain incomplete.

The `Trombetta.SaaS.Templates` project currently reserves the future tooling artifact boundary; it does not yet contain a usable `dotnet new` template.

## When to consider Helium

Helium is intended for teams that:

- are building a new SaaS application with .NET;
- want one integrated model for common SaaS capabilities;
- accept the official reference architecture for the initial adoption path;
- need to retain control of infrastructure, deployment, integrations, and data;
- prefer a maintained framework dependency over copied starter code;
- are prepared to operate a self-hosted application.

## Limitations

The Initial MVP does not target arbitrary integration into existing architectures, multiple database engines, multiple billing providers, Kubernetes, high-availability multi-replica deployment, or a general public HTTP API.

Current preview limitations are broader because the official template, complete capability set, validated deployment path, published packages, and release compatibility evidence are not yet available.

## Next steps

Read [Why use Helium?](why-use-helium.md), review the [supported application model](supported-application-model.md), and check the [product scope and current limitations](scope-and-limitations.md).