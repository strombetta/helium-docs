from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVIEW_DATE = "2026-07-30"


@dataclass(frozen=True)
class Item:
    name: str
    href: str
    items: tuple["Item", ...] = ()


def parse_toc(path: str) -> list[Item]:
    result: list[Item] = []
    name: str | None = None
    href: str | None = None
    for raw in (ROOT / path).read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("- name:"):
            if name is not None and href is not None:
                result.append(Item(name, href))
            name = line.split(":", 1)[1].strip().strip('"')
            href = None
        elif line.startswith("href:"):
            href = line.split(":", 1)[1].strip().strip('"')
    if name is not None and href is not None:
        result.append(Item(name, href))
    if not result:
        raise ValueError(f"No TOC entries found in {path}")
    return result


def prefix(items: list[Item], value: str) -> list[Item]:
    return [Item(item.name, f"{value}{item.href}", item.items) for item in items]


def local_group(directory: str, title: str | None = None) -> Item:
    items = parse_toc(f"articles/{directory}/toc.yml")
    first = items[0]
    return Item(title or first.name, f"{directory}/{first.href}", tuple(prefix(items[1:], f"{directory}/")))


def render_item(item: Item, indent: int = 0) -> list[str]:
    pad = " " * indent
    lines = [
        f"{pad}- name: {json.dumps(item.name, ensure_ascii=False)}",
        f"{pad}  href: {item.href}",
    ]
    if item.items:
        lines.append(f"{pad}  items:")
        for child in item.items:
            lines.extend(render_item(child, indent + 2))
    return lines


def write_tocs() -> None:
    overview_local = parse_toc("articles/overview/toc.yml")
    overview_children = prefix(overview_local[1:], "overview/")
    overview_children.append(local_group("whats-new", "What's new"))

    build_groups = [
        local_group("configuration", "Configure Helium"),
        local_group("identity", "Identity and accounts"),
        local_group("onboarding", "Onboarding"),
        local_group("organizations", "Organizations and tenancy"),
        local_group("authorization", "Authorization"),
        local_group("billing", "Billing and subscriptions"),
        local_group("entitlements", "Entitlements"),
        local_group("communications", "Transactional email"),
        local_group("testing", "Testing"),
    ]

    extensibility_local = parse_toc("articles/extensibility/toc.yml")
    extend_children = prefix(extensibility_local[1:], "extensibility/")
    extend_children.append(local_group("hosting", "ASP.NET Core hosting"))

    operate_groups = [
        local_group("persistence", "Persistence and migrations"),
        local_group("durable-processing", "Durable processing"),
        local_group("deployment", "Deployment"),
        local_group("diagnostics", "Logging and diagnostics"),
        local_group("security", "Security"),
        local_group("performance", "Performance and scalability"),
        local_group("troubleshooting", "Troubleshooting"),
    ]

    reference_local = parse_toc("reference/toc.yml")
    reference_children = prefix(reference_local[1:], "../reference/")
    reference_children.insert(1, Item(".NET API", "../api/"))

    contributing_local = parse_toc("articles/contributing/toc.yml")

    top = [
        Item("Overview", "overview/index.md", tuple(overview_children)),
        local_group("getting-started", "Get started"),
        local_group("fundamentals", "Fundamentals"),
        Item("Build with Helium", "build/index.md", tuple(build_groups)),
        Item("Extend and customize", "extensibility/index.md", tuple(extend_children)),
        Item("Deploy and operate", "operate/index.md", tuple(operate_groups)),
        Item("Reference", "../reference/index.md", tuple(reference_children)),
        Item("Contribute", "contributing/index.md", tuple(prefix(contributing_local[1:], "contributing/"))),
    ]

    lines = ["order: -100", "items:"]
    for item in top:
        lines.extend(render_item(item))
    (ROOT / "articles/toc.yml").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (ROOT / "toc.yml").write_text('items:\n- name: "Documentation"\n  href: articles/\n', encoding="utf-8")


