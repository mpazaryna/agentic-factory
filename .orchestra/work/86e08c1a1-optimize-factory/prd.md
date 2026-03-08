# PRD: Component Sharing & Distribution System

**Version:** 1.1
**Date:** 2026-03-08
**Author:** mpaz
**Status:** Ready for Review

---

## Problem Statement

General-purpose agentic components (agents, sub-agents, commands, skills, plugins) are being built inside domain-specific projects and getting trapped there. Across 4+ active Claude Code projects, this leads to duplicated effort — the same patterns are rebuilt per-project instead of being created once and shared. The agentic-factory repo exists as the central factory, but there is no mechanism to install components from it into projects, promote reusable components back into it, or discover what's available. Components are domain-agnostic programming tools that should be available everywhere, but currently require manual copy-paste to move between projects.

---

## Goals

### User Goals
- Start a new project and immediately have all general-purpose agents, commands, and plugins available — no manual copying, no forgetting what exists
- When building something useful in a domain project, have a simple way to promote it to the factory so it's available everywhere
- Know what's available — discover tools across the toolkit without hunting through directories in multiple projects
- Choose to install components at the global level (`~/.claude/`) or project level (`.claude/`), with global as the ideal default — **without paying a context cost for unused components**

### Business Goals
- **Zero duplication** — stop rebuilding the same agent/command patterns across projects
- **Faster project bootstrap** — go from `git init` to productive in minutes, not hours of setup
- **Compound returns** — every component built makes the whole system stronger, not just one project
- **Marketplace-ready structure** — while not designing for multi-user distribution now, the structure should not preclude someone using this repo as a component marketplace in the future

---

## Non-Goals

- **Not a package manager** — no versioning, semver, or dependency resolution; latest-from-factory is the model
- **Not multi-user** — no publishing, sharing with others, or access control
- **Not auto-sync** — no daemon or watcher keeping projects in sync; install and update are explicit actions (auto-sync is an immediate opportunity to fail)
- **Not restructuring what exists** — the current factory layout (skills/, agents/, commands/, .claude/) stays as-is

---

## Key Decisions

### Decision: Private repo with public fork

**Context:** The factory will house both general-purpose and domain-specific components. Domain-specific components may contain sensitive context (medical/HIPAA, client projects) that cannot be public. However, there is value in a public portfolio version for community visibility.

**Decision:** Make `agentic-factory` private. It becomes the single source of truth for all components — general-purpose and domain-specific. A separate public fork (`agentic-factory-public`) will be maintained as a portfolio/showcase version with domain-specific components stripped out.

**Implications:**
- All components (general-purpose + domain-specific) are versioned, backed up, and managed in one place
- No risk of accidental exposure of sensitive domain context
- Domain-specific components need clear tagging/metadata so the public fork can be derived programmatically (or at minimum, easily)
- The install mechanism works against the private repo; the public fork is read-only for community consumption
- Component metadata should include a `scope` field (e.g., `general` vs `domain-specific`) to support automated filtering for the public fork

---

## User Stories

1. **As a developer, I want to install the factory toolkit into a new project, so that all my general-purpose agents, commands, and plugins are immediately available**
2. **As a developer, I want to promote a component I built in a domain project to the factory, so it becomes available across all my projects**
3. **As a developer, I want to see what components the factory offers, so I can discover and use tools I've already built instead of rebuilding them**
4. **As a developer, I want to choose between global and project-level installation, so that components are available where I need them without bloating context when they're not in use**

---

## Requirements

### Functional Requirements

1. **Registry / Catalog** — The factory maintains a manifest of all available components (agents, commands, skills, plugins) with metadata (name, description, type, scope, dependencies). The manifest is queryable without loading full component content. Each component is tagged with a `scope` (`general` or `domain-specific`) to support filtering for the public fork.

2. **Install Mechanism** — A single action installs a component (or set of components) into either `~/.claude/` (global) or `.claude/` (project-level). When a component has dependencies on other factory components, those dependencies are bundled and installed together.

3. **Lazy Loading** — Globally installed components must not consume context until actually invoked. The install mechanism must respect Claude Code's loading behavior and only place components where they will be loaded on-demand, not eagerly.

4. **Promote Workflow** — A workflow to take a component from any project and add it to the factory repo. This includes extracting the component, classifying its scope (general vs domain-specific), ensuring it meets factory conventions (kebab-case naming, proper YAML frontmatter), and registering it in the manifest.

