---
title: Helium documentation
description: Build, extend, deploy, and operate self-hosted SaaS applications with Helium and .NET.
content_type: index
area: product
version: all
status: stable
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
    <p class="helium-eyebrow">Self-hosted SaaS framework for .NET</p>
    <h1 id="helium-home-title">Helium documentation</h1>
    <p class="helium-lead">Build product-specific SaaS features on a maintained foundation for accounts, organizations, authorization, billing, entitlements, email, persistence, and durable processing.</p>
    <div class="helium-actions">
      <a class="btn btn-primary btn-lg" href="articles/getting-started/index.md">Get started</a>
      <a class="btn btn-outline-secondary btn-lg" href="articles/overview/what-is-helium.md">What is Helium?</a>
    </div>
    <ul class="helium-hero-facts" aria-label="Helium characteristics">
      <li>Self-hosted</li>
      <li>Versioned framework</li>
      <li>ASP.NET Core</li>
      <li>PostgreSQL</li>
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
        <p>Review the application model, architecture, scope, support policy, and operational responsibilities.</p>
        <span class="helium-card-link">Explore the overview <span aria-hidden="true">→</span></span>
      </a>
      <a class="helium-card" href="articles/getting-started/index.md">
        <span class="helium-card-kicker">Start</span>
        <h3>Build your first application</h3>
        <p>Create an application, configure PostgreSQL, run migrations, register an account, and complete onboarding.</p>
        <span class="helium-card-link">Follow Get started <span aria-hidden="true">→</span></span>
      </a>
      <a class="helium-card" href="articles/build/index.md">
        <span class="helium-card-kicker">Build</span>
        <h3>Add SaaS capabilities</h3>
        <p>Configure Helium and implement identity, tenancy, authorization, billing, entitlements, and email workflows.</p>
        <span class="helium-card-link">Browse build guides <span aria-hidden="true">→</span></span>
      </a>
      <a class="helium-card" href="articles/operate/index.md">
        <span class="helium-card-kicker">Operate</span>
        <h3>Deploy and operate</h3>
        <p>Prepare production configuration, migrations, security, diagnostics, durable workers, upgrades, and recovery.</p>
        <span class="helium-card-link">Review operations guidance <span aria-hidden="true">→</span></span>
      </a>
    </div>
  </section>

  <section class="helium-home-section" aria-labelledby="capabilities-heading">
    <div class="helium-section-heading">
      <p class="helium-eyebrow">Capabilities</p>
      <h2 id="capabilities-heading">Build on an integrated SaaS foundation</h2>
      <p>Each capability uses shared account, organization, authorization, subscription, and lifecycle concepts.</p>
    </div>
    <div class="helium-card-grid helium-card-grid--compact">
      <a class="helium-card helium-card--compact" href="articles/identity/index.md"><h3>Identity and accounts</h3><p>Registration, verification, sign-in, sessions, recovery, and account context.</p></a>
      <a class="helium-card helium-card--compact" href="articles/organizations/index.md"><h3>Organizations and tenancy</h3><p>Organizations, memberships, invitations, roles, ownership, and tenant isolation.</p></a>
      <a class="helium-card helium-card--compact" href="articles/authorization/index.md"><h3>Authorization</h3><p>Framework policies, organization-scoped decisions, operations, and endpoints.</p></a>
      <a class="helium-card helium-card--compact" href="articles/billing/index.md"><h3>Billing and subscriptions</h3><p>Stripe plans, checkout, webhooks, customer portal, and synchronized state.</p></a>
      <a class="helium-card helium-card--compact" href="articles/entitlements/index.md"><h3>Entitlements</h3><p>Plan capabilities, effective snapshots, denial reasons, and feature protection.</p></a>
      <a class="helium-card helium-card--compact" href="articles/communications/index.md"><h3>Transactional email</h3><p>Provider adapters, message types, templates, delivery, retries, and diagnostics.</p></a>
    </div>
  </section>

  <section class="helium-home-section helium-home-section--split" aria-labelledby="reference-heading">
    <div>
      <div class="helium-section-heading">
        <p class="helium-eyebrow">Reference</p>
        <h2 id="reference-heading">Look up exact contracts and values</h2>
      </div>
      <div class="helium-link-list">
        <a href="api/index.md"><span><strong>.NET API</strong><small>Public contracts by functional area</small></span><span aria-hidden="true">→</span></a>
        <a href="reference/configuration.md"><span><strong>Configuration</strong><small>Keys, defaults, providers, and environment forms</small></span><span aria-hidden="true">→</span></a>
        <a href="reference/index.md"><span><strong>Reference catalogs</strong><small>Packages, policies, events, endpoints, compatibility, and glossary</small></span><span aria-hidden="true">→</span></a>
        <a href="articles/troubleshooting/index.md"><span><strong>Troubleshooting</strong><small>Diagnose symptoms and collect useful evidence</small></span><span aria-hidden="true">→</span></a>
      </div>
    </div>
    <aside class="helium-status-card" aria-labelledby="status-heading">
      <p class="helium-eyebrow">Documentation status</p>
      <h2 id="status-heading">Current and preview guidance</h2>
      <p>Release information, breaking changes, deprecations, support policy, and preview documentation are maintained separately from stable task guidance.</p>
      <a href="articles/whats-new/index.md">Review what’s new <span aria-hidden="true">→</span></a>
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
