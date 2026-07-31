---
title: What is Helium?
description: Learn what Helium is, how its SaaS capabilities work together, and how it supports flexible and extensible ASP.NET Core applications.
uid: product-what-is-helium
content_type: overview
area: product
source:
  - docs/product/definition.md
  - docs/product/vision.md
  - docs/architecture/decisions/application-architecture.md
  - docs/architecture/decisions/public-lifecycle-extension-points.md
  - docs/api/public-design.md
---

# What is Helium?

Helium is a flexible, modular, and highly extensible SaaS application framework for ASP.NET Core.

Build and operate production-ready SaaS products on an integrated foundation for identity, tenancy, authorization, billing, entitlements, administration, notifications, auditing, persistence, and operations, while running the resulting application in an environment you control.

Helium provides complete default implementations while exposing stable, provider-neutral contracts that let applications configure, replace, and extend framework behavior without modifying its internal implementation.

## A framework for common SaaS capabilities

Every SaaS application requires more than its product-specific features. It must identify users, establish tenant boundaries, control access, manage subscriptions, determine which capabilities customers can use, communicate with users, and operate reliably.

These concerns are closely related:

- an account represents a user and their identity;
- an organization establishes a boundary for tenancy and collaboration;
- a membership connects an account to an organization;
- roles and policies determine which organization operations are allowed;
- subscriptions record the commercial state associated with an organization;
- entitlements translate plans, commercial state, and authorized assignments into access to product capabilities;
- notifications, audit records, and durable processing support the resulting lifecycle events.

Helium provides these concerns as coordinated modules with shared concepts, invariants, and lifecycle rules. Product teams do not need to design and reconcile a separate model for each capability.

See [Key capabilities](key-capabilities.md) for a detailed description of each capability, its responsibilities, and how it relates to the rest of the framework.

## Flexible and extensible by design

Helium provides opinionated defaults without making those defaults a closed system.

Consuming applications can:

- configure supported module behavior;
- replace external-service providers through provider-neutral contracts;
- react to framework lifecycle events through durable, versioned handlers;
- customize branding, navigation, and supported presentation elements;
- integrate product-specific modules through public application contracts;
- add consumer-owned workflows and data without modifying framework internals;
- select supported application, persistence, and deployment configurations.

Helium separates its public contracts from its internal implementation. Applications depend on stable identifiers, commands, queries, result models, configuration options, provider abstractions, and documented lifecycle events rather than framework entities, database schemas, or vendor SDK models.

Extensibility does not make framework-owned invariants optional. Helium remains opinionated about the domains and security boundaries it manages, while providing explicit extension points around those boundaries.

## Standards-based interoperability

Helium follows established ASP.NET Core application conventions for hosting, dependency injection, configuration, authentication, authorization, health checks, and observability.

Integrations with external systems use documented protocols, formats, and provider-neutral adapters. Provider-specific SDK models remain behind integration boundaries and do not become contracts that product-specific code must adopt.

This approach allows Helium applications to work with the wider .NET and infrastructure ecosystem without requiring a proprietary runtime or coupling the application domain to a particular external provider.

## How Helium fits into an application

Helium runs within an ASP.NET Core application alongside the product-specific functionality implemented by the consuming application.

The application references `Trombetta.SaaS` packages and interacts with Helium through public contracts and supported extension points. Product-specific modules remain separate from the framework’s internal implementation.

Helium can use a database provided by the consuming application or create one for the data it manages, depending on how the framework is configured. Helium manages the persistence model and migrations for the capabilities it owns, while the consuming application determines how its product-specific data is stored.

The organization operating the application chooses where and how it is deployed. The application can run in a public cloud, a private environment, an on-premises data center, or another compatible hosting environment.

Helium does not require a proprietary hosted runtime or a Helium-operated control plane. External services for payments, transactional email, logging, monitoring, and other infrastructure concerns remain integrations selected and configured by the consuming application.

Helium provides an official reference architecture while keeping its capability boundaries explicit. It does not define the application’s product-specific domain or require all application behavior to be implemented inside the framework.

## Who Helium is for

Helium is intended for technical founders, software developers, and engineering teams that:

- build SaaS products with ASP.NET Core;
- want common SaaS capabilities to follow one coherent model;
- need flexible configuration and supported extension points;
- prefer an integrated framework over assembling and coordinating unrelated components;
- want to replace external providers without coupling product code to their SDKs;
- want to run applications in infrastructure they control;
- are prepared to operate the resulting application.

Helium is most appropriate for teams that accept an opinionated model for common SaaS capabilities in exchange for less repeated platform work, controlled extensibility, and a more consistent application foundation.

## Next steps

Explore the [key capabilities](key-capabilities.md), read [Why use Helium?](why-use-helium.md) to understand its benefits and trade-offs, then review the [supported application model](supported-application-model.md) and [product scope and limitations](scope-and-limitations.md).
