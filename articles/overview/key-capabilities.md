---
title: Key capabilities
description: Explore the core SaaS capabilities provided by Helium, their responsibilities, and how they work together.
uid: product-key-capabilities
content_type: overview
area: product
source:
  - docs/product/definition.md
  - docs/product/requirements.md
  - docs/architecture/technical-architecture.md
  - docs/api/public-design.md
---

# Key capabilities

Helium provides an integrated set of capabilities for building and operating SaaS applications. These capabilities share concepts, security boundaries, lifecycle rules, persistence infrastructure, and supported extension points.

A capability describes a product responsibility, not necessarily a single assembly, package, service, or user interface. One capability can involve several Helium components, and one component can support several capabilities.

This page describes Helium’s product capabilities. It does not indicate that every capability is available in every release. Review [Product scope and current limitations](scope-and-limitations.md) for the supported scope of the version you are using.

## Capability overview

| Capability | Primary responsibility |
| --- | --- |
| Identity | Manage accounts, credentials, verification, authentication, and account recovery. |
| Tenancy | Establish organizations as tenant boundaries and manage their memberships and lifecycle. |
| Authorization | Determine which authenticated accounts may perform operations within an organization. |
| Billing | Manage plans, checkout, subscriptions, provider synchronization, and commercial state. |
| Entitlements | Translate plan and subscription state into access to product capabilities. |
| Administration | Provide workflows for managing accounts, organizations, members, settings, and billing. |
| Notifications | Deliver required transactional communications and expose supported lifecycle reactions. |
| Audit | Preserve relevant lifecycle and operational facts for diagnostics, support, and traceability. |

## Identity

Identity manages the lifecycle of an application account.

It includes:

- account registration;
- email-address verification;
- password authentication;
- authenticated sessions;
- sign-out and session revocation;
- password recovery and reset;
- authenticated account context.

Identity establishes who is interacting with the application. It does not, by itself, grant access to an organization or its resources. Organization access depends on current membership and authorization.

Helium owns the security-sensitive identity workflows it provides while allowing consuming applications to configure supported behavior and react to documented lifecycle events.

Identity is used by tenancy to associate accounts with organizations and by authorization to establish the current authenticated account.

## Tenancy

Tenancy establishes the boundaries within which users collaborate and product data is accessed.

Helium represents a tenant as an organization. An account can belong to multiple organizations through separate memberships.

The tenancy capability includes:

- first-organization onboarding;
- organization creation and retrieval;
- organization settings;
- organization memberships;
- invitations;
- supported organization roles;
- ownership and ownership transfer;
- active-organization selection;
- validated organization context;
- organization isolation.

Selecting an active organization is contextual state, not an authorization grant. Helium revalidates the account’s current membership before protected operations use the organization context.

Consuming applications can associate their own records with a Helium organization identifier, but those records remain owned by the consuming application.

## Authorization

Authorization determines whether an authenticated account can perform a specific operation within a validated organization context.

Authorization evaluates current framework-owned state, including:

- the authenticated account;
- the selected and accessible organization;
- the account’s current membership;
- the membership’s semantic role;
- the requested framework or consumer policy;
- operation-specific requirements;
- an entitlement when the operation explicitly requires one.

Helium uses organization-scoped roles such as `Owner`, `Administrator`, and `Member`. Roles and policies are evaluated on the server and are not inferred from navigation visibility, route values, client input, or unvalidated claims.

Consuming applications can compose their own authorization requirements with mandatory Helium requirements. Consumer policies can strengthen framework authorization but cannot bypass framework-owned security decisions.

Authorization establishes permission to attempt an operation. Domain invariants and concurrency rules must still be enforced by the workflow that owns the operation.

## Billing

Billing manages the commercial relationship associated with an organization.

The billing capability includes:

- plan definitions;
- billing intervals;
- provider price mappings;
- hosted checkout;
- customer billing management;
- authenticated provider-event handling;
- normalized local subscription state;
- subscription synchronization;
- cancellation state;
- payment-failure handling;
- billing authorization.

The supported billing provider remains behind an integration boundary. Provider SDK objects and webhook payloads do not become application-facing authorization or entitlement contracts.

External provider events are authenticated, accepted durably, deduplicated, and translated into normalized local state. Protected application requests use this local state instead of making direct provider calls.

An allowed billing operation does not automatically grant access to product functionality. Product access is determined separately through entitlements.

## Entitlements

Entitlements determine which product capabilities are available to an organization.

An entitlement is identified by a stable application-facing key. Helium evaluates that key against the organization’s effective plan, normalized subscription state, and configured plan-to-entitlement mapping.

The entitlement capability includes:

