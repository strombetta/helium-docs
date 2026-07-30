---
title: Onboarding
description: Discover onboarding state and create the authenticated account's first organization through the implemented Helium preview contract.
uid: onboarding
content_type: index
area: onboarding
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Identity/IOnboardingApplication.cs
  - docs/engineering/ws-004-readiness.md
  - docs/api/public-design.md
---

# Onboarding

Use onboarding after account verification and authentication to establish the account's first valid organization and Owner membership.

> [!IMPORTANT]
> The onboarding application contract and PostgreSQL-backed behavior are implemented and verified in the preview repository. The official generated UI and consumer package release are not yet published.

## Start here

- [Onboarding state](state.md) — Decide whether verification or first-organization creation is required.
- [Create the first organization](first-organization.md) — Complete the only organization-creation path exposed by the Initial MVP onboarding contract.
- [Transactional onboarding](transactional-onboarding.md) — Understand the atomic state transition and rollback guarantees.

## Common tasks

- [Verify onboarding completion](completion.md)
- [Customize the onboarding experience](customize-experience.md)

## Key concepts

Onboarding is not a consumer-defined workflow engine. The public contract exposes state discovery and one atomic completion operation. It does not expose arbitrary step mutation, skip operations, additional-organization creation, membership administration, or framework persistence.

## Troubleshooting

Use operation errors and the returned correlation identifier. Do not inspect framework tables to infer partial completion; the supported transition is atomic.

## Reference

The public surface consists of `IOnboardingApplication`, `OnboardingState`, `CompleteFirstOrganizationCommand`, and `OnboardingCompletion` in `Trombetta.SaaS.Contracts.Identity`.
