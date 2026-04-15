---
name: push
description: "Stage, commit, and push the current branch following git governance rules. Use when the user wants to commit and push their changes to the remote."
disable-model-invocation: false
---

## Git Governance

- Never use `git add .` or `git add -A` unless every change has been individually reviewed.
- Never stage files containing secrets, credentials, API keys, or tokens.
- Never add AI attribution strings (e.g., `Co-Authored-By: ...`) to commits.
- Never force-push (`--force` or `--force-with-lease`) without explicit user approval.
- Never push directly to `main` or `master` unless the user explicitly confirms.

## Procedure

1. **Review and stage changes** — Run `git status --short`, inspect diffs, and stage files intentionally with `git add <file>`. Avoid staging generated, build, or secret files.

2. **Compose the commit message** — Follow [Conventional Commits](https://www.conventionalcommits.org/):
   - **Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
   - **Subject line** must be 72 characters or fewer.
   - **Scope** uses kebab-case, e.g., `fix(api-client): handle timeout`.
   - Use imperative mood in the subject.
   - If a `commit-template.txt` exists in the repo, use its Context / Testing / Reviewers sections.

3. **Commit** — Run `git commit` with the prepared message. If a commitlint hook or pre-commit hook fails, fix the message or staged content and retry.

4. **Push to origin** — Push the current branch:
   ```
   git push origin $(git branch --show-current)
   ```
   - If the remote branch does not exist yet, use `git push -u origin $(git branch --show-current)`.
   - If the push is rejected due to upstream changes, run `git pull --rebase` first, resolve any conflicts, then push again.

5. **Verify** — Confirm the push succeeded:
   ```
   git log origin/$(git branch --show-current) -1 --oneline
   ```