- entitlement definitions;
- plan-to-entitlement mappings;
- effective entitlement evaluation;
- provider-neutral allow and deny results;
- bounded denial reasons;
- integration with organization authorization;
- testing support for entitlement-dependent product behavior.

Entitlements are distinct from roles:

- roles describe what a member may administer or operate within an organization;
- entitlements describe what the organization’s plan makes available.

A protected operation can require both an authorized role and an allowed entitlement. Neither condition bypasses the other.

## Administration

Administration provides supported workflows through which users manage Helium-owned state.

Administrative workflows can include:

- personal account settings;
- organization settings;
- member discovery and management;
- invitations;
- role changes;
- membership removal;
- ownership transfer;
- active-organization selection;
- billing management;
- presentation of authorization and validation outcomes.

Administration is a cross-cutting capability rather than a single domain module. Its workflows coordinate identity, tenancy, authorization, billing, entitlements, notifications, and persistence.

Helium can provide default administrative interfaces and application services. Consuming applications can configure supported presentation behavior or replace the presentation while continuing to use the public application contracts.

Administrative user interfaces are not security boundaries. Every protected administrative operation remains subject to server-side authorization, current-state validation, domain invariants, and concurrency handling.

## Notifications

Notifications communicate required lifecycle information to users and allow applications to react to supported framework events.

The Initial MVP notification model centers on transactional email and durable lifecycle processing.

Supported concerns include:

- account-verification messages;
- password-recovery messages;
- organization invitations;
- invitation-acceptance communications;
- material membership or ownership changes;
- material billing-state communications;
- rendered message templates;
- sender and branding configuration;
- provider-neutral email delivery;
- retry and failure handling;
- consumer lifecycle handlers.

Helium records required external work durably before delivery. Delivery failures do not roll back an already committed domain operation, and retryable work remains observable.

Consuming applications can replace the transactional-email provider through a supported contract and react to documented lifecycle events. They do not need to depend on provider-specific message or SDK types.

## Audit

Audit preserves relevant facts about framework lifecycle transitions and operational processing.

Audit-related information can support:

- security investigation;
- support and troubleshooting;
- durable-work inspection;
- provider-event deduplication;
- lifecycle traceability;
- diagnosis of failed or indeterminate operations;
- reconstruction of material framework state changes.

Audit is not equivalent to application logging. Logs describe runtime execution and diagnostics, while durable audit or lifecycle facts describe relevant state transitions and processing outcomes.

Helium exposes bounded identifiers, result codes, timestamps, and lifecycle facts where required. It avoids including credentials, secrets, raw provider data, or unrelated tenant information in diagnostics.

The availability of a complete user-facing audit-log product depends on the supported release scope. Consuming applications remain responsible for audit requirements that belong to their product-specific domain.

## Platform foundations

The key capabilities are supported by shared platform foundations that are not themselves independent SaaS business capabilities.

These foundations include:

- public contracts and configuration;
- PostgreSQL persistence;
- framework-owned database migrations;
- inbox and outbox processing;
- retries, leasing, and deduplication;
- startup validation;
- health information and diagnostics;
- testing support;
- hosting and middleware integration;
- deployment and upgrade support.

These foundations give the capabilities a consistent operational and compatibility model. They also allow consuming applications to keep product-specific code and data outside Helium’s internal implementation.

## How the capabilities work together

A typical protected product operation crosses several capability boundaries:

1. Identity resolves the authenticated account.
2. Tenancy resolves and validates the active organization and current membership.
3. Authorization evaluates the required role and policy.
4. Entitlements evaluate product access when required.
5. The owning workflow applies its domain invariants and persists the result.
6. Notifications and audit processing record or communicate relevant lifecycle outcomes.
7. Durable processing completes external side effects outside the request transaction.

Billing modifies the organization’s normalized commercial state asynchronously. Entitlements then use that local state when evaluating product access.

This separation prevents authentication, organization selection, role, billing-provider state, or entitlement state from being treated as interchangeable forms of authority.

## Capability boundaries

Helium owns the domains, invariants, and data required for the capabilities it manages. The consuming application owns its product-specific domain and determines how its own data is modeled and stored.

A consuming application can:

- call Helium through public contracts;
- store Helium account or organization identifiers on product-owned records;
- define consumer authorization policies;
- define product entitlement keys;
- react to documented lifecycle events;
- replace supported external providers;
- customize or replace supported presentation elements.

A consuming application must not depend on Helium’s internal entities, database implementation, provider SDK objects, or undocumented services as extension contracts.

## Next steps

- Read [What is Helium?](what-is-helium.md) for the product overview.
- Review the [supported application model](supported-application-model.md).
- Understand the [reference application architecture](../fundamentals/reference-architecture.md).
- Review [Product scope and current limitations](scope-and-limitations.md) before relying on a capability.