5. **Discovery** — From within any project, a developer can list and search available factory components with descriptions, types, and dependency information — without installing them and without reading all their file contents into context.

6. **Self-Contained Bundles** — Components are installable units with clear boundaries. When installed, a component and its dependencies form a self-contained bundle at the install target. Dependencies are resolved at install time, not at runtime.

7. **Public Fork Derivation** — The factory supports generating a public-safe subset by filtering on component scope. Domain-specific components are excluded from the public fork. This can be manual initially but should support automation.

8. **Context Separation** — Components must not hardcode domain-specific context (project names, architecture details, tech stack assumptions, specific API endpoints, proprietary workflows). General-purpose logic and domain context must be cleanly separated. Domain context should be injected at invocation time via project-level configuration (e.g., CLAUDE.md), arguments, or codebase inspection — not embedded in the component itself. This is a **hard requirement** for any component classified as `general` scope. Components that violate this are flagged during the promote workflow and must be refactored before acceptance.

### Non-Functional Requirements

1. **Pure markdown/YAML compatible** — The registry, manifest, and component metadata work within the existing no-executable-code convention of the repo. A lightweight install script or npm-style CLI is acceptable as an iteration.

2. **Installable unit structure** — The factory repo's directory structure supports treating components as installable units with clear boundaries and metadata.

3. **Future distribution path** — The component structure and manifest format should be compatible with a future `npm install agentic-factory/<component>` style distribution model, even though v1 is local-only.

---

## Success Metrics

| Metric | Target |
|--------|--------|
| **Bootstrap time** | New project has full toolkit available in <2 minutes |
| **Promotion friction** | Promoting a reusable component from a domain project to the factory takes a single command/action |
| **Zero drift** | All active projects use the same version of shared components (no stale copies diverging) |
| **Coverage** | 100% of general-purpose components live in the factory, not scattered across domain projects |
| **Context cost** | Globally installed but unused components add zero tokens to context |

---

## Open Questions

1. **Claude Code loading behavior** — How exactly does Claude Code handle global components in `~/.claude/`? Which component types (agents, commands, skills) load eagerly vs. lazily? This determines what can safely be installed globally.

2. **Manifest format** — Should the manifest be a single file (e.g., `registry.yaml`) or derived from scanning component directories and their frontmatter? Single file is simpler but requires maintenance; scanning is automatic but slower.

3. **npm distribution model** — What would the package structure look like for `npm install agentic-factory/<component>`? Is this a monorepo with workspaces, or individual packages? This is a v2 concern but influences v1 directory structure decisions.

4. **Dependency depth** — How deep can component interdependencies go? Is it A→B only, or can you have A→B→C chains? Deeper chains complicate bundling.

5. **Conflict resolution** — When installing a factory component into a project that already has a local version, what happens? Overwrite? Skip? Warn?

---

## Timeline Considerations

### Phase 1: Foundation
- Audit all active projects (chiro + others) and identify general-purpose components to promote to factory
- Define installable unit structure and manifest format
- Ensure 100% of general-purpose components live in the factory

### Phase 2: Install & Discover
- Build install mechanism (local-first: factory repo → project or global)
- Build discovery/listing capability
- Build promote workflow (domain project → factory)

### Phase 3: Distribution
- Explore npm-style packaging for remote install
- Package factory components for `npm install` distribution
- Document the system for potential community use

---

## Acceptance Criteria

- [ ] A developer can install any factory component into `~/.claude/` (global) or `.claude/` (project) with a single action
- [ ] Installed components do not consume context until invoked
- [ ] A developer can list all available factory components with descriptions without installing them
- [ ] A developer can promote a component from a domain project into the factory repo
- [ ] Interdependent components are bundled correctly — installing component A that references component B brings both
- [ ] The factory repo's directory structure supports treating components as installable units (clear boundaries, metadata)
- [ ] A new project can go from zero to full toolkit in under 2 minutes
- [ ] 100% of general-purpose components live in the factory, not in domain projects

---

## Summary

The agentic-factory repo is a meta-generator for Claude Code components, but it currently lacks a mechanism to distribute those components to projects and collect reusable components back from them. This PRD defines a component sharing system that enables instant project bootstrap, frictionless promotion of reusable tools, and discovery across the toolkit — all without paying a context cost for unused components. The system is designed for a single power user managing multiple projects today, but structured so it could evolve into an npm-style distribution model or community marketplace in the future.