SPECS = [
    ("articles/overview/index.md", "Overview", "Evaluate Helium, understand its supported application model, and review scope, versions, and release information.", "product", "Use this section to determine whether Helium fits your product, architecture, and operating model.", "articles/overview/toc.yml", [("What's new", "../whats-new/index.md"), ("Get started", "../getting-started/index.md")]),
    ("articles/whats-new/index.md", "What's new", "Review current and preview releases, breaking changes, deprecations, release notes, and support policy.", "compatibility", "Use this section to understand release changes and required consumer action.", "articles/whats-new/toc.yml", [("Compatibility matrix", "../../reference/compatibility.md")]),
    ("articles/getting-started/index.md", "Get started", "Create, configure, migrate, run, and complete onboarding for your first Helium application.", "getting-started", "Follow this ordered path to produce a working local application with an account and active organization.", "articles/getting-started/toc.yml", [("Fundamentals", "../fundamentals/index.md"), ("Troubleshooting", "../troubleshooting/index.md")]),
    ("articles/fundamentals/index.md", "Fundamentals", "Understand Helium architecture, domain concepts, public contracts, lifecycle behavior, durable processing, and data ownership.", "architecture", "Use these conceptual topics to build a reliable mental model before combining Helium capabilities.", "articles/fundamentals/toc.yml", [("Build with Helium", "../build/index.md"), ("Reference", "../../reference/index.md")]),
    ("articles/build/index.md", "Build with Helium", "Configure Helium and add identity, onboarding, tenancy, authorization, billing, entitlements, email, and testing capabilities.", "configuration", "Use these capability guides to implement supported SaaS workflows in a consuming application.", None, [("Configure Helium", "../configuration/index.md"), ("Identity and accounts", "../identity/index.md"), ("Onboarding", "../onboarding/index.md"), ("Organizations and tenancy", "../organizations/index.md"), ("Authorization", "../authorization/index.md"), ("Billing and subscriptions", "../billing/index.md"), ("Entitlements", "../entitlements/index.md"), ("Transactional email", "../communications/index.md"), ("Testing", "../testing/index.md")]),
    ("articles/extensibility/index.md", "Extend and customize", "Use supported contracts and extension points to customize providers, policies, hosting, branding, and presentation.", "extensibility", "Use this section when configuration is not sufficient and the application must extend or replace supported behavior.", "articles/extensibility/toc.yml", [("ASP.NET Core hosting", "../hosting/index.md"), ("Compatibility matrix", "../../reference/compatibility.md")]),
    ("articles/operate/index.md", "Deploy and operate", "Prepare Helium for production, manage persistence and durable work, deploy securely, diagnose failures, and plan recovery.", "deployment", "Use these operational guides to move a verified application into a supportable production deployment.", None, [("Persistence and migrations", "../persistence/index.md"), ("Durable processing", "../durable-processing/index.md"), ("Deployment", "../deployment/index.md"), ("Logging and diagnostics", "../diagnostics/index.md"), ("Security", "../security/index.md"), ("Performance and scalability", "../performance/index.md"), ("Troubleshooting", "../troubleshooting/index.md")]),
    ("reference/index.md", "Reference", "Look up Helium packages, .NET APIs, configuration, error codes, policies, events, endpoints, compatibility, and terminology.", "api", "Use reference content when you need exact names, values, identifiers, defaults, compatibility information, or API details.", "reference/toc.yml", [(".NET API", "../api/"), ("Build with Helium", "../articles/build/index.md")]),
    ("articles/configuration/index.md", "Configure Helium", "Register services and configure runtime options, providers, PostgreSQL, authentication, secrets, Stripe, and presentation.", "configuration", "Start here when preparing an application to load and validate Helium configuration.", "articles/configuration/toc.yml", [("Configuration reference", "../../reference/configuration.md")]),
    ("articles/identity/index.md", "Identity and accounts", "Implement registration, verification, sign-in, sessions, recovery, profiles, lifecycle events, and identity security.", "identity", "Use these topics to implement and secure the account lifecycle managed by Helium.", "articles/identity/toc.yml", [("Identity troubleshooting", "../troubleshooting/registration-and-verification.md")]),
    ("articles/onboarding/index.md", "Onboarding", "Understand and customize first-organization onboarding, state transitions, transactional behavior, and completion.", "onboarding", "Use these topics to move a newly registered account into a valid first organization and application context.", "articles/onboarding/toc.yml", [("Organizations and tenancy", "../organizations/index.md")]),
    ("articles/organizations/index.md", "Organizations and tenancy", "Model organizations, memberships, roles, invitations, settings, ownership, active context, and tenant isolation.", "organizations", "Use these topics to implement organization-scoped behavior and preserve tenant boundaries.", "articles/organizations/toc.yml", [("Authorization", "../authorization/index.md")]),
    ("articles/authorization/index.md", "Authorization", "Evaluate authorization policies and protect organization-scoped operations, endpoints, roles, and entitlements.", "authorization", "Use these topics to enforce server-side access decisions against a validated organization context.", "articles/authorization/toc.yml", [("Policy identifiers", "../../reference/authorization-policies.md")]),
    ("articles/billing/index.md", "Billing and subscriptions", "Configure Stripe, define plans, start checkout, process webhooks, synchronize state, and diagnose billing failures.", "billing", "Use these topics to integrate the supported Stripe billing workflow with organization subscriptions.", "articles/billing/toc.yml", [("Entitlements", "../entitlements/index.md")]),
    ("articles/entitlements/index.md", "Entitlements", "Define plan keys, evaluate effective access, interpret denial reasons, and test entitlement-dependent behavior.", "entitlements", "Use entitlements to represent product capabilities and limits made available by an organization's plan.", "articles/entitlements/toc.yml", [("Billing and subscriptions", "../billing/index.md"), ("Authorization", "../authorization/index.md")]),
    ("articles/communications/index.md", "Transactional email", "Configure and implement email providers, message templates, durable delivery, retries, diagnostics, and tests.", "communications", "Use these topics to deliver account, invitation, and billing messages through a supported provider adapter.", "articles/communications/toc.yml", [("Message types", "../../reference/transactional-message-types.md")]),
    ("articles/testing/index.md", "Testing", "Test account and organization context, authorization, entitlements, handlers, providers, migrations, and tenant isolation.", "testing", "Use the testing support and integration guidance to verify successful workflows and security-sensitive negative cases.", "articles/testing/toc.yml", [("Build with Helium", "../build/index.md")]),
    ("articles/hosting/index.md", "ASP.NET Core hosting", "Integrate services, middleware, endpoints, account and organization context, health checks, and reference presentation.", "hosting", "Use these topics to compose Helium correctly inside an ASP.NET Core host.", "articles/hosting/toc.yml", [("Configure Helium", "../configuration/index.md"), ("Deployment", "../deployment/index.md")]),
    ("articles/persistence/index.md", "Persistence and migrations", "Understand schema ownership, PostgreSQL requirements, migrations, migration hosts, upgrades, rollback, and recovery.", "persistence", "Use these topics to operate the framework-owned schema without crossing consumer data boundaries.", "articles/persistence/toc.yml", [("Migration troubleshooting", "../troubleshooting/migrations.md")]),
    ("articles/durable-processing/index.md", "Durable processing", "Operate inbox and outbox work, leasing, retries, idempotency, failed work, graceful shutdown, and recovery.", "durable-processing", "Use these topics to operate background work that must survive process and provider failures.", "articles/durable-processing/toc.yml", [("Worker troubleshooting", "../troubleshooting/durable-workers.md")]),
    ("articles/deployment/index.md", "Deployment", "Build and deploy the container, configure dependencies, apply migrations, verify health, upgrade, and roll back.", "deployment", "Use this section to implement the supported production topology and verify a deployment before serving traffic.", "articles/deployment/toc.yml", [("Security checklist", "../security/deployment-checklist.md")]),
    ("articles/diagnostics/index.md", "Logging and diagnostics", "Use categories, correlation identifiers, health signals, and capability diagnostics without exposing sensitive data.", "diagnostics", "Use these topics to collect evidence and distinguish configuration, provider, and processing failures.", "articles/diagnostics/toc.yml", [("Troubleshooting", "../troubleshooting/index.md")]),
    ("articles/security/index.md", "Security", "Review trust boundaries, tenant isolation, credentials, tokens, cookies, sessions, webhooks, secrets, and logging.", "security", "Use these topics to understand framework security responsibilities and controls the application must preserve.", "articles/security/toc.yml", [("Authorization", "../authorization/index.md")]),
    ("articles/performance/index.md", "Performance and scalability", "Plan database connections, worker concurrency, query indexes, provider latency, processing capacity, and limits.", "performance", "Use these topics to identify capacity constraints and tune a deployment without violating supported behavior.", "articles/performance/toc.yml", [("Deployment", "../deployment/index.md")]),
    ("articles/troubleshooting/index.md", "Troubleshooting", "Diagnose startup, package, database, migration, identity, authorization, email, billing, and worker failures.", "troubleshooting", "Start from the observed symptom, collect evidence, and follow the relevant diagnostic path before changing configuration.", "articles/troubleshooting/toc.yml", [("Logging and diagnostics", "../diagnostics/index.md")]),
]


