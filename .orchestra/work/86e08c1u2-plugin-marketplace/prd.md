# PRD: The Factory Becomes a Factory

**Version:** 2.0
**Date:** 2026-03-10
**Author:** mpaz
**Status:** Draft
**Parent:** 86e08c1a1 (Component Sharing & Distribution System) — Phase 3

---

## Problem Statement

The factory is organized like a warehouse — components sorted by type (skills/, agents/, commands/) into flat bins. This creates two problems that compound each other:

**1. The structure fights the practice.**

A developer working on product planning needs `ticket-refiner` (agent), `prd-to-spec` (agent), `prd-creator` (command + skill), and `spec-executor` (agent). These live in three different directories. There's no way to install "the product planning practice" — you install individual pieces and hope you got them all. The type-based organization obscures what actually belongs together.

**2. There's no authoring environment.**

To improve a skill, you open the factory repo, navigate to `components/skills/some-skill/`, and edit in isolation. There's no `CLAUDE.md` providing context about what this skill is part of, how it relates to its siblings, what the practice area needs. Every authoring session starts cold. Compare this to claude-skills where each domain folder is a self-contained workspace — `cd engineering-team && claude` puts you in context immediately.

**3. Distribution is disconnected from organization.**

The custom `/factory install` system and Claude Code's native plugin system are parallel, incompatible paths. The factory has 61 components that can only be installed via custom tooling, while 5 plugins sit orphaned in `plugins/`. Meanwhile, the native plugin system offers namespacing, versioning, caching, marketplace support, and team distribution — all unused.

These three problems share a root cause: **the organizing principle is wrong.** Components are grouped by what they are (skill, agent, command) instead of what they do (developer workflow, product planning, Swift development). Fix the organizing principle and all three problems resolve together.

---

## The Insight

The claude-skills repo (alirezarezvani) reveals a pattern where each domain folder is three things simultaneously:

1. **An installable plugin** — `.claude-plugin/plugin.json` with `"skills": "./"` makes the folder distributable via Claude Code's native system
2. **A development workspace** — `CLAUDE.md` at the folder root gives Claude the context to work on, improve, and extend the skills inside
3. **A practice domain** — the folder represents a coherent area of expertise, not an arbitrary grouping of component types

Each folder is a production line. The `CLAUDE.md` is the workbench context. The skills, agents, and commands inside are the products. The `plugin.json` is the packaging. The root `marketplace.json` is the shipping manifest. `/plugin install` is delivery.

**The factory becomes a factory.**

---

## Goals

### User Goals
- Install an entire practice domain in one action: `/plugin install product-planning@agentic-factory`
- Cherry-pick individual components when needed: `/plugin install dev-context@agentic-factory`
- Open any domain folder in Claude Code and immediately have authoring context for improving those components
- Browse the factory by what things do, not what type they are

### Practice Goals
- **Each domain = a specialization I bring to projects.** The factory is the portfolio of my professional toolkit.
- **Composable project setup.** Starting a Swift iOS project? Install `swift-development` + `developer-workflow` + `product-planning`. Each one brings everything needed for that practice area.
- **Compound improvement.** Working inside `developer-workflow/` with its CLAUDE.md means improvements are informed by context — how the skills relate, what's missing, what the conventions are. Not isolated edits in a flat directory.

### Technical Goals
- **One distribution mechanism** — native `/plugin install` replaces custom `/factory install`
- **Zero packaging overhead** — the directory structure IS the plugin structure, no generate step
- **Marketplace-native** — `marketplace.json` at root, installable from GitHub

---

## Non-Goals

- **Not a public marketplace yet** — private repo becomes a marketplace first; public fork is a follow-on
- **Not building a custom CLI** — we leverage Claude Code's built-in `/plugin` commands
- **Not abandoning `/factory` entirely** — `/factory promote` and `/factory rebuild-registry` still have authoring value; the install/update path migrates to native plugins

---

## Architecture

### The Reorganization

**From (warehouse — organized by type):**
```
components/
├── skills/
│   ├── dev-context/
│   ├── dev-explore/
│   ├── swift-lang/
│   ├── writing/
│   └── ... (16 skills)
├── agents/
│   ├── ticket-refiner/
│   ├── prd-to-spec/
│   └── ... (8 agents)
├── commands/
│   ├── git/
│   ├── acb/
│   └── ... (6 commands)
└── domain/
    ├── chiro/
    └── resin/
```

