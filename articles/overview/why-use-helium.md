---
title: Why use Helium?
description: Evaluate the intended benefits and trade-offs of using a versioned, integrated, and self-hosted SaaS framework for .NET.
uid: product-why-use-helium
content_type: overview
area: product
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/product/problem-statement.md
  - docs/product/vision.md
  - docs/product/requirements.md
---

# Why use Helium?

SaaS products repeatedly need identity, tenant isolation, authorization, billing, entitlements, email, persistence, operations, and upgrades. These concerns are necessary, security-sensitive, and closely connected, but they rarely differentiate the product.

Helium is intended to provide those concerns as one maintained .NET framework so that product teams can focus more engineering effort on their own domain.

> [!NOTE]
> This page explains the product rationale and target Initial MVP. It does not imply that every listed capability is available in the current preview.

## Reduce repeated platform work

Building common SaaS infrastructure internally requires product teams to design, secure, test, operate, and upgrade it for the lifetime of the application. A maintained framework can concentrate that work in one versioned implementation and one documented reference path.

The intended benefit is not only faster project creation. It is also a smaller amount of application-specific platform code that must be maintained indefinitely.

## Use an integrated domain model

Common SaaS capabilities are not independent:

- authentication identifies an account;
- membership determines which organizations the account can access;
- roles and policies authorize organization operations;
- billing establishes subscription facts;
- entitlements translate plans and subscription state into product access;
- durable processing protects external side effects from transient failures.

Combining unrelated libraries leaves the application team responsible for defining all of these relationships. Helium instead establishes explicit domain ownership and shared invariants.

## Keep the framework versioned

Copied starter code can accelerate the first implementation but diverges as soon as the application changes it. Later security fixes, dependency changes, migrations, and improved workflows must then be reconciled manually.

Helium is designed to remain an identifiable dependency. The consuming application references coordinated artifacts and uses supported public contracts. Framework internals, migrations, and reference presentation remain maintained upstream.

## Retain operational control

Helium is self-hosted. The consuming organization controls:

- application and product code;
- product-specific data;
- infrastructure and deployment;
- configuration and secrets;
- external integrations;
- monitoring, backups, recovery, and infrastructure security.

This avoids a mandatory proprietary hosted runtime, but it also means Helium does not operate the application for the consumer.

## Accept the central trade-off

The target value proposition combines an integrated and upgradable foundation with consumer ownership. In exchange, adopters accept:

- the supported reference architecture;
- Helium domain invariants for framework-owned capabilities;
- one declared runtime and database baseline;
- a coordinated framework release lifecycle;
- responsibility for self-hosted operations.

## When Helium may fit

Helium may fit when you are building a new .NET SaaS application, need common capabilities to work together, value infrastructure and data ownership, and can follow the official reference path.

## When another approach may fit better

Another approach may be more appropriate when you need a fully managed platform, a non-.NET runtime, immediate integration into a substantially different existing architecture, a database other than PostgreSQL, or complete freedom to redefine framework-owned invariants.

During the preview, another approach is also required when you need a production-ready framework now: Helium has not yet published a supported consumer release.

## Next steps

Review the [supported application model](supported-application-model.md) and [current limitations](scope-and-limitations.md) before preparing the [Get started prerequisites](../getting-started/prerequisites.md).