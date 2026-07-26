# Review — dev-distribution-audit

## Why it exists

Restructuring this repo surfaced a failure class that no existing skill catches.
Every one of these was live in `agentic-factory` and none produced a warning:

| Found | Consequence |
|-------|-------------|
| `.claude/skills/skills-auditor/` tracked in the repo | shipped to every CLI installer, with a description byte-identical to `dev-skills-auditor` |
| `plugins/cloudflare/` holding 5 copies of skills already in `skills/` | invisible only because name-dedup happened to favor `skills/`; a rename or reordering would have surfaced 5 duplicates |
| `marketplace.json` using `"skills": "./"` | would have discovered **zero** skills the moment category folders were introduced |
| README and CLAUDE.md listing 9 skills deleted commits earlier | docs described a repo that no longer existed |

The pattern: individually well-formed skills, broken at the distribution layer,
failing silently. `dev-skills-auditor` would have passed all of it.

## Open questions

**1. Should this fork?** It produces a lot of intermediate shell output, which
argues for `context: fork` per the repo's own convention. Against: an audit's
evidence is the useful part, and forking returns a summary while discarding the
diffs a reviewer wants to read. Currently inline. Undecided.

**2. The `--list` parse is brittle.** §1 depends on parsing box-drawing
characters out of CLI output that is not a stable contract. The skill says so and
gives a fallback, but a real solution probably means asking upstream for
`--json`. Until then §1 is the weakest check in a skill whose whole premise is
"don't trust the layout, run the installer."

**3. Depth and prefix rules are pinned to observed behavior**, not documented
guarantees. The two-level limit, the shadowing rule, and the priority-prefix list
were established empirically against `skills@1.5.20` by building fixtures at each
depth. They are not in any published spec and could change without notice. Needs
a version note, and possibly a self-check that warns when the installed CLI is
much newer.

**4. Is it too repo-specific?** Every check generalizes to any skill repo in
principle, but all of them were derived from one restructure. Running it against
`mattpocock/skills`, `vercel-labs/agent-skills`, and an unrelated library would
show whether the checks hold or whether they encode this repo's accidents.

**5. Overlap with `dev-skills-auditor`.** The split — quality versus distribution
— is clean in description but untested in practice. If running both routinely
means running them together, they should probably merge.

## Promotion criteria

Move to `dev/` when:

- [ ] Run against at least three skill repos not authored here, finding at least
      one real defect in a repo whose author didn't already know about it
- [ ] §1 no longer depends on parsing decorated terminal output, **or** the
      fallback is proven adequate across those runs
- [ ] The fork question is settled with a reason, not a default
- [ ] The overlap question is settled: merge with `dev-skills-auditor`, or state
      the boundary in both descriptions so the model can route between them

Delete it instead if the checks turn out to encode this repo's history rather
than a general failure class.
