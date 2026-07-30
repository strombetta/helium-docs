---
title: Customize the onboarding experience
description: Build consumer presentation around the fixed Helium onboarding contract without weakening its state or security invariants.
uid: onboarding-customize-experience
content_type: concept
area: onboarding
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/api/public-design.md
  - docs/engineering/identity-and-onboarding-specification.md
  - docs/architecture/decisions/application-architecture.md
---

# Customize the onboarding experience

A consuming application can choose its routes, forms, copy, branding, and navigation around `IOnboardingApplication`. Custom presentation does not replace or redefine the framework onboarding state machine.

## Model

A custom experience can:

- read `OnboardingState` and choose the next page;
- collect a first organization name;
- invoke `CompleteFirstOrganizationAsync`;
- map safe field and operation errors to the UI;
- redirect after a verified successful result;
- add consumer-owned educational or product setup steps after Helium onboarding.

## Fixed framework behavior

Customization cannot:

- mark an unverified account as verified;
- skip required first-organization creation while reporting completion;
- create the first Owner outside the onboarding transaction;
- mutate onboarding or organization persistence directly;
- fabricate authenticated or organization context;
- convert the operation into arbitrary additional-organization creation;
- suppress server-side authorization because a step was shown in the UI.

## Consumer-owned steps

Product setup that does not own Helium state can occur after the framework onboarding transaction. Keep consumer state in consumer persistence and make any reaction to `OrganizationCreated` idempotent because lifecycle delivery is at least once.

## Failure conditions

A browser refresh, duplicate form submission, or concurrent request must be safe. Re-read onboarding state and handle the current authoritative result instead of relying on a client-maintained step number.

## Current availability

The reference presentation and generated application experience are not yet published. This page documents the supported contract boundary for future reference UI and consumer-owned presentation.

## Related tasks

- [Onboarding state](state.md)
- [Create the first organization](first-organization.md)
- [Identity security considerations](../identity/security-considerations.md)
