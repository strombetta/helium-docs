---
title: Create the first organization
description: Complete first-organization onboarding atomically with IOnboardingApplication.
uid: onboarding-create-first-organization
content_type: how-to
area: onboarding
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Identity/IOnboardingApplication.cs
  - src/Trombetta.SaaS.Contracts/Identity/CompleteFirstOrganizationCommand.cs
  - docs/engineering/ws-004-readiness.md
---

# Create the first organization

Use `CompleteFirstOrganizationAsync` to create the account's first organization, initial Owner membership, active preference, and required lifecycle work in one framework transaction.

## Prerequisites

The current account must:

- be authenticated through the framework account context;
- have a verified email address;
- have no existing valid organization membership;
- provide a valid organization name.

Read [Onboarding state](state.md) immediately before presenting or submitting the operation.

## Submit the organization name

```csharp
var command = new CompleteFirstOrganizationCommand("Contoso");

OperationResult<OnboardingCompletion> result =
    await onboardingApplication.CompleteFirstOrganizationAsync(
        command,
        cancellationToken);
```

The operation is not a general organization-creation API. The Initial MVP public contract exposes only first-organization onboarding.

## Handle repeated or competing requests

If a valid membership already exists, onboarding is complete and the operation must not create another organization. Concurrent requests produce one coherent result without duplicate first organizations or Owner memberships.

## Verify the result

After success, verify that:

- `result.Value.Organization` contains the created organization snapshot;
- `result.Value.Context` identifies the authenticated account, organization, Owner membership, and Owner role;
- a fresh onboarding-state read reports completion;
- protected organization operations still enforce current authorization.

Do not verify completion by querying framework persistence directly.

## Troubleshooting

A failure before commit leaves no partial organization, membership, active preference, or lifecycle work. Use the operation correlation identifier to inspect bounded diagnostics.

## Next steps

Continue to [Verify onboarding completion](completion.md) and review [Organizations and tenant context](../fundamentals/organizations-and-tenant-context.md).
