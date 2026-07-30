---
title: Authoring conventions
description: Follow the editorial, structural, terminology, code-sample, and accessibility conventions for Helium documentation.
content_type: reference
area: contributing
version: all
status: stable
last_reviewed: 2026-07-30
---

# Authoring conventions

Use these conventions when writing or reviewing manual content in `strombetta/helium-docs`. They apply to overview, conceptual, tutorial, how-to, reference, troubleshooting, release, and contribution pages.

## Language and voice

Write in US English. Use a direct, technical, and neutral style.

- Use active voice when it identifies responsibility clearly.
- Use present tense for supported behavior.
- Address the reader as `you` in procedures.
- Refer to the product as `Helium`, not `we`.
- Prefer specific subjects and verbs over abstract nouns.
- Keep paragraphs focused on one primary idea.
- Avoid promotional claims that cannot be verified.

Preferred:

> Helium validates the active organization before it evaluates an organization-scoped operation.

Avoid:

> We perform validation so that operations can be handled securely.

## Page anatomy

A manual page normally uses this order:

1. front matter;
2. one `H1` heading;
3. a short introduction;
4. a status notice when required;
5. the main content;
6. verification, summary, or resolution where applicable;
7. curated next steps and related reference.

The `title` metadata and `H1` must normally match exactly.

## Introductions

The introduction should explain what the page covers, the result it provides, and when it is relevant. Use one or two short paragraphs.

How-to example:

> Use Helium authorization policies to protect application endpoints. This guide shows how to require an authenticated organization member and evaluate an organization-scoped policy.

Concept example:

> An organization context identifies the organization against which an authenticated request is evaluated. Helium validates this context before organization-scoped operations execute.

Avoid generic openings such as `This document discusses...` or `In this article, you will learn about...` when the subject can be stated directly.

## Content-type templates

Each page has one dominant content type. See [Metadata reference](metadata-reference.md) for allowed values.

### Index

Use this structure as applicable:

```markdown
# Authorization

Briefly define the section and its boundary.

## Start here
## Common tasks
## Key concepts
## Troubleshooting
## Reference
```

An index page must provide orientation and recommendations. It must not be an empty container or a copy of the local TOC.

### Overview

Use an overview to explain what an area provides, why it exists, and when it applies.

```markdown
# Organizations and tenancy

## What Helium provides
## How it fits into the application
## Main components
## Important constraints
## Limitations
## Next steps
```

### Concept

Use a concept page to explain a model, relationship, lifecycle, invariant, or supported behavior.

```markdown
# Active organization context

## Context model
## Selection and validation
## Invariants
## Failure conditions
## Security implications
## Related tasks
```

Distinguish supported contracts from implementation details. Do not describe observable internal behavior as a compatibility guarantee unless the framework explicitly supports it.

### Tutorial

A tutorial teaches through one complete and reproducible scenario.

```markdown
# Create your first Helium application

## Prerequisites
## What you will build
## Prepare the environment
## Create the application
## Configure the application
## Run the application
## Verify the result
## What you learned
## Next steps
```

Use one supported configuration and one consistent example. Move alternatives and optional variants to separate how-to guides.

### How-to

A how-to guide completes one specific task.

```markdown
# Configure Stripe webhooks

## Prerequisites
## Configure the endpoint
## Configure the signing secret
## Verify webhook delivery
## Troubleshooting
## Next steps
```

Start the title with an action verb such as `Configure`, `Create`, `Protect`, `Implement`, `Apply`, `Deploy`, `Test`, `Verify`, `Upgrade`, or `Replace`.

### Reference

Reference pages use a predictable structure and provide exact definitions. For a configuration option, include as applicable:

- configuration key;
- type;
- whether it is required;
- default value;
- valid values;
- behavior;
- security considerations;
- environment-variable form;
- example;
- version information.

Generated API reference owns signatures, inheritance, parameters, return types, and XML documentation. Manual reference owns functional catalogs such as configuration, error codes, policies, lifecycle events, endpoints, and compatibility.

### Troubleshooting

Start from an observable symptom.

```markdown
# Stripe webhooks are rejected

## Symptoms
## Possible causes
## Diagnostic steps
## Resolution
## Verify the resolution
## Information to collect
## Related documentation
```

Diagnostic evidence must precede corrective action. Do not recommend random configuration changes or restarts without explaining what evidence they test.

### Release

Release content must distinguish:

- release notes;
- what's new summaries;
- breaking changes;
- deprecations;
- upgrade guides;
- compatibility information.

A breaking-change page identifies previous behavior, new behavior, affected applications, required changes, and verification steps.

## Headings

Use sentence case.

Preferred:

- `Configure Stripe webhooks`
- `How the active organization is selected`
- `Verify webhook delivery`

Preserve official capitalization for names such as `.NET`, `ASP.NET Core`, `PostgreSQL`, `Stripe`, `GitHub`, and `DocFX`.

Use one `H1` per page. Normal content hierarchy is limited to `H1`, `H2`, and `H3`. Do not skip heading levels. Use `H4` only when a page cannot be structured clearly without it.

Prefer descriptive headings over generic labels such as `Details`, `Information`, `General`, or `Additional considerations`.

## Procedures

Use numbered lists only when order matters. Use bullet lists for prerequisites, options, characteristics, and unordered results.

