# Why use Helium?

Building a SaaS product involves a large amount of work that is necessary but usually does not differentiate the product. Every team still needs to solve account security, tenant isolation, authorization, billing, entitlements, transactional email, administration, persistence, deployment, and upgrades.

Helium provides these concerns as an integrated and maintained .NET framework. Its purpose is to help teams reach a working SaaS foundation sooner without giving up long-term control or turning the foundation into application-owned code that becomes difficult to update.

## Focus engineering effort on your product

A product team creates value through its domain knowledge, workflows, customer experience, and market-specific features. Rebuilding common SaaS infrastructure delays that work.

Helium supplies supported implementations and workflows for recurring capability areas so that the team can focus more of its engineering capacity on the functionality that makes the product different.

This benefit applies beyond the first prototype. The same common capabilities must be secured, tested, operated, and maintained throughout the life of the application. Using a maintained framework reduces the amount of application-specific platform code that the team must own indefinitely.

## Use capabilities that are designed to work together

Common SaaS capabilities are not independent.

Authentication identifies an account. Organization membership determines which tenant the account can access. Roles authorize operations within that organization. Billing establishes subscription state. Entitlements translate the active plan into product access. Email supports verification, invitations, recovery, and billing-related communication.

When a team selects unrelated libraries for each area, it must design and maintain all of the connections between them. Helium provides a coherent model with shared concepts, explicit responsibility boundaries, and coordinated lifecycle behavior.

This reduces integration work and makes important rules easier to understand, such as:

- organization data must not be exposed across tenant boundaries;
- authentication alone does not grant access to an organization;
- organization roles and product entitlements answer different authorization questions;
- external billing events must be processed safely when they are delayed or delivered more than once;
- background work must remain recoverable when an external provider is temporarily unavailable.

## Avoid the copied-code trap

Starter kits and boilerplates can make the first days of development faster, but they are commonly copied into the new application. Once the team changes that code, it begins to diverge from its original source.

Over time, adopting upstream security fixes, dependency upgrades, database changes, or improved workflows becomes a manual comparison exercise. The initial shortcut can create a growing maintenance cost.

Helium follows a different model. It remains an identifiable, versioned dependency of the consuming application. Framework implementation code stays in Helium, while the application uses documented contracts and extension points. This makes supported upgrades, migrations, and fixes part of the normal application lifecycle rather than a later reconstruction project.

## Retain application and data ownership

Managed SaaS platforms can provide mature features quickly, but they may also control important parts of the runtime, storage model, deployment topology, or extension mechanism.

Helium is self-hosted. The consuming organization owns and operates the application and chooses where it runs. Product-specific code and data remain part of the consuming product, and Helium does not require a proprietary hosted runtime.

This model is useful when the team needs:

- direct control of application infrastructure and deployment;
- ownership of application and customer data;
- freedom to integrate product-specific services;
- access to the application and framework behavior during development and operations;
- the ability to move or redesign infrastructure without migrating away from a hosted Helium service.

Self-hosting also means that the consuming organization remains responsible for operations, including configuration, secrets, monitoring, backups, recovery, and infrastructure security.

## Customize without forking framework internals

A reusable foundation must support product-specific behavior. Helium provides default workflows and presentation, but it is not intended to make every application look or behave the same.

Supported customization is performed through configuration, public contracts, provider adapters, lifecycle events, and documented extension points. Product modules can use Helium capabilities while keeping their own domain models and persistence boundaries.

This approach separates two concerns:

- Helium maintains the common capability implementation and its invariants;
- the consuming application implements the product-specific experience and business rules.

The separation helps custom behavior survive framework upgrades because the application does not need to edit Helium's internal source code.

## Start from a supported application model

Architecture decisions consume time and create long-term consequences. Helium provides an official reference architecture for the initial supported path, including application composition, persistence, migrations, background processing, external-provider integration, deployment, and upgrades.

A supported path gives developers a concrete way to create, configure, run, deploy, and maintain an application. It also gives the framework a defined model that can be documented, tested, and supported consistently.

The reference model is intentionally opinionated. This reduces ambiguity for new applications, but teams should confirm that its boundaries fit their requirements before adoption. Review [Supported application model](supported-application-model.md) and [Product scope and current limitations](scope-and-limitations.md).

## How Helium compares with common alternatives

| Approach | Initial speed | Long-term maintenance | Operational control | Main trade-off |
| --- | --- | --- | --- | --- |
| Build all capabilities internally | Usually slower | Fully owned by the application team | Maximum | The team carries the full implementation, security, integration, and upgrade burden. |
| Copy a starter kit or boilerplate | Often fast | Becomes harder as local code diverges | High | Upstream fixes and improvements can be difficult to merge after customization. |
| Combine independent libraries | Moderate | Depends on the application's integration design | High | The team must define shared concepts, workflows, compatibility, and lifecycle behavior. |
| Use a managed SaaS platform | Often fast | Platform maintains much of the capability | Varies | Architecture, deployment, data, extension, or provider choices may be constrained. |
| Use Helium | Fast foundation through the supported path | Versioned framework, migrations, and upgrade guidance | High | The team accepts Helium's domain model and operates the self-hosted application. |

## When Helium is a good fit

Helium is a strong fit when:

- you are building a new SaaS application with .NET;
- common SaaS capabilities are delaying product-specific development;
- you want an integrated model rather than assembling unrelated components;
- you need to retain infrastructure and data control;
- you prefer a maintained framework dependency over copied source code;
- you can adopt the supported reference architecture for the initial application;
- you are prepared to operate a self-hosted application.

## When another approach may be better

Helium may not be the best fit when:

- you need a fully managed platform and do not want to operate application infrastructure;
- you need a language or runtime other than .NET;
- you must integrate individual modules into a significantly different existing architecture immediately;
- your required identity, billing, tenancy, or deployment model is outside the current supported scope;
- you need complete freedom to redefine the invariants of the capability domains that Helium manages;
- a small, short-lived prototype does not justify adopting a maintained application framework.

## The central trade-off

Helium is designed to combine delivery speed with durable ownership. You receive an opinionated, integrated, and upgradable SaaS foundation, while keeping control of the resulting product.

In exchange, your team adopts Helium's supported domain boundaries and remains responsible for operating the application. For teams whose priorities are .NET development, self-hosting, long-term maintainability, and product ownership, that trade-off can remove substantial repeated work without creating a dependency on copied code or a proprietary runtime.

To continue, read [What is Helium?](what-is-helium.md), review the [Supported application model](supported-application-model.md), and then follow the [Getting started](../getting-started/index.md) guide.