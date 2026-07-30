---
title: Supported versions
description: Check the accepted .NET, ASP.NET Core, Entity Framework Core, Npgsql, and PostgreSQL baseline for the Helium preview.
uid: compatibility-supported-versions
content_type: reference
area: compatibility
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - global.json
  - docs/architecture/decisions/technology-baseline.md
  - docs/planning/implementation-plan.md
---

# Supported versions

Helium has an accepted Initial MVP technology baseline, but it does not yet have a supported consumer release. The versions below define the engineering and future reference-application compatibility target; they are not a production support promise for unpublished artifacts.

## Current development baseline

| Technology | Accepted major version |
| --- | --- |
| .NET | 10 LTS |
| ASP.NET Core | 10 |
| Entity Framework Core | 10 |
| Npgsql | 10 |
| Npgsql Entity Framework Core provider | 10 |
| PostgreSQL | 18 |

The framework repository currently selects .NET SDK `10.0.302` through `global.json`, with `rollForward` set to `latestPatch` and prerelease SDKs disabled.

## Servicing policy

The accepted architecture declares compatibility at major-version level. Individual releases are expected to record the exact SDK, runtime, dependency, database, and container versions used for validation.

Supported deployments will be expected to remain on supported servicing and security updates within the declared major-version boundary. A new major version requires explicit compatibility evaluation.

## Database boundary

PostgreSQL 18 is the only database major version selected for the Initial MVP reference path. Earlier PostgreSQL versions, future PostgreSQL majors, and alternative database engines are outside the declared compatibility boundary unless a later decision explicitly adds support.

Consumers will remain responsible for PostgreSQL minor updates, availability, capacity, access control, backups, recovery, and major-version upgrades.

## Release availability

No stable or preview consumer package version is documented by this site yet. Do not infer availability from project files, package IDs, internal build output, or repository workstream completion.

A release becomes consumable only when coordinated artifacts are published and accompanied by:

- exact compatibility metadata;
- release notes;
- migration information;
- a validated project template;
- a documented upgrade path;
- applicable known limitations.

## Next steps

Review the [supported application model](supported-application-model.md), [current limitations](scope-and-limitations.md), and [Get started prerequisites](../getting-started/prerequisites.md).