---

## Appendix A: Cross-Project Audit

An audit was conducted across 6 active projects to identify general-purpose components currently trapped in domain-specific repositories. The audit confirms the problem statement: **32 general-purpose components exist across projects, none of which live in the factory.**

### Projects Audited

| Project | Path | Domain | Agents | Commands | Skills |
|---------|------|--------|--------|----------|--------|
| chiro | ~/workspace/chiro | Chiropractic iOS/macOS app | 3 | 16 | 9 |
| chiro-base | ~/workspace/chiro-base | Chiro support tooling | 0 | 0 | 1 |
| chiro-mlx | ~/workspace/chiro-mlx | MLX model training | 0 | 5 | 4 |
| yellow-house-project | ~/workspace/yellow-house-project | Multi-purpose dev | 3 | 8+ | 2 |
| pazland-astro | ~/workspace/pazland-astro | Astro website | 0 | 2 | 3 |
| resin-platform | ~/workspace/joe/resin-platform | Data pipeline platform | 4 | 10 | 5 |

### General-Purpose Components Identified

#### Skills (16 candidates)

| Component | Source | Description | Notes |
|-----------|--------|-------------|-------|
| dev-context | chiro | ADRs, design docs, specs, and plans | Part of dev-* family |
| dev-explore | chiro | Codebase exploration and documentation | Part of dev-* family |
| dev-inquiry | chiro | Technical investigations, spikes, comparisons, decisions | Part of dev-* family |
| dev-reports | chiro | Journals, devlogs, status updates from git history | Part of dev-* family |
| compose-guide | chiro | Compose guides from UAT walkthrough files into handbooks | |
| uat-audit | chiro | Audit and enforce UAT folder structure | |
| swift-lang | chiro | Swift language features reference | Platform-general (any Swift project) |
| swift-ui | chiro | SwiftUI implementation patterns | Platform-general (any SwiftUI project) |
| frontend-design | pazland-astro | Production-grade frontend interface design | |
| writing | pazland-astro | SEO blog posts with structured approval workflow | |
| spike-driven-dev | yellow-house | Spike-driven development with TDD and risk reduction | |
| project-moc-generator | chiro-mlx | Map of Content documentation generation | |
| cloudflare | resin | Cloudflare Workers development patterns | Platform-general (any Workers project) |
| fork-terminal | resin | Fork terminal sessions for agentic coding tools | |
| goose-recipes | resin | Create and validate Goose recipes | |
| goose-recipe-analysis | resin | Goose recipes for document analysis and transformation | |

#### Commands (11 candidates)

