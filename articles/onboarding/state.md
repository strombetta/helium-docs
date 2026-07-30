---
title: Onboarding state
description: Interpret IsEmailVerified, RequiresFirstOrganization, IsComplete, and ActiveOrganizationId from IOnboardingApplication.
uid: onboarding-state
content_type: concept
area: onboarding
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Identity/IOnboardingApplication.cs
  - src/Trombetta.SaaS.Contracts/Identity/OnboardingState.cs
  - docs/engineering/ws-004-readiness.md
---

# Onboarding state

Call `IOnboardingApplication.GetStateAsync` for the authenticated account and route the user according to authoritative current state.

## Model

`OnboardingState` contains:

| Property | Meaning |
| --- | --- |
| `IsEmailVerified` | The authenticated account currently has a verified email address. |
| `RequiresFirstOrganization` | The account is eligible and still needs its first organization. |
| `IsComplete` | The supported first-organization onboarding requirement is satisfied. |
| `ActiveOrganizationId` | The current active organization identifier, or `null`. |

The state is a snapshot. It is not a client-editable workflow record.

## Read state

```csharp
OperationResult<OnboardingState> result =
    await onboardingApplication.GetStateAsync(cancellationToken);
```

Use the returned value to select presentation. Do not infer onboarding state from cookies, route values, UI history, or consumer tables.

## Invariants

- The operation requires an authenticated account.
- Email verification is authoritative framework state.
- First-organization creation is required only when no valid membership already completes onboarding.
- An active organization identifier is not an authorization grant by itself.
- Repeated reads may reflect state changes made by another request or accepted invitation.

## Failure conditions

Expected failures include unauthenticated access, temporary dependency unavailability, schema incompatibility, and bounded rate or configuration failures.

## Related tasks

- [Verify an email address](../identity/email-verification.md)
- [Create the first organization](first-organization.md)
- [Verify onboarding completion](completion.md)