**To (factory — organized by practice):**
```
agentic-factory/
├── .claude-plugin/
│   └── marketplace.json              ← root catalog
├── CLAUDE.md                         ← repo-level guidance
├── .orchestra/                       ← ADRs, devlog, work items
│
├── developer-workflow/                ← PRACTICE DOMAIN
│   ├── .claude-plugin/plugin.json    ← installable plugin
│   ├── CLAUDE.md                     ← authoring workspace context
│   ├── skills/
│   │   ├── dev-context/SKILL.md
│   │   ├── dev-explore/SKILL.md
│   │   ├── dev-inquiry/SKILL.md
│   │   └── dev-reports/SKILL.md
│   ├── agents/
│   │   ├── quality-control-enforcer.md
│   │   └── work-completion-summarizer.md
│   └── commands/
│       └── git.md
│
├── product-planning/                  ← PRACTICE DOMAIN
│   ├── .claude-plugin/plugin.json
│   ├── CLAUDE.md
│   ├── skills/
│   │   └── prd-template-guidance/SKILL.md
│   ├── agents/
│   │   ├── ticket-refiner.md
│   │   ├── prd-to-spec.md
│   │   └── spec-executor.md
│   └── commands/
│       └── prd.md
│
├── codebase-analysis/                 ← PRACTICE DOMAIN
│   ├── .claude-plugin/plugin.json
│   ├── CLAUDE.md
│   ├── skills/
│   │   └── spike-driven-dev/SKILL.md
│   ├── agents/
│   │   ├── convention-auditor.md
│   │   └── research-docs-fetcher.md
│   └── commands/
│       ├── acb.md
│       ├── context-rebuild.md
│       ├── prime-web-dev.md
│       └── playwright.md
│
├── swift-development/                 ← PRACTICE DOMAIN
│   ├── .claude-plugin/plugin.json
│   ├── CLAUDE.md
│   ├── skills/
│   │   ├── swift-lang/SKILL.md
│   │   ├── swift-ui/SKILL.md
│   │   └── swiftui-submission-prep/SKILL.md
│   └── commands/
│       └── (future: xcode commands)
│
├── content-creation/                  ← PRACTICE DOMAIN
│   ├── .claude-plugin/plugin.json
│   ├── CLAUDE.md
│   ├── skills/
│   │   ├── writing/SKILL.md
│   │   ├── compose-guide/SKILL.md
│   │   └── frontend-design/SKILL.md
│   └── agents/
│       └── synthesis-executor.md
│
├── platform-tools/                    ← PRACTICE DOMAIN
│   ├── .claude-plugin/plugin.json
│   ├── CLAUDE.md
│   ├── skills/
│   │   ├── cloudflare/SKILL.md
│   │   ├── fork-terminal/SKILL.md
│   │   ├── goose-recipes/SKILL.md
│   │   └── goose-recipe-analysis/SKILL.md
│   └── commands/
│       └── (future)
│
├── chiro/                             ← CLIENT DOMAIN
│   ├── .claude-plugin/plugin.json
│   ├── CLAUDE.md
│   ├── skills/
│   ├── agents/
│   └── commands/
│
├── chiro-mlx/                         ← CLIENT DOMAIN
│   ├── .claude-plugin/plugin.json
│   ├── CLAUDE.md
│   ├── skills/
│   └── commands/
│
└── resin/                             ← CLIENT DOMAIN
    ├── .claude-plugin/plugin.json
    ├── CLAUDE.md
    ├── skills/
    ├── agents/
    └── commands/
```

### What Each Domain Folder Contains

Every domain folder has three fixed elements:

**`.claude-plugin/plugin.json`** — Makes it an installable plugin. Minimal:
```json
{
  "name": "developer-workflow",
  "description": "Developer workflow practice: context, exploration, inquiry, reporting, quality, git",
  "version": "1.0.0",
  "author": { "name": "mpaz" }
}
```

Claude Code discovers `skills/`, `agents/`, and `commands/` subdirectories automatically. No enumeration needed.

**`CLAUDE.md`** — The authoring workspace. When you `cd developer-workflow && claude`, this provides:
- What this practice domain covers and who it's for
- How the skills/agents/commands relate to each other
- Naming and structural conventions for this domain
- What's working well, what needs improvement
- Roadmap — what components are missing
- Testing and validation guidance

**`skills/`, `agents/`, `commands/`** — Mixed component types, unified by practice. A practice domain can have any combination. The type subdirectories exist because Claude Code's plugin system expects them, but the organizing principle is the domain, not the type.

### Root Marketplace

`.claude-plugin/marketplace.json` at the repo root catalogs all domains:

