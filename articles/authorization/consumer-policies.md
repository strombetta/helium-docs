---
title: Define consumer policies
description: Register additive consumer-owned authorization policies without using reserved Helium names or weakening framework policy requirements.
uid: authorization-consumer-policies
content_type: how-to
area: authorization
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS/ConsumerAuthorizationPolicyComposition.cs
  - src/Trombetta.SaaS/ConsumerAuthorizationPolicyBuilder.cs
  - src/Trombetta.SaaS/ConsumerAuthorizationPolicyDefinitionBuilder.cs
---

# Define consumer policies

Use `AddConsumerAuthorizationPolicies` to declare additive product policies while preserving framework policy ownership.

> [!WARNING]
> The public builder surface exists, but complete runtime evaluation, collision enforcement, handler integration, and WS-005 readiness remain in progress.

## Prerequisites

- Choose a consumer-owned policy namespace such as `Acme.Projects.*`.
- Identify the minimum required framework policy and roles.
- Implement any consumer-owned requirement handler against consumer-owned services and persistence.

## Register a policy

```csharp
builder.Services
    .AddTrombettaSaaS(
        builder.Configuration.GetRequiredSection("TrombettaSaaS"))
    .AddConsumerAuthorizationPolicies(policies =>
    {
        policies
            .AddPolicy("Acme.Projects.Edit")
            .RequireFrameworkPolicy(
                FrameworkAuthorizationPolicies.OrganizationsView)
            .RequireOrganizationRoles(
                OrganizationRole.Owner,
                OrganizationRole.Administrator)
            .AddRequirement("Acme.Projects.Edit.Requirement");
    });
```

Consumer policies are additive. Registration does not automatically implement a consumer requirement handler or grant a framework operation.

## Naming and composition rules

- Names beginning with `Trombetta.SaaS.` are reserved.
- Duplicate consumer names and framework collisions must fail during composition or startup.
- Consumer code cannot redefine framework roles or replace framework handlers.
- A consumer requirement cannot fabricate organization context or accept unvalidated identifiers.

## Verify the result

Verify startup rejection for blank, duplicate, reserved, and colliding names. Test every consumer requirement with current membership, foreign organization, role change, membership removal, and dependency failure.

## Next steps

Apply the policy to [ASP.NET Core endpoints](protect-endpoints.md) and server-side [application operations](protect-operations.md).
