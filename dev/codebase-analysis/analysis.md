# Plugin Audit: codebase-analysis

**Path**: ./dev/codebase-analysis
**Date**: 2026-03-19
**Skills**: 8 | **Agents**: 2

## Summary

| Severity | Count |
|----------|-------|
| ERROR    | 0     |
| WARN     | 10    |
| INFO     | 0     |
| PASS     | 79    |

## Plugin Structure

- P1: PASS — plugin.json valid
- P2: PASS — plugin.json has name (`codebase-analysis`, kebab-case)
- P3: PASS — plugin.json has version (`1.0.0`, semver)
- P4: PASS — plugin.json has description
- P5: PASS — no nested components in `.claude-plugin/`
- P6: PASS — CLAUDE.md exists at plugin root
- P7: PASS — all skill/agent names use kebab-case throughout

## Skills

### acb
- F1: PASS — name exists (`acb`)
- F2: PASS — name format (kebab-case, 3 chars)
- F3: PASS — name matches directory
- F4: PASS — description exists
- F5: PASS — description quality (190 chars, starts with "Analyze", contains "Use when")
- F6: PASS — allowed-tools explicit (`Bash, Read, Write`)
- F7: PASS — tools match usage (Bash for scanning, Read for templates, Write for output)
- F8: PASS — argument-hint present (`<folder-path>`)
- F11: PASS — side-effects guarded (`disable-model-invocation: true`)
- F12: PASS — no unknown fields
- C1: PASS — 69 lines
- C2: PASS — templates/ referenced via `${CLAUDE_SKILL_DIR}/templates/`
- C3: PASS — uses `${CLAUDE_SKILL_DIR}` for skill-local paths

### playwright
- F1: PASS — name exists (`playwright`)
- F2: PASS — name format (kebab-case, 10 chars)
- F3: PASS — name matches directory
- F4: PASS — description exists
- F5: WARN — description starts with "Playwright" (noun), not an action verb. Consider: "Generate Playwright E2E tests by exploring websites..."
- F6: WARN — `allowed-tools` missing. Skill relies on Playwright MCP tools, Bash (for test execution), and Write (for saving tests). Should declare explicitly.
- F11: WARN — skill saves test files and executes them (side effects) but lacks `disable-model-invocation: true`
- F12: PASS — no unknown fields
- C1: PASS — 18 lines

### prime-web-dev
- F1: PASS — name exists (`prime-web-dev`)
- F2: PASS — name format (kebab-case, 13 chars)
- F3: PASS — name matches directory
- F4: PASS — description exists
- F5: WARN — description starts with "Quick-start" (adjective/noun), not an action verb. Consider: "Scan a web codebase quickly — runs git ls-files, reads README and CONTEXT..."
- F6: WARN — `allowed-tools` missing. Skill uses Bash (`git ls-files`) and Read. Should declare explicitly.
- F11: PASS — no write side effects (read-only analysis)
- F12: PASS — no unknown fields
- C1: PASS — 22 lines

### rebuild-context
- F1: PASS — name exists (`rebuild-context`)
- F2: PASS — name format (kebab-case, 15 chars)
- F3: PASS — name matches directory
- F4: PASS — description exists
- F5: PASS — description quality (155 chars, starts with "Update", contains "Use when")
- F6: PASS — allowed-tools explicit (`Bash, Read, Write`)
- F7: PASS — tools match usage
- F8: PASS — argument-hint present (`<folder-path>`)
- F11: PASS — side-effects guarded (`disable-model-invocation: true`)
- F12: PASS — no unknown fields
- C1: PASS — 47 lines

### rebuild-readme
- F1: PASS — name exists (`rebuild-readme`)
- F2: PASS — name format (kebab-case, 14 chars)
- F3: PASS — name matches directory
- F4: PASS — description exists
- F5: PASS — description quality (168 chars, starts with "Generate", contains "Use when")
- F6: PASS — allowed-tools explicit (`Bash, Read, Write`)
- F7: PASS — tools match usage
- F8: PASS — argument-hint present (`<folder-path>`)
- F11: PASS — side-effects guarded (`disable-model-invocation: true`)
- F12: PASS — no unknown fields
- C1: PASS — 33 lines

### research-task
- F1: PASS — name exists (`research-task`)
- F2: PASS — name format (kebab-case, 13 chars)
- F3: PASS — name matches directory
- F4: PASS — description exists
- F5: PASS — description quality (180 chars, starts with "Perform", contains "Use when")
- F6: PASS — allowed-tools explicit (`WebFetch, WebSearch, Read, Bash`)
- F7: PASS — tools match usage
- F8: WARN — uses `$ARGUMENTS` but no `argument-hint`. Add `argument-hint: "<research topic or question>"`
- F9: PASS — context:fork has actionable research workflow
- F10: PASS — agent specified (`general-purpose`)
- F12: PASS — no unknown fields
- C1: PASS — 61 lines