```json
{
  "name": "agentic-factory",
  "owner": { "name": "mpaz" },
  "metadata": {
    "description": "Practice-domain plugins for Claude Code",
    "version": "1.0.0"
  },
  "plugins": [
    {
      "name": "developer-workflow",
      "source": "./developer-workflow",
      "description": "Developer workflow: context, exploration, inquiry, reporting, quality, git",
      "version": "1.0.0",
      "category": "practice",
      "tags": ["developer", "workflow", "documentation", "git"]
    },
    {
      "name": "product-planning",
      "source": "./product-planning",
      "description": "Product planning: ticket refinement, PRDs, specs, execution",
      "version": "1.0.0",
      "category": "practice",
      "tags": ["product", "planning", "prd", "specs"]
    },
    {
      "name": "swift-development",
      "source": "./swift-development",
      "description": "Swift & SwiftUI development patterns and submission prep",
      "version": "1.0.0",
      "category": "practice",
      "tags": ["swift", "swiftui", "ios", "macos"]
    },
    {
      "name": "codebase-analysis",
      "source": "./codebase-analysis",
      "description": "Codebase analysis, auditing, research, and testing",
      "version": "1.0.0",
      "category": "practice",
      "tags": ["analysis", "auditing", "testing", "research"]
    },
    {
      "name": "content-creation",
      "source": "./content-creation",
      "description": "Writing, composition, frontend design, and synthesis",
      "version": "1.0.0",
      "category": "practice",
      "tags": ["writing", "content", "design", "frontend"]
    },
    {
      "name": "platform-tools",
      "source": "./platform-tools",
      "description": "Platform-specific tools: Cloudflare, Goose, terminal utilities",
      "version": "1.0.0",
      "category": "practice",
      "tags": ["cloudflare", "goose", "terminal", "platform"]
    },
    {
      "name": "chiro",
      "source": "./chiro",
      "description": "Chiro iOS/macOS project domain tools",
      "version": "1.0.0",
      "category": "client",
      "tags": ["chiro", "ios", "domain"]
    },
    {
      "name": "chiro-mlx",
      "source": "./chiro-mlx",
      "description": "Chiro MLX model training pipeline",
      "version": "1.0.0",
      "category": "client",
      "tags": ["chiro", "mlx", "ml", "domain"]
    },
    {
      "name": "resin",
      "source": "./resin",
      "description": "Resin data extraction platform tools",
      "version": "1.0.0",
      "category": "client",
      "tags": ["resin", "extraction", "domain"]
    }
  ]
}
```

Cherry-picking individual skills is also supported — add entries like:
```json
{
  "name": "dev-context",
  "source": "./developer-workflow/skills/dev-context",
  "description": "Context architecture skill for ADRs, design docs, specs",
  "version": "1.0.0",
  "category": "practice"
}
```

### Install Flow

```bash
# One-time: register the factory as a marketplace
/plugin marketplace add mpaz/agentic-factory

# Install by practice domain
/plugin install developer-workflow@agentic-factory
/plugin install product-planning@agentic-factory
/plugin install swift-development@agentic-factory

# Cherry-pick if needed
/plugin install dev-context@agentic-factory

# Update everything
/plugin marketplace update
```

### Authoring Flow

```bash
# Open a practice domain as a workspace
cd developer-workflow
claude

# Claude reads CLAUDE.md, understands the domain context
# "Add a new skill for PR review workflows"
# "The dev-explore skill overlaps with dev-inquiry — should we merge them?"
# "What's missing from this practice area?"
```

### Team Distribution

In any project's `.claude/settings.json`:
```json
{
  "extraKnownMarketplaces": {
    "agentic-factory": {
      "source": { "source": "github", "repo": "mpaz/agentic-factory" }
    }
  },
  "enabledPlugins": {
    "developer-workflow@agentic-factory": true,
    "product-planning@agentic-factory": true,
    "swift-development@agentic-factory": true
  }
}
```

---

## Proposed Practice Domains

### General Practice (6 domains)

| Domain | Components | Description |
|--------|-----------|-------------|
| `developer-workflow` | dev-context, dev-explore, dev-inquiry, dev-reports, quality-control-enforcer, work-completion-summarizer, git | The daily developer loop: understand context, explore code, investigate problems, report work, ensure quality |
| `product-planning` | ticket-refiner, prd-to-spec, spec-executor, prd-creator (command + skill) | From raw ticket to executed spec: refinement, PRD generation, spec writing, execution |
| `codebase-analysis` | acb, context-rebuild, prime-web-dev, playwright, convention-auditor, research-docs-fetcher, spike-driven-dev | Understand, audit, test, and document codebases |
| `swift-development` | swift-lang, swift-ui, swiftui-submission-prep | Swift/SwiftUI patterns, conventions, and App Store submission |
| `content-creation` | writing, compose-guide, frontend-design, synthesis-executor, project-moc-generator | Create content: blog posts, guides, UI design, documentation maps |
| `platform-tools` | cloudflare, fork-terminal, goose-recipes, goose-recipe-analysis, uat-audit | Platform-specific utilities and integrations |

