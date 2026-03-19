# Release Plugin Changes

Detect which plugins have changed, bump their versions, sync marketplace.json, and prepare a commit. Run this after making any changes to plugin content.

## Arguments

$ARGUMENTS — optional: plugin name(s) to release, or `--all` to scan everything. If omitted, auto-detect from git diff.

## Workflow

### Step 1: Detect Changed Plugins

If specific plugin names were provided in $ARGUMENTS, use those. If `--all` was specified, scan all plugins. Otherwise, auto-detect:

1. Run `git diff --name-only HEAD` to find uncommitted changes
2. If no uncommitted changes, run `git diff --name-only HEAD~1` to find changes in the last commit
3. Map changed file paths to their parent plugin by checking which plugin directory each file belongs to
4. A plugin directory is any folder containing `.claude-plugin/plugin.json`
5. Ignore changes to `.claude/`, `.claude-plugin/marketplace.json`, `CLAUDE.md` (root), and `README.md` (root)

Report which plugins were detected as changed. If none, stop and say so.

### Step 2: Validate Plugin Structure

For each changed plugin, verify:

1. `.claude-plugin/plugin.json` exists and is valid JSON
2. `plugin.json` contains `name`, `description`, `version`, and `"skills": "./"`
3. `plugin.json` does NOT contain `"agents"` field (invalid — causes install failure)
4. At least one `*/SKILL.md` exists as a direct child directory (not nested under `skills/`)
5. Each SKILL.md has valid YAML frontmatter with `name` and `description`
6. No SKILL.md has `disable-model-invocation: true` (hides skills from slash commands)

Report any validation errors. Ask the user whether to proceed or fix first.

### Step 3: Bump Versions

For each changed plugin:

1. Read the current version from `.claude-plugin/plugin.json`
2. Parse as semver (major.minor.patch)
3. Determine bump type:
   - **patch** (default): bug fixes, description changes, minor tweaks
   - **minor**: new skills added, skills removed, behavioral changes
   - **major**: breaking changes to skill interfaces or plugin structure
4. If unsure, ask the user which bump type to use
5. Update the `version` field in `.claude-plugin/plugin.json`

### Step 4: Sync Marketplace

For each bumped plugin:

1. Find the matching entry in `.claude-plugin/marketplace.json` by plugin `name`
2. Update its `version` to match the new plugin.json version
3. If the plugin is not in marketplace.json, warn the user (it should be added)

### Step 5: Summary and Commit

1. Show a summary table:

| Plugin | Old Version | New Version | Bump Type | Changes |
|--------|-------------|-------------|-----------|---------|

2. Stage all changed files: the plugin content files, plugin.json files, and marketplace.json
3. Create a commit with message format:
   ```
   release: <plugin-1> vX.Y.Z, <plugin-2> vX.Y.Z

   Bumped versions for changed plugins and synced marketplace.
   ```
4. Ask the user if they want to push

## Rules

- NEVER skip the version bump. The plugin cache keys on version — without a bump, consumers get stale copies.
- NEVER add `"agents": "./"` to plugin.json — it's not a valid manifest field.
- Always keep plugin.json and marketplace.json versions in sync.
- If a plugin has structural issues (skills nested under `skills/`, missing `"skills": "./"`), fix them before releasing.
