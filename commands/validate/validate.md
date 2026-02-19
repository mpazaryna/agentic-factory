---
description: Validate and score a Claude Code component (skill, agent, command, curated-prompt) against quality rubrics
argument-hint: <type> <path> (e.g., skill skills/yoga-class-planner)
allowed-tools: Read, Glob, Grep
---

## Your Task

Validate the component specified by `$ARGUMENTS` and produce a quality scorecard.

### Step 1: Parse Arguments

Parse the arguments to determine:
- **Component type**: `skill`, `agent`, `command`, or `curated-prompt` (first word)
- **Component path**: path to the component directory or file (second word)

If only a path is provided (one argument), auto-detect the type:
- Path contains `skills/` → skill
- Path contains `agents/` → agent
- Path contains `commands/` → command
- Path contains `curated-prompts/` → curated-prompt

### Step 2: Gather Component Files

1. Use Glob to find all files in the component path
2. Read the main file (SKILL.md for skills, `<name>.md` for agents/commands, the .md file for prompts)
3. Read all supporting files (README.md, HOW_TO_USE.md, INSTALL.md, etc.)

### Step 3: Evaluate Against Rubric

Score the component using the rubric below for its type. For each check, award full points for PASS or 0 points for FAIL.

#### Skills (100 pts)

**Structure (25 pts):** SKILL.md exists (10), README.md exists (5), HOW_TO_USE.md exists (5), directory name matches YAML `name` (5)

**Frontmatter (15 pts):** Valid YAML (5), `name` present & kebab-case (5), `description` present & non-empty (5)

**Content Quality (35 pts):** Description is specific, not circular (10), has practical examples (5), documents when to use (5), has clear workflow/steps (5), references related skills if applicable (5), lists anti-patterns or limitations (5)

**Documentation (15 pts):** README has overview (5), HOW_TO_USE has invocation examples (5), sample data if applicable (5)

**Cleanliness (10 pts):** No backup/temp files (5), no cache artifacts (5)

#### Agents (100 pts)

**Structure (15 pts):** Main .md file exists (10), file name matches YAML `name` (5)

**Frontmatter (30 pts):** Valid YAML (5), `name` kebab-case (5), `description` triggers auto-discovery (5), `tools` is comma-separated string (5), `color` present (5), `field` present (5)

**Content Quality (35 pts):** Clear role/purpose statement (10), numbered workflow steps (10), output format defined (5), focused purpose (5), safety/constraints noted (5)

**Documentation (10 pts):** When-to-invoke examples (5), related agents referenced (5)

**Cleanliness (10 pts):** No backup/temp files (5), no artifacts (5)

#### Commands (100 pts)

**Structure (15 pts):** Main .md file exists (10), kebab-case name (5)

**Frontmatter (30 pts):** Valid YAML (5), `description` present (5), `allowed-tools` present (5), bash permissions specific not wildcard (10), `argument-hint` if args used (5)

**Content Quality (35 pts):** Has numbered steps (10), uses `$ARGUMENTS` correctly if applicable (5), defines output format (5), has success criteria (5), context gathering section (5), clear single purpose (5)

**Documentation (10 pts):** Supporting docs (README/HOW_TO_USE/INSTALL) (10)

**Cleanliness (10 pts):** No backup/temp files (5), no artifacts (5)

#### Curated Prompts (100 pts)

**Structure (15 pts):** .md file exists (10), kebab-case name (5)

**Frontmatter (25 pts):** Valid YAML (5), `name` present (5), `description` present (5), `source` present (5), `tags` present (5)

**Content Quality (40 pts):** Prompt is substantive (15), has clear use cases (10), includes examples (10), well-structured (5)

**Cleanliness (10 pts):** No backup/temp files (5), no artifacts (5)

**Metadata (10 pts):** `collected` date present (5), tags are relevant (5)

### Step 4: Produce Scorecard

Output the scorecard in this exact format:

```
VALIDATION REPORT: <type>/<name>
============================================

<Category Name> (<earned>/<possible>)
  [PASS]  <check description>
  [FAIL]  <check description>          (-<points>)

...repeat for each category...

TOTAL: <total>/100  [<RATING>]

Rating: 90-100 EXCELLENT | 75-89 GOOD | 60-74 NEEDS WORK | <60 POOR
```

After the scorecard, provide 2-3 sentences of actionable recommendations for the highest-impact improvements.

**Success Criteria:**
- All component files are read and evaluated
- Every check in the rubric is scored as PASS or FAIL
- Scorecard follows the exact format above
- Recommendations are specific and actionable
