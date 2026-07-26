# dev-distribution-audit

Checks what a skill repository actually ships against what its authors think it
ships.

**Status: in the lab.** Not yet proven — see [REVIEW.md](REVIEW.md) for open
questions and promotion criteria.

## The problem

A skill can be flawless and still never reach anyone. Discovery failures are
silent: no error, no warning, and a directory tree that looks correct in every
case.

- A category folder that gains its own `SKILL.md` silently swallows every skill
  beneath it.
- A skill nested one level too deep is invisible to every installer who doesn't
  pass `--full-depth` — which the repo cannot ask for.
- Two skills declaring the same `name` deduplicate by search order, so one
  vanishes and which one is positional luck.
- A skill left in `.claude/skills/` for local development ships to everyone.
- Manifest paths that point at moved directories still pass schema validation.

## What it does

Runs the real installers and diffs their output against the repo, rather than
inferring correctness from the layout. Nine checks: ground-truth diff, depth,
shadowing, leaked project skills, name collisions, duplicate descriptions,
name/directory match, manifest integrity, and CLI-versus-plugin curation drift.

Reports defects in installer terms — "invisible to every CLI user" rather than
"unconventional layout."

## Usage

```
/dev-distribution-audit
```

Run from the root of a skill repository. Requires network access for
`npx skills@latest` and the `claude` CLI for manifest validation.

## Related

- `dev-skills-auditor` — audits skill *quality*: frontmatter, descriptions,
  structure, naming. Ask that one "is this skill well-formed?" and this one "does
  it arrive at all, exactly once, where intended?"
