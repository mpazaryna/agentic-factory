# Plugin Audit: kairos

**Path**: pm/kairos
**Date**: 2026-03-19
**Skills**: 6 | **Agents**: 1

## Summary
| Severity | Count |
|----------|-------|
| ERROR    | 14    |
| WARN     | 8     |
| INFO     | 2     |
| PASS     | 38    |

## Plugin Structure

| Check | Result | Detail |
|-------|--------|--------|
| P1 | PASS | plugin.json is valid JSON |
| P2 | PASS | name `kairos` is kebab-case |
| P3 | PASS | version `1.1.0` follows semver |
| P4 | PASS | description present (133 chars) |
| P5 | PASS | no nested skills/ or agents/ inside .claude-plugin/ |
| P6 | PASS | CLAUDE.md exists at plugin root |
| P7 | PASS | all directory names use kebab-case |

## Skills

### interstitial (58 lines)

| Check | Result | Detail |
|-------|--------|--------|
| F1 | ERROR | `name` field missing from frontmatter |
| F2 | -- | skipped (no name field) |
| F3 | -- | skipped (no name field) |
| F4 | PASS | description present |
| F5 | WARN | description is 52 chars but lacks "Use when" trigger phrase |
| F6 | ERROR | `allowed-tools` field missing |
| F7 | -- | skipped (no allowed-tools) |
| F8 | PASS | no $ARGUMENTS used, no argument-hint needed |
| F9 | PASS | no context:fork |
| F10 | PASS | no context:fork |
| F11 | WARN | `disable-model-invocation` not set; should be explicitly `false` for plugin skills |
| F12 | PASS | no unknown frontmatter fields |
| C1 | PASS | 58 lines (limit 500) |
| C2 | PASS | no supporting files to reference |
| C3 | PASS | no file path references |
| C4 | PASS | no scripts/ directory |

### kickoff (141 lines)

| Check | Result | Detail |
|-------|--------|--------|
| F1 | ERROR | `name` field missing from frontmatter |
| F2 | -- | skipped (no name field) |
| F3 | -- | skipped (no name field) |
| F4 | PASS | description present |
| F5 | WARN | description is 57 chars but lacks "Use when" trigger phrase |
| F6 | ERROR | `allowed-tools` field missing |
| F7 | -- | skipped (no allowed-tools) |
| F8 | PASS | no $ARGUMENTS used |
| F9 | PASS | no context:fork |
| F10 | PASS | no context:fork |
| F11 | WARN | `disable-model-invocation` not set; should be explicitly `false` for plugin skills |
| F12 | PASS | no unknown frontmatter fields |
| C1 | PASS | 141 lines (limit 500) |
| C2 | PASS | no supporting files to reference |
| C3 | PASS | no file path references needing ${CLAUDE_SKILL_DIR} |
| C4 | PASS | no scripts/ directory |

### review (73 lines)

| Check | Result | Detail |
|-------|--------|--------|
| F1 | ERROR | `name` field missing from frontmatter |
| F2 | -- | skipped (no name field) |
| F3 | -- | skipped (no name field) |
| F4 | PASS | description present |
| F5 | WARN | description is 89 chars, starts with action verb, but lacks "Use when" trigger phrase |
| F6 | ERROR | `allowed-tools` field missing |
| F7 | -- | skipped (no allowed-tools) |
| F8 | PASS | $ARGUMENTS implied by usage pattern ("/review weekly") but not formally declared -- acceptable since description documents it |
| F9 | PASS | no context:fork |
| F10 | PASS | no context:fork |
| F11 | WARN | `disable-model-invocation` not set; should be explicitly `false` for plugin skills |
| F12 | PASS | no unknown frontmatter fields |
| C1 | PASS | 73 lines (limit 500) |
| C2 | WARN | references `weekly.md`, `monthly.md`, `quarterly.md` which exist as siblings but uses bare filenames instead of `${CLAUDE_SKILL_DIR}` paths |
| C3 | WARN | bare relative references (`weekly.md`, `monthly.md`, `quarterly.md`) should use `${CLAUDE_SKILL_DIR}/weekly.md` etc. |
| C4 | PASS | no scripts/ directory |

