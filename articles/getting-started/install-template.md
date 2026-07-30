---
title: Project template availability
description: Check the status of the future Trombetta.SaaS.Templates package and understand why no installation command is published yet.
uid: getting-started-template-availability
content_type: overview
area: getting-started
version: preview
status: preview
last_reviewed: 2026-07-30
source:
  - src/Trombetta.SaaS.Templates/Trombetta.SaaS.Templates.csproj
  - docs/engineering/project-structure.md
  - docs/planning/implementation-plan.md
---

# Project template availability

The accepted artifact model reserves `Trombetta.SaaS.Templates` as the `dotnet new` tooling package for the official Initial MVP application.

> [!WARNING]
> No supported installation command is available. Do not publish, install, or depend on a locally packed template project as though it were a Helium release.

## Current state

The repository contains a packable `Trombetta.SaaS.Templates` project whose current responsibility is to reserve the future tooling artifact boundary. The engineering project-structure record identifies it as a future template package with no runtime project references.

The project does not yet establish:

- a template short name;
- generated application content;
- template parameters;
- application package references;
- local configuration examples;
- container files;
- template installation or uninstall commands;
- generated-application build and startup evidence;
- release compatibility metadata.

## Release requirements

Installation instructions can be published only after the release process provides:

1. a coordinated set of consumer packages;
2. a complete template package;
3. a documented template identifier and parameters;
4. automated generated-application restore, build, migration, and startup tests;
5. exact release compatibility information;
6. package provenance and release notes;
7. a supported upgrade path.

## What not to do

Do not:

- reference the template project directly from an application;
- infer a template short name from the package ID;
- use repository build output as a supported package feed;
- copy framework source or migrations into a consumer application;
- document placeholder commands that have not been tested against published artifacts.

## Follow availability

Template availability will be announced through:

- [What’s new](../whats-new/index.md);
- release notes for the first published consumer version;
- an updated Get started tutorial;
- the package and compatibility reference.

## Next steps

Review the [supported application model](../overview/supported-application-model.md) and [product limitations](../overview/scope-and-limitations.md).