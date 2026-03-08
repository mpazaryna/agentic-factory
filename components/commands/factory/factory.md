---
description: "Agentic Factory — install, discover, promote, and manage components from the factory toolkit"
---

# Agentic Factory Gateway

You are the factory gateway — the single entry point for managing reusable Claude Code components (skills, agents, commands) across projects.

## Configuration

- **Factory repo path:** ~/workspace/agentic-factory
- **Registry file:** registry.yaml (in factory repo root)

## Subcommands

Parse `$ARGUMENTS` to determine which subcommand to run. The format is:

```
/factory <subcommand> [args...]
```

Supported subcommands: `list`, `install`, `promote`, `check`, `update`, `rebuild-registry`, `help`

If no subcommand is given, or an unknown subcommand is used, show the help.

---

## help

Show this summary:

```
Agentic Factory — component management

Usage:
  /factory list [--scope general|domain-specific] [--type skill|agent|command] [--search <query>]
  /factory install <name|--all> [--global|--project] [--scope general]
  /factory promote <source-path> [--name <name>] [--type <type>] [--scope <scope>]
  /factory check [--global|--project]
  /factory update [<name>|--all] [--global|--project]
  /factory rebuild-registry

Factory repo: ~/workspace/agentic-factory
```

---

## list

**Purpose:** Show available components from the factory registry.

**Steps:**
1. Read `~/workspace/agentic-factory/registry.yaml`
2. Parse the components list
3. Apply filters from arguments:
   - `--scope general` or `--scope domain-specific` — filter by scope
   - `--type skill`, `--type agent`, or `--type command` — filter by type
   - `--search <query>` — match against name, description, or tags
4. Display grouped by type, then by scope:

```
SKILLS (general) — N components
  name                description
  name                description

AGENTS (general) — N components
  name                description

COMMANDS (general) — N components
  name                description

DOMAIN: domain-name — N components
  name    type    description
```

Use fixed-width alignment for readability. If no filters are provided, show everything.

---

## install

**Purpose:** Copy factory components into the current project or global Claude config.

**Arguments:**
- `<name>` — install a specific component by name
- `--all` — install all components (combine with `--scope general` to skip domain-specific)
- `--global` — install to `~/.claude/` (default for single components)
- `--project` — install to `.claude/` in the current working directory
- `--scope general` — when used with `--all`, only install general-purpose components

**Steps:**

1. Read `~/workspace/agentic-factory/registry.yaml`
2. Find the component(s) to install
3. If the component is not found, say so and suggest running `/factory list --search <query>`
4. Resolve dependencies — if the component has dependencies, include them in the install
5. Determine the target base directory:
   - `--global` → `~/.claude/`
   - `--project` → `.claude/` (relative to current working directory)
   - Default: `--global` for single components, `--project` for `--all`
6. For each component:
   a. Read the component's `meta.yaml` from the factory to get `install_files` and `install_target`
   b. Determine the full target path: `<base>/<install_target>/`
   c. For each file in `install_files`:
      - Source: `~/workspace/agentic-factory/<component-path>/<file>`
      - Target: `<base>/<install_target>/<file>`
      - If target file exists:
        - Read both files and compare content
        - If identical: skip silently
        - If different: show the user a brief diff summary and ask whether to overwrite or skip
      - If target does not exist: create directories with `mkdir -p` and copy the file
7. Report what was installed:

```
Installed N components to [~/.claude/ | .claude/]:
  ✓ dev-explore        → skills/dev-explore/
  ✓ dev-context        → skills/dev-context/
  ✓ git                → commands/git/
  - writing            → skills/writing/ (skipped, already identical)
```

**Context budget warning:** If installing more than 40 skills globally, warn the user:
> "You're installing N skills globally. Claude Code loads skill descriptions at startup (~2% context budget). Consider installing less-used skills at the project level instead."

---

## promote

**Purpose:** Copy a component from the current project into the factory repo.

**Arguments:**
- `<source-path>` — path to the component file or directory (e.g., `.claude/skills/my-skill/` or `.claude/agents/my-agent.md`)
- `--name <name>` — component name (inferred from directory/file name if not provided)
- `--type <skill|agent|command>` — component type (inferred from path if not provided)
- `--scope <general|domain-specific>` — defaults to `general`
- `--domain <name>` — required if scope is `domain-specific`

