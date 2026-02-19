# How to Use `/validate`

The `/validate` command scores Claude Code components against quality rubrics and produces a detailed scorecard.

## Basic Usage

```bash
/validate <type> <path>
```

Where `<type>` is one of: `skill`, `agent`, `command`, `curated-prompt`
And `<path>` is the path to the component directory.

## Examples

### Validate a Skill

```bash
/validate skill skills/yoga-class-planner
```

Checks for SKILL.md, README.md, HOW_TO_USE.md, valid frontmatter, content quality, and cleanliness.

### Validate an Agent

```bash
/validate agent agents/quality-control-enforcer
```

Checks for proper frontmatter (name, description, color, tools, field), clear purpose statement, workflow steps, and output format.

### Validate a Command

```bash
/validate command commands/gh-issue
```

Checks for frontmatter (description, allowed-tools, argument-hint), numbered steps, output format, and supporting docs.

### Validate a Curated Prompt

```bash
/validate curated-prompt curated-prompts/engineering/market-research
```

Checks for frontmatter (name, description, source, tags), substantive content, and metadata.

### Auto-Detect Type

If you omit the type, the validator infers it from the path:

```bash
/validate skills/yoga-class-planner
/validate agents/research-agent
```

## Understanding the Scorecard

The scorecard shows each category with earned/possible points:

```
VALIDATION REPORT: skill/yoga-class-planner
============================================

Structure (25/25)
  [PASS]  SKILL.md exists
  [PASS]  README.md exists
  [PASS]  HOW_TO_USE.md exists
  [PASS]  Directory name matches YAML name

Frontmatter (15/15)
  [PASS]  Valid YAML frontmatter
  [PASS]  name field present & kebab-case
  [PASS]  description field present

Content Quality (25/35)
  [PASS]  Description is specific
  [PASS]  Has practical examples
  [FAIL]  Documents when to use          (-5)
  [PASS]  Has clear workflow/steps
  [PASS]  References related skills
  [FAIL]  Lists anti-patterns             (-5)

Documentation (15/15)
  [PASS]  README has overview
  [PASS]  HOW_TO_USE has examples
  [PASS]  Sample data present

Cleanliness (10/10)
  [PASS]  No backup/temp files
  [PASS]  No cache artifacts

TOTAL: 90/100  [EXCELLENT]

Rating: 90-100 EXCELLENT | 75-89 GOOD | 60-74 NEEDS WORK | <60 POOR
```

## Rating Scale

| Score | Rating | Meaning |
|-------|--------|---------|
| 90-100 | EXCELLENT | Ready to share/publish |
| 75-89 | GOOD | Solid, minor improvements possible |
| 60-74 | NEEDS WORK | Functional but missing important elements |
| <60 | POOR | Significant gaps, needs rework |

## Common Workflow

```bash
# 1. Build a skill
/build skill

# 2. Validate it
/validate skill skills/my-new-skill

# 3. Fix any issues based on the scorecard

# 4. Re-validate
/validate skill skills/my-new-skill

# 5. Install when satisfied
/install-agentic-factory skill my-new-skill
```

## Tips

- Run validation after every build to catch issues early
- Focus on FAIL items with the highest point values first
- Content quality checks are qualitative — the validator reads your content and judges whether it meets the bar
- A score of 75+ is generally ready for use; aim for 90+ before publishing