### shutdown (207 lines)

| Check | Result | Detail |
|-------|--------|--------|
| F1 | ERROR | `name` field missing from frontmatter |
| F2 | -- | skipped (no name field) |
| F3 | -- | skipped (no name field) |
| F4 | PASS | description present |
| F5 | WARN | description is 47 chars (under 50-char minimum), lacks "Use when" trigger phrase |
| F6 | ERROR | `allowed-tools` field missing |
| F7 | -- | skipped (no allowed-tools) |
| F8 | PASS | no $ARGUMENTS used |
| F9 | PASS | no context:fork |
| F10 | PASS | no context:fork |
| F11 | WARN | `disable-model-invocation` not set; should be explicitly `false` for plugin skills |
| F12 | PASS | no unknown frontmatter fields |
| C1 | PASS | 207 lines (limit 500) |
| C2 | PASS | no supporting files to reference |
| C3 | PASS | no file path references needing ${CLAUDE_SKILL_DIR} |
| C4 | PASS | no scripts/ directory |

### weekly-plan (109 lines)

| Check | Result | Detail |
|-------|--------|--------|
| F1 | ERROR | `name` field missing from frontmatter |
| F2 | -- | skipped (no name field) |
| F3 | -- | skipped (no name field) |
| F4 | PASS | description present |
| F5 | INFO | description is 79 chars and starts with action verb, but lacks "Use when" trigger phrase |
| F6 | ERROR | `allowed-tools` field missing |
| F7 | -- | skipped (no allowed-tools) |
| F8 | PASS | no $ARGUMENTS used |
| F9 | PASS | no context:fork |
| F10 | PASS | no context:fork |
| F11 | WARN | `disable-model-invocation` not set; should be explicitly `false` for plugin skills |
| F12 | PASS | no unknown frontmatter fields |
| C1 | PASS | 109 lines (limit 500) |
| C2 | PASS | references `reference.md` which exists in the same directory |
| C3 | INFO | `reference.md` referenced with bare filename; consider `${CLAUDE_SKILL_DIR}/reference.md` |
| C4 | PASS | no scripts/ directory |

### weekly-finalize (29 lines)

| Check | Result | Detail |
|-------|--------|--------|
| F1 | ERROR | `name` field missing from frontmatter |
| F2 | -- | skipped (no name field) |
| F3 | -- | skipped (no name field) |
| F4 | PASS | description present |
| F5 | WARN | description is 73 chars, starts with action verb, but lacks "Use when" trigger phrase |
| F6 | ERROR | `allowed-tools` field missing |
| F7 | -- | skipped (no allowed-tools) |
| F8 | PASS | no $ARGUMENTS used |
| F9 | PASS | no context:fork |
| F10 | PASS | no context:fork |
| F11 | WARN | `disable-model-invocation` not set; should be explicitly `false` for plugin skills |
| F12 | PASS | no unknown frontmatter fields |
| C1 | PASS | 29 lines (limit 500) |
| C2 | PASS | no supporting files to reference |
| C3 | PASS | no file path references needing ${CLAUDE_SKILL_DIR} |
| C4 | PASS | no scripts/ directory |

## Agents

### monk

| Check | Result | Detail |
|-------|--------|--------|
| A1 | PASS | name `monk` present |
| A2 | PASS | name is kebab-case |
| A3 | PASS | description present (174 chars) |
| A4 | PASS | description explains when to delegate ("Use when triggering daily rituals via cron, dispatch, or any non-interactive context") |
| A5 | ERROR | `tools` field missing -- agent has no explicit tool restrictions |
| A6 | PASS | model `sonnet` specified |
| A7 | PASS | markdown body has clear role ("You are the timekeeper") and detailed instructions for both kickoff and shutdown modes |

