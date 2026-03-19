---
name: commit
description: "Stage working tree changes and create a Conventional Commit (no push). Use when the user wants to commit their current changes with proper governance."
disable-model-invocation: false
---

## Git Governance

- Never use `git add .` or `git add -A` unless every change has been individually reviewed.
- Never stage files containing secrets, credentials, API keys, or tokens.
- Never add AI attribution strings (e.g., `Co-Authored-By: ...`) to commits.
- Never amend a prior commit without explicit user approval.
- Never push in this skill. Use the **push** skill when ready to publish.

## Procedure

1. **Review changes** — Run `git status --short` to see all pending changes.

2. **Inspect diffs** — For each modified or untracked file, run `git diff -- <file>` (or `git diff --cached -- <file>` for already-staged files). Verify:
   - No secrets, credentials, or sensitive data are present.
   - No unintended generated or build artifacts are included.

3. **Stage intentionally** — Add files one-by-one or in logical groups:
   ```
   git add path/to/file
   ```

4. **Compose the commit message** — Follow [Conventional Commits](https://www.conventionalcommits.org/):
   - **Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
   - **Subject line** must be 72 characters or fewer.
   - **Scope** uses kebab-case, e.g., `feat(auth-flow): add token refresh`.
   - Use imperative mood in the subject (e.g., "add", not "added" or "adds").
   - Optionally include a body separated by a blank line for additional context, testing notes, or reviewer guidance.
   - If a `commit-template.txt` exists in the repo, use its Context / Testing / Reviewers sections.

5. **Commit** — Run `git commit` with the prepared message. If a commitlint hook or pre-commit hook fails, fix the message or staged content and retry.

6. **Verify** — Show the resulting commit and confirm it looks correct:
   ```
   git log -1 --stat
   ```
   Keep the commit hash handy for the push step.
