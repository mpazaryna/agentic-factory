---
name: Mill Recipe
allowed-tools: Read, Write, Glob, Bash, Edit
description: Decompose and optimize a recipe from mill/recipes/ into agent-ready specs in mill/spec/
---

# Mill Recipe

Reads a recipe from `mill/recipes/` and generates agent-optimized extraction specs in `mill/spec/`.

## Arguments

$ARGUMENTS - The recipe path and optional workflow name:
- **recipe**: Recipe file or folder name in `mill/recipes/` (e.g., "weekly-prioritization-recipe.md" or "fundraising-intelligence")
- **workflow** (optional): Output workflow folder name in `mill/spec/`. Defaults to recipe name without extension. If the workflow already exists, appends `-draft` to protect production specs.

Example: `/mill weekly-prioritization-recipe.md weekly-focus-queue`

## Safety Rule

**NEVER overwrite existing specs in `mill/spec/`.** If the target workflow folder already exists, always write to `{workflow}-draft/` instead. This protects production specs from being replaced by untested output.

## Recipe Shapes

Recipes come in two forms. Detect which one you're working with:

### 1. Monolithic Recipe (single .md file)
Example: `mill/recipes/weekly-prioritization-recipe.md`

This needs full **decomposition** — break the recipe into focused, single-purpose extraction specs.

### 2. Pre-decomposed Recipe (folder of numbered .md files)
Example: `mill/recipes/fundraising-intelligence/*.md`

Joe already split this into specs. Each file needs **optimization** — tighten it for reliable agent execution.

## Decomposition Process (Monolithic Recipes)

1. **Read the recipe** carefully. Identify distinct data extraction concerns.
2. **Break into specs** — each spec should have ONE SOQL concern:
   - One query pattern (e.g., "lapse risk donors" or "pipeline health")
   - Clear filter criteria
   - Explicit output schema
3. **Number specs** sequentially: `01-`, `02-`, etc.
4. **Add synthesis spec** as `99-{workflow}-synthesis.md`
5. **Generate manifest.json**

## Optimization Rules

Each spec must be:

- **Single-purpose** — one SOQL concern per spec. If you're tempted to write "also query X", that's a separate spec.
- **Explicit about output schema** — define the exact JSON structure the LLM should return. Include field names, types, and example values.
- **Clear about Salesforce fields** — list specific field API names (e.g., `npo02__LastCloseDate__c`), not vague references like "giving history."
- **Small enough** — if a spec is more than ~150 lines, it's too big. The LLM will lose focus.
- **Org-agnostic** — never hardcode org-specific thresholds. Use descriptions like "major donor threshold (from org-context)" instead. The extraction worker injects org-context at runtime.

## Spec Frontmatter

Every spec must have this YAML frontmatter:

```yaml
---
title: lapse-risk-candidates
description: Identify donors in the 11-14 month lapse risk window
source_recipe: mill/recipes/weekly-prioritization-recipe.md
sequence: 01
allowed-tools: resin MCP server
---
```

## Manifest Format

Generate a `manifest.json` following this structure:

```json
{
  "version": "1.0",
  "folder": "{workflow-name}",
  "source_recipe": "mill/recipes/{recipe-path}",
  "created_at": "{ISO timestamp}",
  "created_by": "mill",
  "description": "...",
  "specs": [
    {
      "sequence": "01",
      "name": "spec-name",
      "spec_file": "01-spec-name.md",
      "description": "..."
    }
  ],
  "synthesis": {
    "spec_file": "99-{workflow}-synthesis.md",
    "description": "...",
    "input_specs": ["01", "02", "..."],
    "requires_all_specs": false,
    "minimum_specs_required": 3
  }
}
```

## Output

After milling, report:
1. Target folder path (`mill/spec/{workflow}/` or `mill/spec/{workflow}-draft/`)
2. Number of specs generated
3. Whether this is a draft (existing workflow) or new
4. If draft: suggest `diff -r mill/spec/{workflow}/ mill/spec/{workflow}-draft/` to compare

## Example

```
/mill weekly-prioritization-recipe.md weekly-focus-queue

> Recipe: mill/recipes/weekly-prioritization-recipe.md (monolithic)
> Target: mill/spec/weekly-focus-queue-draft/ (existing workflow, using draft)
> Generated 6 extraction specs + synthesis
>
> Compare with production:
>   diff -r mill/spec/weekly-focus-queue/ mill/spec/weekly-focus-queue-draft/
```
