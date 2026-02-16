# How to Use the Goose Recipe Analysis Skill

## Quick Start

Ask Claude to create analysis recipes:

```
"Create a Goose recipe to analyze this quarterly report"
"Generate an analysis recipe from my spec file"
"Help me build a recipe that compares Q3 and Q4 reports"
```

## What This Skill Does

Creates simplified Goose recipes for analyzing saved documents - no MCP servers, no complex validation, just document analysis and insight generation.

## Core Concept

**Analysis recipes work with saved data, not live sources.**

```
Data Extraction Recipe (goose-recipes)
  ↓ Queries Salesforce/GitHub/APIs
  ↓ Generates report.md
  ↓
Analysis Recipe (goose-recipe-analysis)
  ↓ Reads report.md
  ↓ Generates analysis.md with insights
```

This separation allows:
- Fast re-analysis without re-querying
- Multiple analysis perspectives on same data
- Scriptable, repeatable workflows

## Usage Examples

### Example 1: Analyze a Saved Report

```
User: "Create a recipe to analyze my fundraising report and extract actionable insights"

Claude: I'll create an analysis recipe for your fundraising report.

```yaml
version: "1.0.0"
title: "Fundraising Report Analysis"
description: "Analyze saved fundraising reports and generate actionable recommendations"

parameters:
  - key: input_file
    input_type: file
    requirement: required
    description: "Path to the fundraising report markdown file"

  - key: output_file
    input_type: string
    requirement: optional
    default: "fundraising-analysis.md"
    description: "Path where analysis should be saved"

instructions: |
  # Fundraising Report Analysis

  You are analyzing a saved fundraising report to extract actionable insights.

  ## Input Report
  {{ input_file }}

  ## Analysis Framework

  ### 1. Executive Summary
  - Key metrics and performance indicators
  - Overall fundraising health
  - Critical issues requiring immediate attention

  ### 2. Performance Analysis
  - Donor acquisition and retention trends
  - Gift size distribution
  - Campaign effectiveness

  ### 3. Actionable Intelligence
  - High-priority actions for next 30 days
  - Medium-term strategic recommendations
  - Long-term growth opportunities

  ### 4. Risk Assessment
  - Potential challenges and blockers
  - Mitigation strategies

  ## Output Requirements
  - Executive summary (2-3 paragraphs)
  - Prioritized action items with owners and timelines
  - Specific, measurable recommendations
  - Risk mitigation strategies

  Save the complete analysis to: {{ output_file }}

prompt: "Analyze the fundraising report and generate actionable recommendations."

settings:
  goose_provider: "anthropic"
  goose_model: "claude-sonnet-4-20250514"
  temperature: 0.5
```

Save as: `mill/recipes/fundraising-analysis.yaml`

**Usage:**
```bash
goose run --recipe mill/recipes/fundraising-analysis.yaml \
  --params input_file="reports/q4-2024/fundraising.md" \
  --params output_file="reports/q4-2024/analysis.md"
```
```

### Example 2: Compare Two Reports

```
User: "Create a recipe that compares Q3 and Q4 reports"

Claude: I'll create a comparative analysis recipe.

```yaml
version: "1.0.0"
title: "Quarterly Report Comparison"
description: "Compare two quarterly reports and identify trends"

parameters:
  - key: q3_report
    input_type: file
    requirement: required
    description: "Q3 quarterly report"

  - key: q4_report
    input_type: file
    requirement: required
    description: "Q4 quarterly report"

  - key: output_file
    input_type: string
    requirement: optional
    default: "q3-q4-comparison.md"
    description: "Comparison analysis output"

instructions: |
  # Quarterly Report Comparison

  Compare these two quarterly reports:

  **Q3 Report:**
  {{ q3_report }}

  **Q4 Report:**
  {{ q4_report }}

  ## Analysis Framework

  ### 1. Metric Changes
  - Revenue growth/decline
  - User acquisition trends
  - Customer retention changes

  ### 2. Trend Identification
  - Positive momentum areas
  - Concerning patterns
  - Seasonal factors

  ### 3. Comparative Insights
  - What improved from Q3 to Q4
  - What declined and why
  - Unexpected changes

  ### 4. Forward-Looking Recommendations
  - Actions to maintain positive trends
  - Strategies to address declines
  - Opportunities for Q1

  Save analysis to: {{ output_file }}

prompt: "Compare the Q3 and Q4 reports and provide comprehensive trend analysis."

settings:
  goose_provider: "anthropic"
  goose_model: "claude-sonnet-4-20250514"
```

**Usage:**
```bash
goose run --recipe quarterly-comparison.yaml \
  --params q3_report="reports/2024-q3/summary.md" \
  --params q4_report="reports/2024-q4/summary.md"
```
```

### Example 3: Generate from Spec File

```
User: "Create a recipe from mill/spec/customer-churn-analysis.md"

Claude: I'll read the spec and generate the recipe.

[Reads mill/spec/customer-churn-analysis.md which contains:]
```markdown
---
title: customer-churn-analysis
description: Analyze customer churn data and identify at-risk segments
---

# Customer Churn Analysis