def page_entries(path: str | None, extra: list[tuple[str, str]]) -> list[Item]:
    entries: list[Item] = []
    if path:
        entries.extend(parse_toc(path)[1:])
    entries.extend(Item(name, href) for name, href in extra)
    seen: set[tuple[str, str]] = set()
    unique: list[Item] = []
    for item in entries:
        key = (item.name, item.href)
        if key not in seen:
            seen.add(key)
            unique.append(item)
    return unique


def render_index(spec: tuple[str, str, str, str, str, str | None, list[tuple[str, str]]]) -> str:
    path, title, description, area, introduction, toc_path, extra = spec
    entries = page_entries(toc_path, extra)
    start = entries[:2]
    lines = [
        "---",
        f"title: {title}",
        f"description: {description}",
        "content_type: index",
        f"area: {area}",
        "version: all",
        "status: stable",
        f"last_reviewed: {REVIEW_DATE}",
        "---",
        "",
        f"# {title}",
        "",
        introduction,
        "",
        "## Start here",
        "",
    ]
    for index, item in enumerate(start):
        reason = "Begin with this topic to establish the primary model or workflow." if index == 0 else "Continue with this topic for the next core decision or task."
        lines.append(f"- [{item.name}]({item.href}) — {reason}")
    lines.extend(["", "## All topics", ""])
    lines.extend(f"- [{item.name}]({item.href})" for item in entries)
    return "\n".join(lines) + "\n"


def write_indexes() -> list[str]:
    managed: list[str] = []
    for spec in SPECS:
        path = ROOT / spec[0]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_index(spec), encoding="utf-8")
        managed.append(spec[0])
    return managed


def update_managed(paths: list[str]) -> None:
    target = ROOT / ".authoring/managed-files.txt"
    lines = target.read_text(encoding="utf-8").splitlines()
    comments = [line for line in lines if not line.strip() or line.lstrip().startswith("#")]
    current = {line.strip() for line in lines if line.strip() and not line.lstrip().startswith("#")}
    current.update(paths)
    text = "\n".join(comments).rstrip() + "\n\n" + "\n".join(sorted(current)) + "\n"
    target.write_text(text, encoding="utf-8")


def main() -> int:
    write_tocs()
    update_managed(write_indexes())
    subprocess.run(["python3", "scripts/generate_content_inventory.py"], cwd=ROOT, check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
