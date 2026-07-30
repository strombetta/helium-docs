---
title: Helium documentation
description: Evaluate the Helium preview and prepare for the future supported reference-application release.
content_type: index
area: product
version: preview
status: preview
last_reviewed: 2026-07-30
_layout: landing
_disableToc: true
_disableAffix: true
_disableBreadcrumb: true
_disableContribution: true
_disableNextArticle: true
---

<div class="helium-home">
  <section class="helium-hero" aria-labelledby="helium-home-title">
    <p class="helium-eyebrow">Development preview for a self-hosted .NET SaaS framework</p>
    <h1 id="helium-home-title">Helium documentation</h1>
    <p class="helium-lead">Evaluate the accepted architecture and implemented foundations for accounts, organizations, authorization, persistence, and durable processing. A supported consumer release and project template are not yet available.</p>
    <div class="helium-actions">
      <a class="btn btn-primary btn-lg" href="articles/overview/index.md">Evaluate the preview</a>
      <a class="btn btn-outline-secondary btn-lg" href="articles/getting-started/prerequisites.md">Check prerequisites</a>
    </div>
    <ul class="helium-hero-facts" aria-label="Helium characteristics">
      <li>Preview</li>
      <li>Self-hosted</li>
      <li>.NET 10</li>
      <li>PostgreSQL 18</li>
    </ul>
  </section>

  <section class="helium-home-section" aria-labelledby="choose-path-heading">
    <div class="helium-section-heading">
      <p class="helium-eyebrow">Choose your path</p>
      <h2 id="choose-path-heading">Start from your current objective</h2>
    </div>
    <div class="helium-card-grid helium-card-grid--paths">
      <a class="helium-card helium-card--featured" href="articles/overview/index.md">
        <span class="helium-card-kicker">Evaluate</span>
        <h3>Evaluate Helium</h3>
        <p>Review the application model, architecture, technology baseline, scope, current workstreams, and operational responsibilities.</p>
        <span class="helium-card-link">Explore the overview <span aria-hidden="true">→</span></span>
      </a>
      <a class="helium-card" href="articles/getting-started/index.md">
        <span class="helium-card-kicker">Prepare</span>
        <h3>Prepare for the reference application</h3>
        <p>Check the .NET and PostgreSQL prerequisites and track availability of the official project template.</p>
        <span class="helium-card-link">Review Get started <span aria-hidden="true">→</span></span>
      </a>
      <a class="helium-card" href="articles/build/index.md">
        <span class="helium-card-kicker">Explore</span>
        <h3>Review capability areas</h3>
        <p>Browse the planned and implemented identity, tenancy, authorization, billing, entitlement, and communications areas.</p>
        <span class="helium-card-link">Browse capability structure <span aria-hidden="true">→</span></span>
      </a>
      <a class="helium-card" href="articles/operate/index.md">
        <span class="helium-card-kicker">Plan</span>
        <h3>Understand operational ownership</h3>
        <p>Review the intended deployment, migration, security, diagnostics, worker, upgrade, and recovery responsibilities.</p>
        <span class="helium-card-link">Review operations structure <span aria-hidden="true">→</span></span>
      </a>
    </div>
  </section>

  <section class="helium-home-section" aria-labelledby="capabilities-heading">
    <div class="helium-section-heading">
      <p class="helium-eyebrow">Target capability model</p>
      <h2 id="capabilities-heading">An integrated SaaS foundation under development</h2>
      <p>Capability completion varies. Review the Overview implementation-status table before treating an area as available.</p>
    </div>
    <div class="helium-card-grid helium-card-grid--compact">
      <a class="helium-card helium-card--compact" href="articles/identity/index.md"><h3>Identity and accounts</h3><p>Registration, verification, authentication, sessions, recovery, and account context.</p></a>
      <a class="helium-card helium-card--compact" href="articles/organizations/index.md"><h3>Organizations and tenancy</h3><p>Organizations, memberships, invitations, roles, ownership, and tenant isolation.</p></a>
      <a class="helium-card helium-card--compact" href="articles/authorization/index.md"><h3>Authorization</h3><p>Organization-scoped context, policies, operations, and protected endpoints.</p></a>
      <a class="helium-card helium-card--compact" href="articles/billing/index.md"><h3>Billing and subscriptions</h3><p>Target Stripe plans, checkout, webhooks, portal, and normalized state.</p></a>
      <a class="helium-card helium-card--compact" href="articles/entitlements/index.md"><h3>Entitlements</h3><p>Target plan capabilities, effective access decisions, and denial reasons.</p></a>
      <a class="helium-card helium-card--compact" href="articles/communications/index.md"><h3>Transactional email</h3><p>Target provider contracts, message types, durable delivery, retries, and diagnostics.</p></a>
    </div>
  </section>

  <section class="helium-home-section helium-home-section--split" aria-labelledby="reference-heading">
    <div>
      <div class="helium-section-heading">
        <p class="helium-eyebrow">Reference</p>
        <h2 id="reference-heading">Inspect current contracts and decisions</h2>
      </div>
      <div class="helium-link-list">
        <a href="api/index.md"><span><strong>.NET API</strong><small>Public contract structure by functional area</small></span><span aria-hidden="true">→</span></a>
        <a href="articles/overview/supported-versions.md"><span><strong>Technology baseline</strong><small>.NET 10 and PostgreSQL 18 compatibility target</small></span><span aria-hidden="true">→</span></a>
        <a href="reference/index.md"><span><strong>Reference catalogs</strong><small>Packages, policies, events, endpoints, compatibility, and glossary</small></span><span aria-hidden="true">→</span></a>
        <a href="articles/overview/scope-and-limitations.md"><span><strong>Limitations</strong><small>Current preview and Initial MVP boundaries</small></span><span aria-hidden="true">→</span></a>
      </div>
    </div>
    <aside class="helium-status-card" aria-labelledby="status-heading">
      <p class="helium-eyebrow">Documentation status</p>
      <h2 id="status-heading">Preview only</h2>
      <p>No supported consumer package release or installable project template is currently documented. Do not use repository build output as a production dependency.</p>
      <a href="articles/overview/index.md">Review current status <span aria-hidden="true">→</span></a>
    </aside>
  </section>

  <section class="helium-home-section helium-contribute-strip" aria-labelledby="contribute-heading">
    <div>
      <p class="helium-eyebrow">Open documentation</p>
      <h2 id="contribute-heading">Improve Helium and its documentation</h2>
      <p>Review the contribution workflow, authoring conventions, source-of-truth rules, and publication process.</p>
    </div>
    <div class="helium-actions">
      <a class="btn btn-outline-primary" href="articles/contributing/index.md">Contribute</a>
      <a class="btn btn-link" href="https://github.com/strombetta/helium-docs">Documentation repository</a>
    </div>
  </section>
</div>