# Technical Spec: Component Sharing & Distribution System

**PRD:** `PRD-component-sharing.md`
**ClickUp:** [86e08c1a1](https://app.clickup.com/t/86e08c1a1)
**Version:** 2.0
**Date:** 2026-03-08
**Author:** mpaz
**Status:** Draft

---

## 1. Overview

This spec translates the PRD into an implementable design for a component sharing system within the agentic-factory repo. The system enables installing factory components into any project (global or local), promoting components from domain projects back into the factory, and discovering available components — all without consuming context for unused components.

**Core design principle:** No shell scripts in the repo. The entire system is driven by a single globally-installed Claude Code component — the **factory gateway** — that reads the factory registry and handles all operations from within Claude Code sessions.

---

## 2. Architecture Decisions

### 2.1 Bootstrap-First Architecture

The system has one manual step and everything else flows from it:

```
ONE-TIME SETUP
  └─ Manually install factory gateway to ~/.claude/
       ├─ ~/.claude/commands/factory.md    (the /factory command)
       └─ configured with: FACTORY_PATH=~/workspace/agentic-factory

FROM ANY PROJECT, ANY SESSION
  └─ /factory install dev-explore --global
  └─ /factory list
  └─ /factory promote ./my-agent.md
  └─ /factory update
  └─ /factory check
```

**Why this works:**
- The gateway is a single markdown file — zero maintenance burden
- It reads `registry.yaml` from the factory repo at invocation time — always current
- Claude Code handles the "smart" parts (file copying, conflict detection, context separation scanning)
- No executable code in the repo — pure markdown/YAML

### 2.2 Component Type Strategy

Claude Code's loading behavior dictates how each component type should be handled:

| Component Type | Eager Load | Lazy Load | Global Install Safe? | Strategy |
|---------------|------------|-----------|---------------------|----------|
| **Skills** | Descriptions only (~2% budget) | Full content on invocation | Yes | Primary distribution mechanism |
| **Agents** | Metadata (name, description, tools) | Full system prompt on delegation | Yes | Safe for global install |
| **Commands** | Name + description | Full content on invocation | Yes | Treat as skills (merged in recent Claude Code) |
| **Templates** | None (inert files) | Loaded by parent command/skill | Yes | Bundle with parent component |

**Decision:** Skills are the primary packaging mechanism. Commands are treated as skills. Agents install to `agents/`. Templates bundle with their parent component.

### 2.3 Directory Structure

The factory repo organizes components for installability:

```
agentic-factory/
├── registry.yaml                    # Component manifest (single source of truth)
├── components/
│   ├── skills/
│   │   ├── dev-context/
│   │   │   ├── SKILL.md             # Main skill file (installed)
│   │   │   ├── meta.yaml            # Component metadata (not installed)
│   │   │   ├── README.md            # Documentation (not installed)
│   │   │   └── samples/             # Sample data (not installed)
│   │   ├── dev-explore/
│   │   ├── dev-inquiry/
│   │   ├── dev-reports/
│   │   ├── cloudflare/
│   │   ├── frontend-design/
│   │   ├── writing/
│   │   └── ...
│   ├── agents/
│   │   ├── ticket-refiner/
│   │   │   ├── agent.md             # Agent definition (installed)
│   │   │   └── meta.yaml            # Component metadata (not installed)
│   │   ├── quality-control-enforcer/
│   │   ├── research-docs-fetcher/
│   │   ├── spec-executor/
│   │   └── ...
│   ├── commands/
│   │   ├── git/
│   │   │   ├── commit.md            # Command file (installed)
│   │   │   ├── push.md
│   │   │   ├── issue.md
│   │   │   └── meta.yaml
│   │   ├── acb/
│   │   │   ├── acb.md               # Main command
│   │   │   ├── templates/           # Bundled templates (installed together)
│   │   │   │   ├── base.md
│   │   │   │   ├── typescript.md
│   │   │   │   ├── ios-swift.md
│   │   │   │   └── ...
│   │   │   └── meta.yaml
│   │   └── ...
│   └── domain/                      # Domain-specific components
│       ├── chiro/
│       │   ├── skills/
│       │   ├── agents/
│       │   └── commands/
│       ├── resin/
│       └── ...
├── .claude/                         # Factory system (existing)
│   ├── agents/                      # Factory guide agents (existing)
│   ├── commands/                    # Factory commands (existing)
│   └── templates/                   # Factory templates (existing)
├── skills/                          # Legacy location (migrate to components/)
├── agents/                          # Legacy location (migrate to components/)
└── commands/                        # Legacy location (migrate to components/)
```

**Key design choices:**
- `components/` is the new canonical home — separates installable components from factory infrastructure in `.claude/`
- `components/domain/` houses domain-specific components, organized by project — easy to exclude from public fork
- Each component directory contains the installable file(s) plus metadata that stays in the factory
- `meta.yaml` per component holds registry data (scope, dependencies, description) — source of truth for `registry.yaml`

### 2.4 Component Metadata (meta.yaml)

Every component has a `meta.yaml` that drives the registry:

```yaml
name: dev-explore
type: skill                          # skill | agent | command
scope: general                      # general | domain-specific
domain: null                        # null for general; "chiro", "resin", etc. for domain-specific
description: "Explore and understand codebases with documentation"
install_files:
  - SKILL.md                        # Files to copy during install
install_target: skills/dev-explore   # Relative path under .claude/ or ~/.claude/
dependencies: []                     # Other factory components this requires
tags:
  - codebase
  - exploration
  - documentation
source_project: chiro               # Where this was originally built
promoted_date: 2026-03-08
```

For a component with bundled files:

```yaml
name: acb
type: command
scope: general
description: "Codebase analysis with modular templates"
install_files:
  - acb.md
  - templates/base.md
  - templates/typescript.md
  - templates/ios-swift.md
  - templates/android-kotlin.md
  - templates/jest-testing.md
  - templates/mcp-server.md
  - templates/cloudflare-worker.md
install_target: commands/acb
dependencies: []                     # Templates are bundled, not separate components
tags:
  - codebase-analysis
  - multi-tech
```

For a domain-specific component:

```yaml
name: phi-guardian
type: skill
scope: domain-specific
domain: chiro
description: "Prevent PHI leaks for HIPAA compliance in git operations"
install_files:
  - SKILL.md
install_target: skills/phi-guardian
dependencies: []
tags:
  - hipaa
  - compliance
  - healthcare
source_project: chiro-mlx
promoted_date: 2026-03-08
```

### 2.5 Registry (registry.yaml)

A single manifest file at the repo root. Can be manually maintained or regenerated from `meta.yaml` files by the factory gateway:

```yaml
version: 1
generated: 2026-03-08
factory_path: ~/workspace/agentic-factory

components:
  - name: dev-explore
    type: skill
    scope: general
    description: "Explore and understand codebases with documentation"
    path: components/skills/dev-explore
    dependencies: []
    tags: [codebase, exploration, documentation]

  - name: dev-context
    type: skill
    scope: general
    description: "ADRs, design docs, specs, and plans"
    path: components/skills/dev-context
    dependencies: []
    tags: [architecture, adrs, specs]

  # ... all components listed
```

---

## 3. The Factory Gateway

### 3.1 What It Is

A single Claude Code command file installed globally at `~/.claude/commands/factory.md`. This is the only manually installed component — everything else flows through it.

### 3.2 Gateway Design

The gateway command is a markdown file with YAML frontmatter that instructs Claude to:

1. Read `registry.yaml` from the configured factory repo path
2. Parse the user's subcommand and arguments
3. Execute the requested operation using Claude's built-in file tools (Read, Write, Glob, Bash for `cp`/`mkdir`)

```yaml
---
description: "Agentic Factory — install, discover, and manage components from the factory"
---
```

The command body contains instructions for handling each subcommand:

### 3.3 Subcommands

#### `/factory list [--scope <general|domain-specific>] [--type <skill|agent|command>] [--search <query>]`

**Behavior:**
1. Read `registry.yaml` from factory path
2. Filter by scope, type, or search query if provided
3. Display components grouped by type, with name, scope, and description

**Output format:**
```
SKILLS (general)
  dev-context        ADRs, design docs, specs, and plans
  dev-explore        Explore and understand codebases with documentation
  dev-inquiry        Technical investigations, spikes, comparisons, decisions
  dev-reports        Journals, devlogs, status updates from git history
  cloudflare         Cloudflare Workers development patterns
  frontend-design    Production-grade frontend interface design

AGENTS (general)
  quality-control-enforcer   Review and validate work quality
  research-docs-fetcher      Fetch and organize web content into markdown
  spec-executor              Generic spec-based workflow executor

COMMANDS (general)
  git/commit         Conventional Commit, no push
  git/push           Stage, commit, push with governance
  acb                Codebase analysis with modular templates

DOMAIN (chiro)
  mlx                MLX pipeline improvement workflow
  phi-guardian       Prevent PHI leaks for HIPAA compliance
```

#### `/factory install <component-name|--all> [--global|--project] [--scope <general>]`

**Behavior:**
1. Look up component in `registry.yaml`
2. Resolve dependencies — if component A depends on B, install both
3. Determine target directory:
   - `--global` → `~/.claude/<install_target>/`
   - `--project` (default) → `.claude/<install_target>/` in current working directory
4. For each install file:
   - Check if target exists
   - If identical content → skip silently
   - If different content → show diff, ask user to overwrite or skip
   - If new → copy file, creating directories as needed
5. Report what was installed

**Examples:**
```
/factory install dev-explore --global
→ Installed dev-explore to ~/.claude/skills/dev-explore/

/factory install --all --scope general
→ Installed 32 components to .claude/

/factory install acb --project
→ Installed acb (8 files) to .claude/commands/acb/
```

#### `/factory promote <source-path> [--name <name>] [--type <skill|agent|command>] [--scope <general|domain-specific>] [--domain <name>]`

**Behavior:**
1. Read the source component file(s)
2. If interactive (no flags): ask Claude to classify type, scope, and suggest a name
3. Validate factory conventions:
   - Kebab-case naming
   - YAML frontmatter present
   - Required fields (name, description)
4. Context separation check — scan for domain-leak indicators:
   - Hardcoded project-specific paths
   - Named references to specific apps/products/clients
   - Tech stack assumptions not qualified with "if detected"
   - Fixed output paths instead of discoverable ones
   - If violations found: list them, ask user whether to refactor or classify as domain-specific
5. Copy to `components/<type>/<name>/` in the factory repo
6. Generate `meta.yaml`
7. Update `registry.yaml` (or flag for manual update)
8. Report what was promoted and any warnings

#### `/factory check`

**Behavior:**
1. Scan installed components in `~/.claude/` and `.claude/` (current project)
2. Compare against factory `registry.yaml` versions (by content hash or date)
3. Report which installed components are stale (factory has newer version)
4. Suggest: `/factory install <name> --global` to update

#### `/factory update [<component-name>|--all] [--global|--project]`

**Behavior:**
1. Run check logic
2. For stale components, re-install from factory (with conflict prompting)

#### `/factory rebuild-registry`

**Behavior:**
1. Scan all `meta.yaml` files under `components/`
2. Regenerate `registry.yaml`
3. Report component count by type and scope

### 3.4 Gateway Configuration

The gateway needs to know where the factory repo lives. Options:

**Option A (recommended):** Hardcode in the gateway file itself during one-time setup:
```markdown
## Configuration
- Factory repo path: ~/workspace/agentic-factory
```

**Option B:** Environment variable `AGENTIC_FACTORY_PATH`

**Option C:** A config file at `~/.claude/factory-config.yaml`

Option A is simplest — the gateway is a single file you edit once.

### 3.5 Context Cost

The gateway command itself:
- **Eager load**: name + description only (one line in the `/` autocomplete menu)
- **On invocation**: full command content loads into context
- **When not invoked**: zero context cost beyond the description line

This satisfies the PRD requirement: globally installed but unused = zero context cost.

---

## 4. Context Separation Pattern

### 4.1 The Anti-Pattern

```markdown
# clickup-refiner.md (BAD — domain-hardcoded)
You are a ClickUp ticket refiner for the PAB chiropractic app.
When analyzing the codebase, focus on SwiftUI views in Sources/PAB/Views/
and reference ADR-000 for PlatformConfig patterns...
Output PRDs to .orchestra/prds/
```

### 4.2 The Pattern

```markdown
# ticket-refiner.md (GOOD — context-injected)
You are a ticket refiner that converts project management tickets into
formal PRDs by cross-referencing the current codebase.

## Behavior
1. Fetch the ticket content (via ClickUp API, GitHub issue, or provided text)
2. Explore the codebase to understand architecture, conventions, and patterns
3. Reference any ADRs or architectural docs found in the project
4. Produce a PRD following the project's established format

## Context Sources
- Project architecture: discovered from CLAUDE.md, README, and codebase structure
- Conventions: discovered from ADRs, existing docs, and code patterns
- Output location: use the project's established doc structure (or ask)
- Tech stack: inferred from codebase inspection

## What NOT to hardcode
- Project names, app names, or specific product references
- Specific directory paths (discover them)
- Tech stack assumptions (inspect the codebase)
- Output format templates (use project conventions or ask)
```

### 4.3 Context Injection Sources (priority order)

1. **CLAUDE.md** — Project-level instructions that Claude always has in context
2. **Codebase inspection** — Agent explores the repo to discover architecture
3. **Arguments** — User passes context when invoking (`/refine-ticket --ticket CU-123`)
4. **Conventions files** — ADRs, .editorconfig, project-specific config files the agent discovers

### 4.4 Validation During Promote

The `/factory promote` command scans for these domain-leak indicators:

- Hardcoded paths containing project-specific directories
- Named references to specific apps, products, or clients
- Tech stack assumptions not qualified with "if detected" or "when present"
- Fixed output paths instead of discoverable/configurable ones
- References to specific external services (ClickUp task IDs, specific API endpoints)

Violations produce warnings, not blockers — the developer decides whether to refactor or accept as domain-specific.

---

## 5. Public Fork Derivation

### 5.1 Process

The `/factory` command or a manual process generates a clean public copy:

1. Copy entire repo to a target directory
2. Remove `components/domain/` entirely
3. Filter `registry.yaml` to exclude `scope: domain-specific` entries
4. Remove `_audit/` and other working directories
5. Remove any sensitive config (API keys, private paths)
6. Result is ready to push to `agentic-factory-public`

### 5.2 Automation

Initially manual. Can be automated via GitHub Action on the private repo that pushes filtered content to the public fork repo on tag/release.

---

## 6. Migration Plan

### 6.1 Phase 0: Bootstrap (prerequisite)

**Step 1:** Create the factory gateway command file
**Step 2:** Install to `~/.claude/commands/factory.md`
**Step 3:** Verify `/factory list` works from any project

### 6.2 Phase 1: Foundation (ClickUp: 86e08c1tz)

**Step 1: Create directory structure**
```
components/{skills,agents,commands,domain/{chiro,chiro-mlx,resin,yellow-house}}
```

**Step 2: Promote general-purpose components (priority order)**

Batch 1 — Immediate (no refactoring needed):
- dev-context, dev-explore, dev-inquiry, dev-reports (from chiro)
- git/commit, git/push, git/issue (from chiro — consolidate duplicates)
- frontend-design, writing (from pazland-astro)
- spike-driven-dev, project-moc-generator (from yellow-house, chiro-mlx)
- fork-terminal (from resin)

Batch 2 — Light refactoring:
- quality-control-enforcer, research-docs-fetcher, work-completion-summarizer (from yellow-house)
- spec-executor, synthesis-executor (from resin)
- cloudflare, goose-recipes, goose-recipe-analysis (from resin)
- compose-guide, uat-audit (from chiro)

Batch 3 — Context separation refactoring (ClickUp: 86e08c1u4):
- ticket-refiner (from clickup-refiner in chiro + resin)
- prd-to-spec (from spec-writer in chiro + resin)
- convention-auditor (from config-auditor in chiro)

Batch 4 — ACB command + templates:
- acb command + 7 templates (from yellow-house + resin)
- paz/tools/playwright, paz/prime/web_dev (from yellow-house)

**Step 3: Promote domain-specific components**
- Move chiro domain components to `components/domain/chiro/`
- Move resin domain components to `components/domain/resin/`
- Move chiro-mlx domain components to `components/domain/chiro-mlx/`

**Step 4: Build registry**
- Create `meta.yaml` for each promoted component
- Generate initial `registry.yaml`

### 6.3 Phase 2: Install & Discover (ClickUp: 86e08c1u1)

- Implement full `/factory install` logic in the gateway command
- Implement `/factory promote` logic
- Implement `/factory check` and `/factory update`
- Test: bootstrap a fresh project with `/factory install --all --scope general`
- Test: promote a new component from a domain project

### 6.4 Phase 3: Distribution (ClickUp: 86e08c1u2)

- Evaluate npm packaging approach
- Build public fork derivation workflow
- Set up `agentic-factory-public` repo
- Document the system

---

## 7. Acceptance Tests

| # | Test | Expected Result |
|---|------|----------------|
| 1 | `/factory list` from any project | All components displayed grouped by type and scope |
| 2 | `/factory list --scope general --type skill` | Only general-purpose skills shown |
| 3 | `/factory list --search codebase` | Matching components by name, description, or tags |
| 4 | `/factory install dev-explore --global` | SKILL.md copied to `~/.claude/skills/dev-explore/SKILL.md` |
| 5 | `/factory install acb --project` from a new project | acb.md + 7 templates copied to `.claude/commands/acb/` |
| 6 | `/factory install --all --scope general` from a new project | All general components installed to `.claude/` |
| 7 | Start Claude Code after test 6 | Components available; no context warning from `/context` |
| 8 | `/factory install` component A that depends on B | Both A and B installed |
| 9 | `/factory install` when target exists (identical) | Silently skipped |
| 10 | `/factory install` when target exists (different) | Diff shown, user prompted |
| 11 | `/factory promote ~/workspace/proj/.claude/skills/foo` | Component copied to factory, meta.yaml generated, registry updated |
| 12 | `/factory promote` a component with hardcoded domain context | Violations listed, user asked to refactor or classify as domain-specific |
| 13 | `/factory check` with stale installed components | Stale components listed with update suggestion |
| 14 | `/factory update --all --global` | Stale components updated from factory |
| 15 | `/factory rebuild-registry` | registry.yaml regenerated from meta.yaml files |
| 16 | Full bootstrap: new project → `/factory install --all` → use | Toolkit available in <2 minutes, zero context warnings |

---

## 8. Open Items

1. **Symlink vs copy** — Should install create symlinks to the factory repo instead of copies? Pro: always up-to-date, no drift. Con: requires factory repo on disk, breaks if repo moves. Decision: **copy for v1**, evaluate symlinks later.

2. **Uninstall** — `/factory uninstall <name>` — low priority but useful for cleanup.

3. **Gateway self-update** — When the gateway command itself is updated in the factory, the user needs to re-copy it manually. Could add `/factory self-update` that overwrites its own file from the factory repo.

4. **Legacy migration** — Existing `skills/`, `agents/`, `commands/` at repo root need to migrate to `components/`. Plan: migrate in Phase 1, update references.

5. **npm packaging details** — Deferred to Phase 3. The `meta.yaml` format is designed to be convertible to `package.json` fields when needed.

6. **Context budget monitoring** — `/factory install` should warn if installing globally would exceed the ~2% skill description budget (~50+ skills). Could integrate with `/context` check.
