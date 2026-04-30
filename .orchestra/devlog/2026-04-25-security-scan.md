---
created_on: 2026-04-25
commits: 11ae886
---

# Security Scan: Agentic Factory Codebase

## What Was Done

Ran a full security audit of the agentic-factory repo. The branch was clean (no pending changes), so this was a baseline scan of the current HEAD rather than a diff-focused PR review.

## Surface Area

The repo is almost entirely markdown and YAML — skills, agent definitions, and plugin metadata. Executable code is minimal:

- `sync.sh` — 15-line rsync utility, the only shell script in the repo
- `settings.local.json` — Claude Code permission allowlist
- `plugin.json` / `marketplace.json` — plugin distribution manifests
- `agents/*.md` — four autonomous agent definitions (eddie, lenny, monk, slim) that describe shell commands and tool calls in their instruction bodies

## Findings

**No high-confidence vulnerabilities found.**

Checked specifically for:
- Shell injection in skill bodies (`eval`, `exec`, backtick substitution) — none found
- Hardcoded secrets in tracked files — none found (`.env` exists locally, is gitignored, and was never committed to history)
- Dangerous file write operations outside project scope — none found
- Overly broad `allowed-tools` declarations that could enable privilege escalation — all 34 skills have explicit restrictions

### sync.sh

Clean. Uses `set -euo pipefail`, quoted variables, and a straightforward `rsync -av --delete` to `~/.claude/skills/`. The `--delete` flag removes stale skills from the destination, which is the intended behaviour. No injection vectors.

### Agent Definitions

The four agents (eddie, lenny, monk, slim) reference two external scripts not in this repo:
- `kairos/tools/clickup-today.sh` (used by monk)
- `tools/fetch_feeds.py` (used by eddie)

These are not auditable from this repo. They're out of scope for the factory itself but worth a note: if either script is compromised or poorly written, the agents that invoke them would inherit the risk.

Lenny performs autonomous git commits and pushes. This is by design but means a mis-scoped invocation could push unintended changes. The risk is in the orchestration pattern, not a code vulnerability.

### settings.local.json Permissions

The local settings allowlist includes `Bash(git commit -m ' *)` and `Bash(git push *)`. These are intentionally permissive for development workflow in this repo. They're project-scoped (`.claude/settings.local.json`) and not committed via the public plugin, so downstream consumers don't inherit them.

## Summary

The repo's security posture is strong by virtue of its nature: no server, no user input, no database, no crypto, no auth. The primary risk surface is the autonomous agents invoking external scripts and performing git operations — risks that are architectural rather than vulnerabilities in the code itself.

Nothing to remediate.
