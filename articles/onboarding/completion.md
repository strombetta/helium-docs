---
title: Verify onboarding completion
description: Verify OnboardingCompletion, refresh state, and transition the application to validated organization context.
uid: onboarding-verify-completion
content_type: how-to
area: onboarding
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Identity/OnboardingCompletion.cs
  - src/Trombetta.SaaS.Contracts/Identity/OnboardingState.cs
  - docs/engineering/ws-004-readiness.md
---

# Verify onboarding completion

Use the returned `OnboardingCompletion` and a fresh state read to transition the application from account-only identity to organization-scoped presentation.

## Prerequisites

- `CompleteFirstOrganizationAsync` returned a successful result.
- The current request still represents the authenticated account that performed onboarding.
- The application uses framework authorization for subsequent organization operations.

## Read the completion result

```csharp
OnboardingCompletion completion = result.Value!;

OrganizationSnapshot organization = completion.Organization;
OrganizationContext context = completion.Context;
```

The context returned by the framework describes the completed transition. Consumer-created copies do not establish authority.

## Refresh onboarding state

```csharp
OperationResult<OnboardingState> stateResult =
    await onboardingApplication.GetStateAsync(cancellationToken);
```

After completion, expect `IsComplete` to be `true`, `RequiresFirstOrganization` to be `false`, and `ActiveOrganizationId` to identify the active organization.

## Continue with organization-scoped work

Use the supported organization context and authorization pipeline for protected operations. Do not treat an organization identifier in a URL, cookie, form, or consumer record as sufficient authorization.

## Verify the result

Verify that:

- the organization snapshot and context identify the same organization;
- the context account matches the authenticated account;
- the membership role is Owner;
- a repeated completion attempt does not create another first organization;
- lifecycle-handler failure does not change the completed state.

## Troubleshooting

When state appears incomplete after a successful operation, preserve both operation correlation identifiers and inspect schema compatibility and request authentication before retrying. Do not create consumer-side repair rows.

## Next steps

Review [Organizations and tenant context](../fundamentals/organizations-and-tenant-context.md) and [Memberships, roles, and authorization](../fundamentals/memberships-roles-authorization.md).