| Component | Source | Description | Notes |
|-----------|--------|-------------|-------|
| git/commit (git/cm) | chiro, pazland-astro | Conventional Commit, no push | **Duplicate exists in 3 projects** |
| git/push (git/cp) | chiro, pazland-astro | Stage, commit, push with governance | **Duplicate exists in 3 projects** |
| git/issue | chiro | Fetch GitHub issue for coding agent analysis | |
| paz/acb | yellow-house | Codebase analysis with modular templates | Rich multi-tech analysis tool |
| paz/tools/playwright | yellow-house | Playwright browser automation | |
| paz/prime/web_dev | yellow-house | Web codebase comprehension | |
| paz/learn/acb | yellow-house | Multi-tech codebase analysis with detection | |
| paz/context/* | yellow-house | Documentation rebuild commands | |

#### Agents (5 candidates)

| Component | Source | Description | Notes |
|-----------|--------|-------------|-------|
| quality-control-enforcer | yellow-house | Review and validate work quality, avoid workarounds | |
| research-docs-fetcher | yellow-house | Fetch, process, organize web content into markdown | |
| work-completion-summarizer | yellow-house | Create concise summaries when tasks finish | |
| spec-executor | resin | Generic executor for any spec-based workflow | Spec-agnostic; works with any spec format |
| synthesis-executor | resin | Combine multiple analysis outputs into executive summaries | |

#### Templates (7 candidates)

| Component | Source | Description | Notes |
|-----------|--------|-------------|-------|
| paz/acb/base | resin | Base codebase analysis template | Used by paz/acb command |
| paz/acb/typescript | resin | TypeScript configuration analysis | Used by paz/acb command |
| paz/acb/ios-swift | resin | iOS Swift implementation patterns | Used by paz/acb command |
| paz/acb/android-kotlin | resin | Android Kotlin implementation patterns | Used by paz/acb command |
| paz/acb/jest-testing | resin | Jest testing framework patterns | Used by paz/acb command |
| paz/acb/mcp-server | resin | MCP server implementation patterns | Used by paz/acb command |
| paz/acb/cloudflare-worker | resin | Cloudflare Worker implementation patterns | Used by paz/acb command |

### Domain-Specific Components (remain in projects)

| Domain | Count | Components |
|--------|-------|------------|
| **Chiro/PAB app** | 15 | clickup-refiner, config-auditor, spec-writer, install, refine-ticket, tk-agent, tk-close, tk-investigate, tk-open, uat-audit (cmd), uat-new, uat, write-spec, xcode/*, mlx |
| **Chiro MLX** | 8 | quality-checker, phi-guardian, deployment-helper, train, validate-phi, status, quality-check, deploy-guide |
| **Resin Platform** | 11 | clickup-refiner, spec-writer, extract-agent, extract-worker, mill, refine-ticket, run-agents, run-enrich, run-specs, run-sync, resin |
| **iOS submission** | 1 | swiftui-submission-prep |
| **Presentation** | 1 | build-deck |

### Duplicates & Consolidation Opportunities

| Component Pattern | Instances | Projects | Action |
|-------------------|-----------|----------|--------|
| git commit/push commands | 3 | chiro, pazland-astro, agentic-factory | Consolidate into single factory version |
| clickup-refiner agent | 2 | chiro, resin | Domain-specific forks; extract shared pattern if possible |
| spec-writer agent | 2 | chiro, resin | Domain-specific forks; extract shared pattern if possible |
| refine-ticket command | 2 | chiro, resin | Domain-specific wrappers around clickup-refiner |
| write-spec command | 2 | chiro, resin | Domain-specific wrappers around spec-writer |

### Context Separation Violations

The following components contain hardcoded domain context and require refactoring before (or during) promotion to the factory:

| Component | Source | Violation | Refactoring Needed |
|-----------|--------|-----------|-------------------|
| clickup-refiner | chiro, resin | Hardcodes project architecture (PAB views, Resin workers), specific ADR references, output paths (.orchestra/prds/) | Extract to general "ticket-to-prd" agent; inject project context via CLAUDE.md or arguments |
| spec-writer | chiro, resin | Hardcodes tech stack (SwiftUI/ADRs in chiro, workers/MCP in resin), output structure (.orchestra/work/) | Extract to general "prd-to-spec" agent; project architecture discovered at runtime |
| config-auditor | chiro | Hardcodes PAB's PlatformConfig pattern (ADR-000) | Generalize to "convention-auditor" that reads conventions from project config |
| refine-ticket | chiro, resin | Wrapper around domain-hardcoded clickup-refiner | Will resolve once clickup-refiner is generalized |
| write-spec | chiro, resin | Wrapper around domain-hardcoded spec-writer | Will resolve once spec-writer is generalized |

**Pattern observed:** These components all follow the same anti-pattern — general-purpose logic (fetch ticket → analyze codebase → produce document) with domain context baked into the component file instead of being injected at runtime. This is the highest-priority design problem to solve during implementation.

### Key Findings

1. **32 general-purpose components** are scattered across 6 projects with 0% living in the factory today
2. **The dev-* skill family** (4 skills) is the strongest, most cohesive candidate set — fully general-purpose, well-structured, immediately portable
3. **Git commands** are duplicated in 3 projects with minor variations — the most obvious consolidation win
4. **The paz/ command namespace** from yellow-house contains a rich codebase analysis toolkit (ACB) with 7 tech-specific templates — high-value factory addition
5. **Domain-specific components outnumber general-purpose 36 to 32**, confirming that projects contain a roughly even mix and extraction is worthwhile
6. **Duplicate domain forks** (clickup-refiner, spec-writer) suggest a pattern: some components start general and get domain-specialized — the factory should support this "fork from factory" model
7. **Context separation is the #1 design challenge** — 5 components across 2 projects hardcode domain context into general-purpose logic, creating unmaintainable forks instead of reusable tools