### Client Domains (3 domains, existing)

| Domain | Components | Description |
|--------|-----------|-------------|
| `chiro` | 3 agents, 12 commands, 1 skill | iOS/macOS chiropractic app project |
| `chiro-mlx` | 3 skills, 5 commands | MLX model training pipeline |
| `resin` | 2 agents, 11 commands, 1 skill | Data extraction platform |

### Placement Decisions

| Component | Domain | Rationale |
|-----------|--------|-----------|
| dev-context, dev-explore, dev-inquiry, dev-reports | developer-workflow | Core dev loop family |
| quality-control-enforcer | developer-workflow | Quality is part of the dev loop |
| work-completion-summarizer | developer-workflow | Reporting is part of the dev loop |
| git commands | developer-workflow | Git is the developer's primary tool |
| ticket-refiner, prd-to-spec, spec-executor | product-planning | End-to-end planning pipeline |
| prd-creator (plugin) | product-planning | Migrated from plugins/prd-creator |
| acb, context-rebuild, prime-web-dev | codebase-analysis | Codebase understanding tools |
| convention-auditor | codebase-analysis | Auditing is analysis |
| research-docs-fetcher | codebase-analysis | Research feeds analysis |
| playwright | codebase-analysis | Testing is validation of analysis |
| spike-driven-dev | codebase-analysis | Spikes are focused analysis |
| writing, compose-guide | content-creation | Written content production |
| frontend-design | content-creation | Visual content production |
| synthesis-executor | content-creation | Combines analysis into output |
| project-moc-generator | content-creation | Documentation structure |
| cloudflare | platform-tools | Platform-specific |
| fork-terminal | platform-tools | Terminal utility |
| goose-recipes, goose-recipe-analysis | platform-tools | Platform-specific |
| uat-audit | platform-tools | Testing utility |

---

## CLAUDE.md Per Domain

Each domain's `CLAUDE.md` serves as the authoring workbench. Template structure:

```markdown
# {Domain Name}

## What This Practice Covers
{1-2 sentence description of the practice area}

## Components

### Skills
- **{name}** — {what it does, when it activates}

### Agents
- **{name}** — {what it does, when to delegate to it}

### Commands
- **{name}** — {what it does, how to invoke it}

## How They Work Together
{Describe the workflow — which components feed into which, typical usage sequences}

## Conventions
- {Naming conventions specific to this domain}
- {Output format conventions}
- {Any shared patterns}

## What's Missing
- {Components that should exist but don't yet}
- {Known gaps or weaknesses}

## Authoring Guide
- {How to add a new component to this domain}
- {How to test components work correctly}
- {What to check before considering a component done}
```

---

## Migration Plan

### What Changes

| Before | After |
|--------|-------|
| `components/skills/dev-context/` | `developer-workflow/skills/dev-context/` |
| `components/agents/ticket-refiner/` | `product-planning/agents/ticket-refiner/` |
| `components/commands/acb/` | `codebase-analysis/commands/acb/` |
| `components/domain/chiro/` | `chiro/` |
| `plugins/prd-creator/` | `product-planning/` (contents merged) |
| `registry.yaml` | `marketplace.json` + per-domain `CLAUDE.md` |
| `/factory install dev-context` | `/plugin install developer-workflow@agentic-factory` |

### What Stays

- `/factory promote` — still useful for bringing components from external projects into a domain
- `/factory rebuild-registry` — adapts to regenerate marketplace.json from domain folders
- `.orchestra/` — project meta (ADRs, devlog, work items) unchanged
- Root `CLAUDE.md` — repo-level guidance unchanged

### What Goes

- `components/skills/`, `components/agents/`, `components/commands/` — replaced by domain folders
- `registry.yaml` — replaced by marketplace.json + convention-based discovery
- `plugins/` directory — contents migrate into their practice domains
- `/factory install`, `/factory update`, `/factory check` — replaced by native `/plugin` commands

### Existing Plugins Migration

