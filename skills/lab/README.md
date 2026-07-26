# lab/

Skills in review. Not yet proven, deliberately visible.

A skill lands here when it's worth looking at but hasn't earned a category folder
— the idea is sound, the shape is uncertain, and it needs eyes before it's
treated as reliable. The lab is where "I think this should exist" lives before it
becomes "this works."

## What the lab is not

**It is not hidden.** `npx skills add mpazaryna/agentic-factory` offers every
skill in this repo, lab included — folder names are not a filter. Anyone
installing via the CLI sees lab skills in the picker alongside proven ones.

What the lab *does* control is plugin distribution. `skills/lab/` is deliberately
absent from every `skills` array in `.claude-plugin/marketplace.json`, so
`/plugin install skills@agentic-factory` ships the four category folders and
nothing from here. That asymmetry is the whole mechanism:

| Install path | Gets lab skills? |
|--------------|------------------|
| `npx skills add …` | **Yes** — every skill in the repo |
| `/plugin install …@agentic-factory` | **No** — only paths listed in the manifest |

If a lab skill must not reach anyone yet, it doesn't belong in this repo — keep
it in the project you're building it in.

## Conventions

**Name it its final name on day one.** The `name` field is the invocation
identity, and renaming breaks anyone who already installed it. A skill destined
for `dev/` is called `dev-*` while it sits in the lab. Graduation is then a pure
move:

```bash
git mv skills/lab/dev-thing skills/dev/dev-thing
```

No rename, no broken installs, no manifest surprise. Add it to the relevant
`skills` array in `marketplace.json` at that point — that's what graduating
means.

**Each lab skill carries a `REVIEW.md`** stating what feedback it needs: the open
questions, the parts the author isn't sure about, and what would have to be true
to promote it. Without that, "in review" is just a folder name.

**Retire freely.** A lab skill that doesn't earn promotion gets deleted. Git
history is the archive — see `CLAUDE.md`.

## Current occupants

| Skill | Needs | Open questions |
|-------|-------|----------------|
| [`dev-distribution-audit`](dev-distribution-audit) | Real-world runs against other skill repos | See its [REVIEW.md](dev-distribution-audit/REVIEW.md) |
