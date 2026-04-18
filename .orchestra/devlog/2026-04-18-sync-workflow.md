---
created_on: 2026-04-18
commits: 29d5cda
---

# Skills Sync Workflow — sync.sh

## Overview

Added `sync.sh` to replace manual copying of skills to `~/.claude/skills/`. One command keeps the local Claude installation in sync with the repo.

## Problem

During development, skills live in `~/workspace/agentic-factory/skills/`. Claude Code reads installed skills from `~/.claude/skills/`. These were diverging — stale skills in `~/.claude/` were shadowing updated repo versions, causing confusing behavior.

We explored symlinks first. Symlinks work for skill *invocation* but fail `/skills` discovery — Claude Code doesn't follow symlinks when building the skills index.

## Solution

```bash
#!/usr/bin/env bash
SRC="$(dirname "$0")/skills/"
DEST="$HOME/.claude/skills/"
mkdir -p "$DEST"
rsync -av --delete "$SRC" "$DEST"
```

`rsync --delete` ensures removals propagate — if a skill is pruned from the repo, it disappears from `~/.claude/skills/` on next sync. Without `--delete`, deleted skills would linger indefinitely.

## Workflow

```
edit skill in skills/
./sync.sh
test with /skill-name in Claude Code
commit when solid
```

## Why Not Symlinks

Claude Code's plugin scanner resolves skill paths at index time. When the path is a symlink, the scanner sees the symlink target as outside the plugin directory and skips it. Rsync copies the actual files, which is what the scanner expects.