## Workflow
1. Parse churn data
2. Identify patterns
3. Segment at-risk customers
4. Generate retention strategies
```

[Generates recipe based on spec:]

Created `mill/recipes/customer-churn-analysis.yaml`

Also created a convenience runner script:
`scripts/mill/run-customer-churn-analysis.sh`

**Usage:**
```bash
chmod +x scripts/mill/run-customer-churn-analysis.sh
./scripts/mill/run-customer-churn-analysis.sh \
  --input reports/churn-data.csv \
  --output analysis/churn-insights.md
```
```

## Recipe vs goose-recipes Skill

| Feature | goose-recipes | goose-recipe-analysis |
|---------|---------------|---------------------|
| **Purpose** | Query live data | Analyze saved docs |
| **Input** | MCP tools + params | File parameters |
| **Output** | Structured JSON | Markdown analysis |
| **Auth** | MCP server auth | Not needed |
| **Validation** | JSON schema | Simple checks |
| **Use Case** | Data extraction | Insight generation |

## Common Patterns

### Pattern 1: Single File Analysis

```yaml
parameters:
  - key: report_file
    input_type: file
    requirement: required
    description: "Report to analyze"

instructions: |
  Analyze: {{ report_file }}
  Extract insights and recommendations.
```

### Pattern 2: Multi-File Analysis

```yaml
parameters:
  - key: current_report
    input_type: file
    requirement: required

  - key: previous_report
    input_type: file
    requirement: required

instructions: |
  Compare:
  Current: {{ current_report }}
  Previous: {{ previous_report }}
```

### Pattern 3: Time-Aware Analysis

```yaml
instructions: |
  Today's date: $(date +%Y-%m-%d)
  Current quarter: Q$(( ($(date +%-m)-1)/3+1 ))

  Analyze {{ report_file }} with time-sensitive context.
```

### Pattern 4: Data Enrichment

```yaml
parameters:
  - key: base_data
    input_type: file
    requirement: required

  - key: context
    input_type: string
    requirement: optional
    default: ""

instructions: |
  Enrich {{ base_data }} with:
  - Recommendations
  - Risk assessment
  - Action items

  Context: {{ context }}
```

## Shell Script Runners

Claude generates convenient runner scripts:

```bash
#!/bin/bash
# run-analysis.sh

usage() {
  cat <<EOF
Usage: $0 [OPTIONS]

OPTIONS:
  --input FILE   Report to analyze (required)
  --output FILE  Analysis output (default: analysis.md)
  -h, --help     Show help
EOF
}

# Parse args, validate, run goose
goose run --recipe mill/recipes/analysis.yaml \
  --params input_file="$INPUT_FILE" \
  --params output_file="$OUTPUT_FILE"
```

## Best Practices

### Do's ✅

- Specify clear input file formats
- Structure instructions with frameworks
- Define specific output requirements
- Include time context for date-sensitive analysis
- Add data quality validation steps
- Make recommendations actionable

### Don'ts ❌

- Don't query live data sources (use goose-recipes)
- Don't add MCP authentication
- Don't add JSON schema validation (unless truly needed)
- Don't make output too generic
- Don't skip validation steps in framework

## File Organization

```
mill/
├── spec/                    # Analysis specifications
│   └── analysis-spec.md
└── recipes/                 # Generated recipes
    └── analysis-recipe.yaml

scripts/mill/                # Runner scripts
└── run-analysis.sh
```

## Integration Workflow

### Two-Stage Analysis

```bash
# Stage 1: Extract data (goose-recipes)
goose run --recipe extract-fundraising.yaml
# Output: reports/fundraising-data.md

# Stage 2: Analyze data (goose-recipe-analysis)
./scripts/mill/run-fundraising-analysis.sh \
  --input reports/fundraising-data.md \
  --output reports/fundraising-insights.md
```

### Reusable Analysis

```bash
# Generate report once
goose run --recipe extract-sales.yaml
# Output: sales-2024-q4.md

# Analyze multiple ways
goose run --recipe analyze-trends.yaml --params input_file=sales-2024-q4.md
goose run --recipe analyze-segments.yaml --params input_file=sales-2024-q4.md
goose run --recipe analyze-forecasts.yaml --params input_file=sales-2024-q4.md
```

## Common Questions

**Q: When should I use this vs goose-recipes?**
A: Use this for analyzing *saved* data. Use goose-recipes for *querying* live sources.

**Q: Can I add MCP servers?**
A: Technically yes, but defeats the purpose. This skill is for document analysis, not data extraction.

**Q: Do I need JSON schema validation?**
A: Usually no. Analysis recipes output markdown reports, not structured JSON.

**Q: Can I analyze non-markdown files?**
A: Yes! CSV, JSON, any text-based format works with `input_type: file`.

**Q: How do I test a recipe?**
A: Use the `--explain` flag or test with sample data first.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "File not found" | Use absolute paths or check file exists |
| "No output generated" | Ensure instructions specify saving to output_file |
| "Analysis too generic" | Add more specific framework sections |
| "Missing context" | Include date, period, or domain context |

## Related Skills

- **goose-recipes** - Create data extraction recipes
- **code-reviewer** - Review recipe YAML quality

---

Generated by Claude Code Skills Factory