Each numbered step should contain one primary action. State a significant expected result immediately after the action.

Preferred:

```markdown
1. Run the migration host.

   The process exits with code `0` after all pending framework migrations are applied.
```

Avoid combining setup, execution, and verification into one long step.

## Code samples

Every code fence must declare an appropriate language, such as `csharp`, `json`, `yaml`, `bash`, or `text`.

Before a sample, explain:

- where the code belongs;
- what it changes;
- any symbols or setup it assumes.

After a sample, explain only the non-obvious behavior. Do not paraphrase every line.

Code samples must be:

- syntactically valid;
- applicable to the documented version;
- minimal for the task;
- complete enough to copy safely;
- free of realistic secrets or credentials.

Use explicit comments for omitted context:

```csharp
// Existing service registrations.
```

Do not use screenshots for source code, configuration, commands, or output.

## Commands and output

Do not include shell prompts such as `$` or `>` in copyable commands.

Separate commands from output:

```markdown
Run:

```bash
dotnet run
```

The application reports:

```text
Application started.
```
```

Do not create operating-system variants when the command is identical.

## Placeholders

Use lowercase angle-bracket placeholders:

- `<connection-string>`
- `<stripe-api-key>`
- `<webhook-signing-secret>`
- `<organization-id>`

Avoid values such as `YOUR_KEY_HERE`, `foo`, `abc123`, or credentials that resemble real secrets.

## Callouts

Use DocFX callouts according to their semantic purpose.

| Callout | Use |
| --- | --- |
| `NOTE` | Supplemental information that is useful but not required. |
| `TIP` | Optional advice that makes a task easier. |
| `IMPORTANT` | Information required for a correct result. |
| `WARNING` | A security, compatibility, or data-loss risk. |
| `CAUTION` | An action that can produce an undesirable operational consequence. |

Example:

```markdown
> [!WARNING]
> Do not disable Stripe signature validation in production.
```

Do not hide prerequisites in callouts. Avoid consecutive callouts when normal prose or a structured section is clearer.

## Tables

Use tables for structured comparison, configuration matrices, role and state definitions, compatibility information, and symptom-to-cause mappings.

Every table must have meaningful column headings. Do not use tables for page layout, long procedures, or large code samples. The meaning must not depend on color.

## Links

Use descriptive link text.

Preferred:

```markdown
Review the [supported application model](../overview/supported-application-model.md).
```

Avoid `click here`, `more information`, and raw URLs in prose.

Link to the canonical owner of a fact:

- configuration defaults link to configuration reference;
- public members link to generated API reference;
- procedures link to how-to guides;
- architectural explanations link to concepts;
- failures link to troubleshooting.

Use relative links or stable cross-references for internal content.

## Images and diagrams

Use a visual only when it explains a relationship, flow, architecture, state transition, or topology more effectively than text.

Every image or diagram must have:

- meaningful alternative text;
- a source file that can be maintained when practical;
- an explanation in the surrounding text;
- no information conveyed by color alone.

Prefer versionable diagram sources and generated SVG. Use raster images only when necessary.

## Normative language

Use these terms consistently:

- `must` and `must not` for mandatory requirements;
- `should` and `should not` for strong recommendations that may have justified exceptions;
- `may` for explicitly permitted behavior;
- `can` for capability or possibility.

Do not use `should` to describe behavior that Helium guarantees.

## Helium terminology

Use the canonical domain terms consistently.

| Use | Meaning |
| --- | --- |
| account | The authenticated identity managed by Helium. |
| organization | The primary tenant boundary. |
| membership | The relationship between an account and an organization. |
| active organization | The organization selected for the current application context. |
| organization context | The validated organization identity used by scoped behavior. |
| role | What a member may do within an organization. |
| entitlement | What the organization's plan makes available. |
| consuming application | The application that references and uses Helium. |
| framework-owned data | Data whose schema and lifecycle are managed by Helium. |
| consumer-owned data | Product-specific data managed by the consuming application. |

Preserve these distinctions:

- account is not membership;
- authentication is not authorization;
- role is not entitlement;
- organization is the domain term; tenant is an architectural description;
- a public CLR type is not automatically a supported contract.

## Canonical example

Use `Acme Projects` as the recurring application example unless another domain is necessary for the feature.

Recommended names:

- application: `Acme Projects`;
- entity: `Project`;
- organization: `Contoso`;
- account: `alex@example.com`;
- plans: `Free` and `Professional`.

Keep names and behavior consistent across tutorials and related how-to guides.

## Pull-request checklist

Before requesting review, confirm that:

- the page has one dominant content type and objective;
- title and description identify the reader outcome;
- front matter uses allowed values;
- the introduction establishes scope and context;
- terminology follows the glossary and these conventions;
- procedures include prerequisites and verification;
- code samples are valid for the documented version;
- defaults and public behavior are verified against the framework;
- links resolve and point to canonical sources;
- the page does not duplicate another normative source;
- status and version are explicit;
- `last_reviewed` represents an actual technical review;
- the rendered preview has been inspected when layout is affected.

## Related documentation

- [Documentation architecture](documentation-architecture.md)
- [TOC conventions](toc-conventions.md)
- [Metadata reference](metadata-reference.md)
- [Issue and pull-request workflow](issues-and-pull-requests.md)