**Steps:**

1. Read the source file(s)
2. Infer name and type from the path if not provided:
   - Path contains `/skills/` → type is skill
   - Path contains `/agents/` → type is agent
   - Path contains `/commands/` → type is command
   - Directory or file name → component name (converted to kebab-case)
3. Validate factory conventions:
   - Name is kebab-case
   - YAML frontmatter is present (for .md files)
   - Required fields exist (name, description)
4. **Context separation check** — scan the component content for domain-leak indicators:
   - Hardcoded directory paths that look project-specific (e.g., `native/pab/`, `workers/extraction/`)
   - Named references to specific apps, products, or clients
   - Tech stack assumptions without "if detected" or "when present" qualifiers
   - Fixed output paths (e.g., `.orchestra/prds/`) without discovery logic
   - Specific API endpoints, service names, or tenant references

   If violations are found, list them and ask:
   > "I found N potential domain-specific references. Options:
   > 1. Refactor them out (I can suggest changes)
   > 2. Classify this component as domain-specific instead
   > 3. Proceed anyway (you'll fix it later)"

5. Determine destination:
   - General: `~/workspace/agentic-factory/components/<type>s/<name>/`
   - Domain-specific: `~/workspace/agentic-factory/components/domain/<domain>/<type>s/<name>/`
6. Copy files to destination
7. Generate `meta.yaml` in the destination:
   ```yaml
   name: <name>
   type: <type>
   scope: <scope>
   domain: <domain or null>
   description: "<from frontmatter>"
   install_files:
     - <list of files, excluding meta.yaml and README.md>
   install_target: <type>s/<name>
   dependencies: []
   tags: []
   source_project: <inferred from current directory name>
   promoted_date: <today>
   ```
8. Remind the user to run `/factory rebuild-registry` to update the manifest
9. Report:

```
Promoted: <name> (<type>, <scope>)
  → ~/workspace/agentic-factory/components/<type>s/<name>/
  Files: <list>

  Run `/factory rebuild-registry` to update the manifest.
```

---

## check

**Purpose:** Compare installed components against the factory to find stale copies.

**Arguments:**
- `--global` — check `~/.claude/` (default)
- `--project` — check `.claude/` in current working directory
- No argument — check both

**Steps:**

1. Read `~/workspace/agentic-factory/registry.yaml`
2. For each component in the registry:
   a. Check if it's installed at the target location (global and/or project)
   b. If installed, compare each `install_file` content against the factory source
   c. Classify as: up-to-date, stale (factory is newer/different), or not installed
3. Report:

```
Component Status ([global|project|both]):

  Up to date (N):
    ✓ dev-explore
    ✓ git

  Stale (N) — factory has changes:
    ⚠ ticket-refiner    (installed differs from factory)
    ⚠ writing           (installed differs from factory)

  Not installed (N):
    · convention-auditor
    · prd-to-spec

Run `/factory update <name>` or `/factory update --all` to refresh stale components.
```

---

## update

**Purpose:** Re-install stale components from the factory.

**Arguments:**
- `<name>` — update a specific component
- `--all` — update all stale components
- `--global` / `--project` — target location (same defaults as install)

**Steps:**

1. Run the `check` logic to identify stale components
2. If a specific name is given, update just that one
3. If `--all`, update all stale components
4. For each component to update:
   - Show what changed (brief diff summary)
   - Copy factory version to installed location (overwrite)
5. Report what was updated

---

## rebuild-registry

**Purpose:** Regenerate `registry.yaml` from all `meta.yaml` files in the factory.

**Steps:**

1. Find all `meta.yaml` files under `~/workspace/agentic-factory/components/`
2. Read each one
3. Build the registry structure grouped by:
   - Skills (general)
   - Agents (general)
   - Commands (general)
   - Domain-specific (grouped by domain)
4. Write to `~/workspace/agentic-factory/registry.yaml`
5. Report:

```
Registry rebuilt: N components
  Skills (general): N
  Agents (general): N
  Commands (general): N
  Domain-specific: N (across M domains)
```
