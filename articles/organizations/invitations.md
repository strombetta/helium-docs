---
title: Invitations
description: Understand the accepted organization invitation contract, token rules, administration operations, and current WS-005 status.
uid: organizations-invitations
content_type: concept
area: organizations
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Contracts/Organizations/IMembershipApplication.cs
  - docs/api/public-design.md
  - docs/engineering/organizations-context-and-authorization-specification.md
---

# Invitations

An organization invitation is an email-bound, organization-bound, single-use offer to create a current `Administrator` or `Member` membership.

> [!WARNING]
> Invitation listing, issuance, revocation, acceptance, durable communication integration, and readiness verification remain in progress in WS-005.

## Token model

Invitation tokens are opaque, purpose-specific, valid for seven days, bound to the normalized invited email, single-use, and invalid after acceptance or revocation. Reusable plaintext tokens must never be persisted or emitted in diagnostics.

Acceptance requires an authenticated account, a verified email address, an exact normalized email match, and a currently valid invitation.

## Administration contract

`IMembershipApplication` defines:

- `ListInvitationsAsync` for scoped cursor pagination;
- `InviteMemberAsync` for `Administrator` or `Member` invitations;
- `RevokeInvitationAsync` with an expected version token;
- `AcceptInvitationAsync` with the opaque token.

A second pending invitation for the same organization and normalized email returns `invitation_already_pending`. There is no public resend operation.

## Invariants

- An ordinary invitation cannot assign Owner.
- Cross-organization invitation identifiers must not disclose protected state.
- Invitation state and required durable email intent commit atomically.
- Acceptance creates at most one logical membership.
- Later protected operations still require validated organization context and authorization.

## Related tasks

- [Memberships](memberships.md)
- [Transactional onboarding](../onboarding/transactional-onboarding.md)
- [Transactional email](../communications/index.md)
