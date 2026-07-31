---
title: Authorization troubleshooting
description: Diagnose missing organization context, policy denial, stale membership state, reserved names, and fail-closed dependency behavior.
uid: authorization-troubleshooting
content_type: troubleshooting
area: authorization
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - docs/engineering/organizations-context-and-authorization-specification.md
  - docs/api/public-design.md
---

# Authorization troubleshooting

Use this guide while integrating the accepted authorization contracts. WS-005 runtime readiness is still in progress, so distinguish integration defects from unavailable implementation.

## Symptoms

- `IOrganizationContextAccessor.Current` is null for an authenticated request.
- A known role receives a forbidden decision.
- A policy name is rejected during composition or startup.
- A removed membership appears to retain access.
- A foreign organization request returns a generic not-found result.
- Authorization fails during a database or validation dependency outage.

## Possible causes

- Active organization context or policy handlers are not yet implemented in the selected framework build.
- Middleware ordering is unsupported.
- The account has zero memberships or multiple memberships without explicit selection.
- The stored preference is stale, malformed, or no longer accessible.
- The policy identifier is unknown, misspelled, unregistered, reserved, or colliding.
- The caller lacks the required current role or a capability-specific invariant fails.
- Dependency failure correctly triggered fail-closed behavior.

## Diagnostic steps

1. Confirm the exact framework commit or package version under evaluation.
2. Verify authoritative authenticated account context before organization resolution.
3. List the current account memberships through `IOrganizationApplication`.
4. Compare the requested identifier with the explicit operation scope without logging protected details.
5. Use constants from `FrameworkAuthorizationPolicies`.
6. Check current role, membership state, expected version, target ownership, and entitlement requirements independently.
7. Preserve the correlation identifier and inspect bounded server diagnostics.

## Resolution

Correct middleware ordering, require explicit selection when multiple memberships exist, refresh stale state, use a registered policy constant, fix consumer policy collisions, or restore the validation dependency. Do not reconstruct authority from claims, cookies, routes, or cached UI state.

When the required WS-005 component is not implemented, keep the integration behind preview-only development code and do not deploy the protected operation as supported behavior.

## Verify the resolution

Repeat the operation with allowed and denied roles, removed membership, foreign organization, stale preference, unknown policy, and dependency outage. Confirm the system denies safely and discloses no protected cross-organization state.

## Related documentation

- [Authorization model](model.md)
- [Validated organization context](../organizations/validated-context.md)
- [Organization isolation](../organizations/isolation.md)
