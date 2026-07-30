---
title: Prerequisites
description: Prepare the accepted .NET 10 and PostgreSQL 18 baseline for the future Helium reference-application path.
uid: getting-started-prerequisites
content_type: reference
area: getting-started
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - global.json
  - docs/architecture/decisions/technology-baseline.md
---

# Prerequisites

The future official reference-application path uses one declared runtime and database baseline. Preparing these prerequisites does not provide access to a consumer release or template.

## Required technology baseline

| Requirement | Preview baseline | Notes |
| --- | --- | --- |
| .NET SDK | .NET 10 | The framework repository currently selects SDK `10.0.302`; a release may validate a later supported servicing patch. |
| ASP.NET Core runtime | 10 | Installed with the corresponding .NET runtime or SDK. |
| PostgreSQL | 18 | The only database major version selected for the Initial MVP reference path. |
| Git | Current supported client | Required to work with source repositories and contribution workflows. |

An OCI-compatible container runtime will be required for the validated production deployment path, but it is not required merely to review the documentation or inspect framework source.

## Operating-system expectations

The development path is intended to remain portable across operating systems supported by the selected .NET SDK and PostgreSQL tooling. The production validation target is a consumer-controlled Linux container host.

Release documentation will identify any additional operating-system, architecture, or container-image constraints.

## Verify .NET

Run:

```bash
dotnet --version
```

For the current framework checkout, the selected SDK feature band begins with:

```text
10.0.302
```

A later patch in the same feature band may be selected through the repository `global.json` roll-forward policy.

## Verify PostgreSQL tooling

Run:

```bash
psql --version
```

The reported major version must be 18 for the Initial MVP compatibility target. Having the client installed does not confirm that a reachable PostgreSQL 18 server is configured.

## Credentials and external providers

The complete reference path will eventually require:

- a local PostgreSQL connection with permission to create or migrate the application database;
- an email-provider configuration for transactional workflows;
- Stripe test-mode credentials for billing scenarios;
- local secret storage that does not commit credentials to source control.

Do not create production credentials for an unreleased tutorial.

## Current blocker

The official `Trombetta.SaaS.Templates` package is not yet usable or published. Continue to [Project template availability](install-template.md) rather than inventing an installation command.