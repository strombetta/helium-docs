# What is Helium?

Helium is a modular, self-hosted, versioned, and extensible framework for building SaaS applications with .NET.

It provides a maintained foundation for the capabilities that most SaaS products need but that rarely make the product unique. Instead of implementing these capabilities from scratch, copying them from a starter repository, or depending on a proprietary hosted platform, a team can use Helium as part of its own application.

Helium is designed for technical founders, software developers, and engineering teams that want to spend more time on product-specific features while retaining control of their application, infrastructure, deployment, integrations, and data.

## A foundation for common SaaS capabilities

A production SaaS application needs more than its main product features. It also needs accounts, organizations, authorization, billing, email, administration, deployment support, and reliable background processing. These areas are closely connected and must use consistent rules and data.

Helium brings those recurring concerns together in one framework. Its capability areas include:

- account registration, email verification, sign-in, sessions, and password recovery;
- onboarding and first-organization creation;
- organizations, memberships, invitations, roles, and ownership;
- organization-scoped authorization and tenant context;
- subscription billing through Stripe;
- plan-based entitlements for controlling product access;
- transactional email for account, invitation, and billing workflows;
- personal and organization settings;
- persistence, migrations, durable background work, health information, and deployment guidance.

These capabilities are designed to work together. For example, organization membership determines which tenant a user can access, authorization determines which operations the user can perform, and subscription entitlements determine which product features the organization can use.

## Helium remains a framework dependency

Helium is not copied into an application as source code. A consuming application references versioned Helium artifacts and remains connected to the framework's release lifecycle.

This model is important after the first release of the application. It allows a team to adopt supported fixes, migrations, compatibility updates, and new framework versions without manually reconciling a large body of locally modified starter code.

Helium provides:

- an official reference architecture for the supported application model;
- versioned framework packages and database migrations;
- default workflows and user interfaces;
- documented configuration options;
- public contracts and supported extension points;
- release and upgrade guidance.

Application-specific functionality stays in the consuming application. It can use Helium's public contracts without depending on internal framework implementation details.

## Self-hosted and under your control

Helium does not run your product for you. You deploy and operate the application in infrastructure that you control.

Your organization retains ownership of:

- the consuming application and its source code;
- product-specific modules and data;
- infrastructure and deployment choices;
- application configuration and secrets;
- third-party integrations;
- operational monitoring, backups, and recovery.

Helium may provide packages, project templates, container images, and deployment instructions, but these are delivery mechanisms for the framework. They do not turn Helium into a proprietary application runtime or hosted SaaS platform.

## Opinionated where consistency matters

Helium defines clear domain rules for the capabilities it manages. For example, organization-scoped operations require a valid organization context, authorization is enforced on the server, and an organization must retain a valid owner.

These opinions provide a coherent and supportable model. They reduce the number of architectural decisions that each application team must make independently and help prevent different capability areas from developing incompatible concepts.

Helium does not, however, control the complete architecture of the consuming product. Product-specific behavior and data can remain outside Helium-owned modules. Supported behavior can be configured or extended through public contracts instead of by changing framework internals.

## Initial supported application model

The initial supported path is for new SaaS applications created from the official Helium reference architecture. The reference model uses a single ASP.NET Core application with an external PostgreSQL database and integrates the Helium capability modules into one deployable application.

The supported production path is self-hosted and container-based. Stripe is the supported billing provider for the initial product scope, and transactional email is connected through a provider adapter.

Progressive integration of individual modules into an existing .NET application is part of Helium's longer-term direction, but it is not the primary initial adoption path. See [Supported application model](supported-application-model.md) and [Product scope and current limitations](scope-and-limitations.md) for the applicable boundaries.

## Who Helium is for

Helium is intended primarily for:

- technical founders creating and validating a SaaS product;
- .NET developers who need a working application foundation;
- engineering teams that expect to maintain and upgrade a product over multiple releases;
- engineering leaders evaluating delivery speed, operational control, and lifecycle cost;
- operators responsible for deploying, monitoring, updating, and recovering the application.

Helium is most relevant when a team wants an integrated SaaS foundation, accepts a supported reference model for common capability domains, and still needs to own and operate the resulting product.

## What Helium is not

Helium is not:

- a one-time boilerplate or copied starter application;
- a proprietary managed SaaS runtime;
- a collection of unrelated low-level libraries that the application must integrate itself;
- a replacement for the .NET ecosystem, ASP.NET Core, or general application architecture;
- a platform that owns the consuming application's infrastructure or data.

## Next steps

Read [Why use Helium?](why-use-helium.md) to understand the problems it addresses and the trade-offs involved. Then review the [Supported application model](supported-application-model.md) before following the [Getting started](../getting-started/index.md) guide.