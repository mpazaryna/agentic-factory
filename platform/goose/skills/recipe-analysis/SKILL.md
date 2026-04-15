---
name: recipe-analysis
description: "Create Goose recipes for document analysis and transformation of saved data. Use when analyzing reports, extracting insights from existing files, or enriching documents without querying live sources."
---

# Goose Recipe Analysis

Create Goose recipes for document analysis and transformation — recipes that work with saved data rather than querying live data sources.

## When to Use

- Analyze previously generated reports (markdown, JSON, CSV)
- Transform or enrich existing documents
- Extract insights from saved data
- Generate actionable recommendations from reports

**Do NOT use for**: Live data queries, MCP server access, structured JSON validation — use the `recipes` skill instead.

## Quick Start

```
Use the recipe-analysis skill to create a recipe for mill/spec/your-analysis-spec.md
```

The skill will:
1. Read the markdown spec file
2. Generate a simplified recipe YAML (no MCP auth, no JSON schema)
3. Create a shell script runner
4. Save to `mill/recipes/` and `scripts/mill/`

## Recipe Creation Workflow

### 1. Read the Spec File
Read from `mill/spec/*.md` files describing analysis workflows.

### 2. Extract Key Information
- **Title/Description**: From frontmatter
- **Workflow steps**: The analysis process
- **Output requirements**: What the report should include

### 3. Generate Recipe YAML

```yaml
version: "1.0.0"
title: "Recipe Title from Spec"
description: "Description from spec"

parameters:
  - key: input_file
    input_type: file
    requirement: required
    description: "Path to the report file to analyze"
  - key: output_file
    input_type: string
    requirement: optional
    default: "analysis-output.md"
    description: "Path where analysis should be saved"

instructions: |
  # Analysis Instructions
  You are analyzing a saved report to extract actionable insights.

  ## Input
  {{ input_file }}

  ## Analysis Framework
  [From spec]

  ## Output Requirements
  [From spec]

  Save the analysis to: {{ output_file }}

prompt: "Analyze the report and generate actionable recommendations."
```

### 4. Generate Shell Script Runner

Create a runner script with `--input` and `--output` flags that calls `goose run --recipe`.

## Common Patterns

- **Report Analysis**: Single file → insights and recommendations
- **Multi-File Analysis**: Compare current vs previous period reports
- **Data Enrichment**: Add context or recommendations to existing data
- **Time-Sensitive**: Include `$(date)` for time-aware recommendations

## Key Differences from `recipes` Skill

| Feature | recipes | recipe-analysis |
|---------|---------|-----------------|
| Purpose | Query live data | Analyze saved documents |
| MCP Auth | Yes | No |
| JSON Schema | Yes | No |
| Output | Structured JSON | Markdown analysis |

## Templates

- [assets/analysis-recipe-template.yaml](assets/analysis-recipe-template.yaml)
- [assets/runner-script-template.sh](assets/runner-script-template.sh)
