---
name: branch
description: "Create a new feature branch from main with safety checks. Use when the user wants to start a new feature branch."
argument-hint: "<branch-name>"
disable-model-invocation: true
---

Create a new feature branch from main and ensure safe development practices. Required branch name: $ARGUMENTS

## Steps

1. Check current git status and warn if there are uncommitted changes
2. Switch to main branch: `git checkout main`
3. Pull latest changes: `git pull origin main`
4. If no branch name provided in $ARGUMENTS, suggest branch name based on:
   - Current date (format: YYYY-MM-DD)
   - Common prefixes: feature/, fix/, chore/, docs/
   - Ask to confirm or specify different branch name
5. Create and switch to new branch: `git checkout -b [BRANCH_NAME]`
6. Show current branch status: `git branch --show-current`
7. Show git status to confirm clean working directory

## Safety Checks

- Warn if already on a feature branch and ask for confirmation
- Warn if uncommitted changes exist and suggest stashing or committing first
- Prevent accidental work directly on main branch
- Ensure main is up to date before branching
