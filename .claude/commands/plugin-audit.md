# Plugin Audit

Validate all plugins in the marketplace for structural correctness, manifest compliance, and readiness for consumer installation.

## Arguments

$ARGUMENTS — optional: specific plugin name or path. If omitted, audit all plugins.

## Workflow

### Phase 1: Discovery

1. Read `.claude-plugin/marketplace.json` to get the list of all plugins
2. For each plugin, resolve the `source` path to its directory
3. Build an inventory: plugin name, path, version, skill count, agent count

### Phase 2: Manifest Validation

For each plugin, check `.claude-plugin/plugin.json`:

| Check | Severity | Rule |
|-------|----------|------|
| Valid JSON | ERROR | Must parse without errors |
| `name` present | ERROR | Required field |
| `description` present | ERROR | Required field |
| `version` present | ERROR | Must be valid semver (X.Y.Z) |
| `"skills": "./"` present | ERROR | Required for skill discovery |
| No `"agents"` field | ERROR | Invalid field — causes install failure |
| `author` present | WARN | Recommended for attribution |
| Version matches marketplace | ERROR | plugin.json and marketplace.json must agree |

### Phase 3: Structure Validation

For each plugin directory:

| Check | Severity | Rule |
|-------|----------|------|
| No `skills/` subdirectory | ERROR | Skills must be direct children, not nested |
| No `agents/` subdirectory | WARN | Agents should be direct children |
| At least one `*/SKILL.md` | WARN | Plugin should contain skills (unless agents-only) |
| CLAUDE.md exists | WARN | Authoring context recommended |

### Phase 4: Skill Validation

For each `*/SKILL.md` found:

| Check | Severity | Rule |
|-------|----------|------|
| Valid YAML frontmatter | ERROR | Must have `---` delimited frontmatter |
| `name` field present | ERROR | Required, must be kebab-case |
| `name` matches directory | ERROR | Skill dir name must match frontmatter name |
| `description` present | ERROR | Required, ≥50 chars |
| Description has trigger | WARN | Should contain "Use when" or similar |
| `allowed-tools` present | WARN | Explicit tool restrictions recommended |
| `disable-model-invocation` not `true` | ERROR | Hides skill from slash commands in consumer projects |
| File ≤500 lines | WARN | Move reference material to supporting files |

### Phase 5: Cross-Reference

1. Every plugin in marketplace.json has a corresponding directory with plugin.json
2. Every plugin directory with plugin.json has a marketplace.json entry
3. No orphaned plugins (in marketplace but directory missing, or vice versa)

### Phase 6: Report

Generate a summary:

```
Plugin Audit Report
═══════════════════

Plugins scanned: X
Skills found: Y
Agents found: Z

ERRORS: N
WARNINGS: N

[Details per plugin]
```

If any ERRORs found, list them with fix instructions. If clean, report "All plugins ready for distribution."
