---
title: Discover and retrieve organizations
description: List the current account memberships and retrieve an accessible organization through IOrganizationApplication.
uid: organizations-discover-retrieve
content_type: how-to
area: organizations
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Organizations/IOrganizationApplication.cs
  - docs/engineering/organization-discovery-and-settings.md
  - docs/planning/implementation-plan.md
---

# Discover and retrieve organizations

Use `IOrganizationApplication` to discover current memberships for the authenticated account and retrieve one accessible organization.

> [!IMPORTANT]
> These operations are implemented preview foundations. The official consumer package and project template are not yet published.

## Prerequisites

- The request has an authoritative authenticated account context.
- Resolve `IOrganizationApplication` from the request scope.
- Treat returned identifiers and version tokens as opaque application values.

## List current memberships

```csharp
OperationResult<IReadOnlyList<OrganizationMembership>> result =
    await organizationApplication.ListMembershipsAsync(cancellationToken);
```

The result contains only current valid memberships belonging to the authenticated account. Each item includes the membership identifier, organization identifier, organization name, and current semantic role.

## Retrieve an organization

```csharp
OperationResult<OrganizationSnapshot> result =
    await organizationApplication.GetOrganizationAsync(
        organizationId,
        cancellationToken);
```

Absent, inaccessible, and cross-organization identifiers use safe not-found-equivalent behavior when disclosure would be unsafe.

## Organization creation boundary

The public contract does not expose general organization creation after onboarding. The supported first organization is created atomically through `IOnboardingApplication.CompleteFirstOrganizationAsync`.

## Verify the result

Verify that:

- membership discovery never returns removed or foreign memberships;
- retrieval returns the requested accessible organization only;
- the returned `VersionToken` is retained for a later update;
- inaccessible identifiers do not disclose protected organization state.

## Next steps

Continue to [Update organization settings](settings.md) or review [Active organization selection](active-organization.md).
