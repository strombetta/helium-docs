---
title: Update organization settings
description: Update the supported organization name with an opaque optimistic-concurrency precondition.
uid: organizations-settings
content_type: how-to
area: organizations
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Organizations/IOrganizationApplication.cs
  - src/Trombetta.SaaS.Contracts/Organizations/UpdateOrganizationCommand.cs
  - docs/engineering/organization-discovery-and-settings.md
---

# Update organization settings

The Initial MVP organization settings surface supports changing the organization name through `IOrganizationApplication.UpdateOrganizationAsync`.

> [!IMPORTANT]
> Organization retrieval and name update are implemented preview foundations. Complete policy enforcement depends on the remaining WS-005 authorization work.

## Prerequisites

- Retrieve the current `OrganizationSnapshot`.
- Preserve its opaque `VersionToken` without parsing or comparing it.
- Ensure the caller is authenticated and the application applies the current organization-update authorization boundary.

## Submit the update

```csharp
var command = new UpdateOrganizationCommand(
    organization.OrganizationId,
    "Contoso Projects",
    organization.Version);

OperationResult<OrganizationSnapshot> result =
    await organizationApplication.UpdateOrganizationAsync(
        command,
        cancellationToken);
```

Use the returned snapshot as the authoritative committed state.

## Handle concurrency

A stale expected version returns `concurrency_conflict`. Refresh the organization, show the current value, and require the user to confirm a new update. Do not retry automatically with a newly loaded token.

## Scope limitations

The operation cannot change organization identity, ownership, membership state, lifecycle state, billing state, slug, domain, or arbitrary metadata.

## Verify the result

After success, verify that:

- the returned name is the accepted committed value;
- the returned version differs from the submitted expected version;
- organization identity is unchanged;
- stale and foreign identifiers produce controlled failures without disclosure.

## Next steps

Review [Roles](roles.md) and [Authorization model](../authorization/model.md).
