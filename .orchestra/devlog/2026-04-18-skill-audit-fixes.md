---
created_on: 2026-04-18
commits: 57a6a95
---

# Skill Audit Fixes — Kairos and Orchestra

## Overview

Systematic audit of all 34 skills against Claude Code standards. Found and fixed two categories of breakage: missing `allowed-tools` in orchestra skills, and broken tool paths in kairos skills.

## Kairos: Broken Tool Paths

All five kairos skills (`kairos-kickoff`, `kairos-shutdown`, `kairos-knote`, `kairos-review`, `kairos-weekly-plan`) referenced:

```
kairos/tools/clickup-today.sh
```

This path doesn't exist. The real script lives at:

```
~/workspace/primary-pm/_tools/clickup-today.sh
```

Fixed all five skills to use the correct absolute path. These skills are optimized for this machine only — no attempt to make the path portable.

## Orchestra: Missing allowed-tools

Six of seven orchestra skills lacked `allowed-tools` in their SKILL.md frontmatter. Without it, Claude Code grants implicit full-session access — the skill can use any tool available in the session, which is both unsafe and unpredictable.

Added explicit tool lists to each:

| Skill | Tools |
|-------|-------|
| `orchestra-prd` | Read, Write, Glob |
| `orchestra-spec` | Read, Write, Glob |
| `orchestra-ticket` | Read, Write, Glob |
| `orchestra-milestone` | Read, Write, Glob, Bash |
| `orchestra-scaffold` | Read, Write, Bash |
| `orchestra-adr` | Read, Write, Glob |
| `orchestra-roadmap` | Read, Write, Glob |

## Orchestra: Broken Template References

Several skills referenced template files via `${CLAUDE_PLUGIN_DIR}/references/*.md` — paths that made sense in the old nested plugin layout but don't exist in the flat structure.

Replaced all template references with inline generation instructions. Skills now carry their output format spec directly in SKILL.md rather than loading an external file.

## Lesson

`allowed-tools: Always` in the CLAUDE.md conventions is there for a reason. Skills without it are a latent footgun — they work fine until someone runs them in a session with destructive tools available.