| Plugin | Destination | Action |
|--------|-------------|--------|
| `prd-creator` | `product-planning/` | Merge commands/ and skills/ into the domain |
| `research-task` | `codebase-analysis/commands/` | Move command, fix README |
| `decide-technical` | `codebase-analysis/commands/` | Move command, fix README |
| `git-start-new` | `developer-workflow/commands/` | Evaluate merge with git commands |
| `hello-world` | Archive or delete | Development example, no longer needed |

---

## Implementation Phases

### Phase 3a: Structure (1-2 sessions)
- Create all 9 domain folders at repo root
- Move components from `components/` into their practice domains
- Create `.claude-plugin/plugin.json` for each domain
- Create `CLAUDE.md` for each domain (start with component inventory, refine over time)
- Create root `.claude-plugin/marketplace.json`
- Migrate existing plugins into their domains

### Phase 3b: Validate (1 session)
- Test `/plugin marketplace add ./` locally
- Test `/plugin install developer-workflow@agentic-factory`
- Test cherry-pick install of individual skill
- Verify Claude Desktop compatibility
- Verify authoring flow: `cd developer-workflow && claude`

### Phase 3c: Cut Over (1 session)
- Remove old `components/` structure
- Update `/factory promote` to target domain folders
- Update `/factory rebuild-registry` to regenerate marketplace.json
- Update root `CLAUDE.md` and repo documentation
- Remove `registry.yaml`

### Phase 3d: Public Distribution (future)
- Create `agentic-factory-public` with `category: "client"` domains excluded
- Publish as public GitHub repo
- Test `/plugin marketplace add mpaz/agentic-factory-public`

---

## Success Metrics

| Metric | Target |
|--------|--------|
| **Install by practice** | Every domain installable via `/plugin install {domain}@agentic-factory` |
| **Authoring context** | Every domain has a CLAUDE.md; `cd domain && claude` works |
| **Zero custom tooling** | Install/update uses native `/plugin` commands only |
| **Complete migration** | All 61 components placed in a practice domain |
| **Marketplace functional** | `/plugin marketplace add` from GitHub works |

---

## Acceptance Criteria

- [ ] All 9 practice domains exist at repo root, each with `.claude-plugin/plugin.json` and `CLAUDE.md`
- [ ] All 61 components are placed in a domain — nothing left in type-based directories
- [ ] Root `.claude-plugin/marketplace.json` references all domains
- [ ] `/plugin marketplace add ./` registers the factory locally
- [ ] `/plugin install developer-workflow@agentic-factory` installs all dev-* skills, agents, and commands
- [ ] `/plugin install dev-context@agentic-factory` cherry-picks a single skill (if marketplace entry exists)
- [ ] `cd developer-workflow && claude` loads CLAUDE.md and provides authoring context
- [ ] Client domains (chiro, resin) are tagged `category: "client"` and filterable for public fork
- [ ] Existing `plugins/prd-creator` content lives in `product-planning/`
- [ ] `/factory promote` updated to target domain folders

---

## Open Questions

1. **~~Domain granularity~~** — **Resolved: keep `platform-tools` as-is for now.** It's a grab bag, but splitting prematurely creates domain sprawl. If a critical mass builds up for a specific platform (e.g., several AWS skills), break it out into its own domain at that point.

2. **Cross-domain components** — `dev-explore` is useful in both developer-workflow and codebase-analysis contexts. Does it live in one and get referenced from the other, or does duplication across domains matter when each is an independent plugin?

3. **~~`factory/` vs repo root~~** — **Resolved: repo root.** Domain folders live at the top level of agentic-factory. The repo IS the factory — no extra nesting needed. Repo-level files (CLAUDE.md, .orchestra/, .claude/) coexist alongside domain folders.

4. **Registry sunset** — Is `registry.yaml` fully replaced by `marketplace.json` + `CLAUDE.md` per domain, or does it still serve a purpose for metadata that marketplace.json doesn't carry (tags, dependencies)?

5. **Version strategy** — All domains start at 1.0.0? Version per-domain independently? Tie to git tags?

---

## References

- Claude Code plugins: https://code.claude.com/docs/en/plugins.md
- Plugin marketplaces: https://code.claude.com/docs/en/plugin-marketplaces.md
- Pattern source: https://github.com/alirezarezvani/claude-skills (folder-level plugin.json, CLAUDE.md per domain, `"skills": "./"` discovery)
- Reference implementation: https://github.com/jeremylongshore/claude-code-plugins-plus-skills (339 plugins, marketplace at scale)
- Parent spec: .orchestra/work/86e08c1a1-optimize-factory/spec.md
- Parent PRD: .orchestra/work/86e08c1a1-optimize-factory/prd.md