## Top Issues (by impact)

1. **All 6 skills missing `name` frontmatter field** (ERROR x6) -- Skills cannot be properly registered as slash commands without a `name` field. This is the most fundamental compliance gap.

2. **All 6 skills missing `allowed-tools` field** (ERROR x6) -- Every skill implicitly has full-session tool access. This violates the principle of least privilege and is a security concern.

3. **Monk agent missing `tools` field** (ERROR x1) -- The agent has unrestricted tool access. Given that Monk writes files and runs scripts, it should have an explicit tool allowlist.

4. **No skill has `disable-model-invocation: false` set** (WARN x6) -- While the default behavior may be correct, the field should be explicitly set for clarity and to signal intentional design.

5. **Most descriptions lack "Use when" trigger phrases** (WARN x5) -- Claude cannot effectively pattern-match when to auto-load these skills without explicit trigger descriptions.

## Suggested Fixes

### ERRORs

1. **Add `name` to all skill frontmatter.** Each SKILL.md needs `name: <directory-name>` in the YAML block:
   - `interstitial/SKILL.md` -> `name: interstitial`
   - `kickoff/SKILL.md` -> `name: kickoff`
   - `review/SKILL.md` -> `name: review`
   - `shutdown/SKILL.md` -> `name: shutdown`
   - `weekly-plan/SKILL.md` -> `name: weekly-plan`
   - `weekly-finalize/SKILL.md` -> `name: weekly-finalize`

2. **Add `allowed-tools` to all skill frontmatter.** Suggested minimal sets:
   - `interstitial`: `["Read", "Write", "Bash"]` (reads time, writes note files)
   - `kickoff`: `["Read", "Write", "Bash", "Glob"]` (reads notes/projects, writes daily note, runs clickup-today.sh)
   - `review`: `["Read", "Write", "Bash", "Glob"]` (reads notes/CSVs, writes review files)
   - `shutdown`: `["Read", "Write", "Edit", "Bash", "Glob"]` (reads notes, updates daily note frontmatter, runs git status and clickup-today.sh)
   - `weekly-plan`: `["Read", "Write", "Bash", "Glob"]` (reads score/notes, writes weekly plan, runs calendar and clickup scripts)
   - `weekly-finalize`: `["Read", "Edit", "Bash"]` (reads plan, updates frontmatter, runs clickup-today.sh)

3. **Add `tools` to monk agent.** Suggested: `["Read", "Write", "Edit", "Bash", "Glob"]`

### WARNs

4. **Add `disable-model-invocation: false` to all 6 skills** to make the intent explicit.

5. **Enhance descriptions with "Use when" triggers.** Examples:
   - interstitial: `"Quick-capture a timestamped note to the log folder. Use when the user dictates a thought, observation, or note they want persisted."`
   - kickoff: `"Run morning orientation: surface carry-overs, ClickUp tasks, and daily focus. Use when starting the workday or triggering the morning ritual."`
   - shutdown: `"End-of-day capture: accomplishments, blockers, intensity, tomorrow's frog. Use when closing out the workday or triggering the evening ritual."`
   - review: `"Review at weekly, monthly, or quarterly zoom level. Use when the user asks for a retrospective, review, or period summary."`
   - weekly-plan: `"Generate the start-of-week planning draft with load calculation and project triage. Use when beginning a new work week or requesting a weekly plan."`
   - weekly-finalize: `"Finalize the weekly plan after decisions are acted on in ClickUp. Use when the user has reviewed the weekly draft and is ready to lock it."`

6. **Use `${CLAUDE_SKILL_DIR}` for file references** in review/SKILL.md (`weekly.md`, `monthly.md`, `quarterly.md`) and weekly-plan/SKILL.md (`reference.md`).