### spike-driven-dev
- F1: PASS — name exists (`spike-driven-dev`)
- F2: PASS — name format (kebab-case, 15 chars)
- F3: PASS — name matches directory
- F4: PASS — description exists
- F5: WARN — description starts with "Guide" (noun), not an action verb. Consider: "Apply spike-driven development methodology..."
- F6: WARN — `allowed-tools` missing. As a methodology guide, it's passive reference — consider adding `allowed-tools: Read` or marking `user-invocable: false` for background knowledge.
- F12: PASS — no unknown fields
- C1: PASS — 143 lines
- C2: PASS — references/ files are referenced from SKILL.md (decision-criteria.md, examples.md, spike-patterns.md)
- C3: WARN — uses relative paths (`references/decision-criteria.md`) instead of `${CLAUDE_SKILL_DIR}/references/`. May fail when skill runs from a different working directory.

### technical-decision
- F1: PASS — name exists (`technical-decision`)
- F2: PASS — name format (kebab-case, 18 chars)
- F3: PASS — name matches directory
- F4: PASS — description exists
- F5: PASS — description quality (172 chars, starts with "Analyze", contains "Use when")
- F6: PASS — allowed-tools explicit (`WebFetch, WebSearch, Read, Bash`)
- F7: PASS — tools match usage
- F8: WARN — uses `$ARGUMENTS` but no `argument-hint`. Add `argument-hint: "<decision to analyze>"`
- F9: PASS — context:fork has actionable decision analysis workflow
- F10: PASS — agent specified (`general-purpose`)
- F12: PASS — no unknown fields
- C1: PASS — 65 lines

## Agents

### convention-auditor
- A1: PASS — name exists (`convention-auditor`)
- A2: PASS — name format (kebab-case)
- A3: PASS — description exists
- A4: PASS — description explains delegation trigger ("Audit codebase for compliance with project conventions")
- A5: PASS — tools explicit (`Read, Grep, Glob, Write`)
- A6: PASS — model specified (`haiku`)
- A7: PASS — system prompt with clear role and detailed instructions

### research-docs-fetcher
- A1: PASS — name exists (`research-docs-fetcher`)
- A2: PASS — name format (kebab-case)
- A3: PASS — description exists
- A4: WARN — description is vague ("Use proactively for researching topics"). Should explain specific delegation triggers. Consider: "Fetch and organize web documentation and technical specs into structured markdown. Use when gathering reference material from multiple URLs or researching technical topics."
- A5: PASS — tools explicit (`WebFetch, Read, Glob, Bash`)
- A6: PASS — model specified (`sonnet`)
- A7: PASS — system prompt with clear workflow

## Top Issues (by impact)

1. **playwright missing allowed-tools + side-effect guard** — This skill writes files and executes code without `allowed-tools` or `disable-model-invocation: true`, granting implicit full-session access with no invocation guard. Highest risk.
2. **3 skills missing allowed-tools** (playwright, prime-web-dev, spike-driven-dev) — Grants implicit full-session tool access. Each should declare the minimum tools needed.
3. **spike-driven-dev uses relative paths** — `references/decision-criteria.md` may break when the skill runs from a different working directory. Should use `${CLAUDE_SKILL_DIR}/references/`.

## Suggested Fixes

### playwright (3 WARNs)
- **F5**: Change description to start with action verb: `"Generate Playwright E2E tests by exploring websites and automating browser interactions. Use when the user wants to generate Playwright tests by exploring a website, or needs browser automation."`
- **F6**: Add `allowed-tools: Bash, Read, Write` (plus any Playwright MCP tools)
- **F11**: Add `disable-model-invocation: true` — skill writes test files and executes them

### prime-web-dev (2 WARNs)
- **F5**: Change description to start with action verb: `"Scan a web codebase quickly — runs git ls-files, reads README and CONTEXT, and summarizes understanding. Use when the user wants a fast overview of a web project."`
- **F6**: Add `allowed-tools: Bash, Read`

### spike-driven-dev (3 WARNs)
- **F5**: Change description to start with action verb: `"Apply spike-driven development methodology with TDD and risk reduction. Use when starting new features, testing architecture patterns, integrating unfamiliar APIs/data sources, or validating technical feasibility before full implementation."`
- **F6**: Add `allowed-tools: Read` (passive reference material) or consider `user-invocable: false` if this is background knowledge only
- **C3**: Replace `references/decision-criteria.md` with `${CLAUDE_SKILL_DIR}/references/decision-criteria.md` (and same for examples.md, spike-patterns.md)

### research-task (1 WARN)
- **F8**: Add `argument-hint: "<research topic or question>"`

### technical-decision (1 WARN)
- **F8**: Add `argument-hint: "<decision to analyze>"`

### research-docs-fetcher (1 WARN)
- **A4**: Improve description: `"Fetch and organize web documentation and technical specs into structured markdown. Use when gathering reference material from multiple URLs or researching technical topics requiring web access."`
