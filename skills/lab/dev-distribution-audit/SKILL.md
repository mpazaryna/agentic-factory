---
name: dev-distribution-audit
description: "Audit what a skill repository actually ships versus what its authors think it ships — silent shadowing, depth-limit invisibility, name-collision dedup, leaked project skills, and manifest drift. Use when publishing or restructuring a skill library, after moving skill directories, or when an installed skill is missing or duplicated."
allowed-tools: Read, Grep, Glob, Bash
---

# Distribution Audit

A skill can be perfectly written and still never reach anyone. This skill checks
the layer where that happens: the gap between the files in the repo and the
skills an installer actually gets.

Distinct from `dev-skills-auditor`, which audits skill *quality* — frontmatter,
descriptions, structure, naming. That one asks "is this skill well-formed?" This
one asks "does this skill arrive at all, exactly once, where intended?"

Run it before publishing, after any directory move, and whenever someone reports
a skill missing or showing up twice.

## Core principle

**Never audit by reading the layout. Run the installers and diff.** Every failure
below is silent — no error, no warning, just a skill that isn't there. The
directory tree looks correct in all of them.

## The checks

### 1. Ground truth versus offered

Establish what exists, then what an installer is actually offered.

```bash
# Ground truth: every skill's declared name
find skills -name 'SKILL.md' -not -path '*/node_modules/*' \
  -exec grep -m1 '^name:' {} \; \
  | sed 's/^name: *//; s/^["'"'"']//; s/["'"'"']$//' | sort > /tmp/ground.txt

# What the CLI offers
npx skills@latest add . --list 2>&1 | tee /tmp/raw.txt | grep -c 'Found'
```

Parse the names out of `/tmp/raw.txt` and diff against `/tmp/ground.txt`.

The list output is decorated with box-drawing characters and its exact shape is
not a stable contract. If a parse looks wrong, fall back to comparing the
reported `Found N skills` against `wc -l < /tmp/ground.txt` and reading the list
by eye. **A count match is not a pass** — collisions can hide a missing skill
behind an unexpected one.

Report both directions:

- **In repo, not offered** → invisible. Check depth (§2) and shadowing (§3).
- **Offered, not expected** → a leak. Check §4.

### 2. Depth

Discovery stops two levels below a container prefix. `skills/<category>/<skill>/SKILL.md`
is the deepest layout that works.

```bash
find skills -name 'SKILL.md' | awk -F/ 'NF>4 {print NF-1" levels: "$0}'
```

Anything deeper is found only when the installer passes `--full-depth`, which the
repo cannot request on their behalf. Treat every hit as invisible.

### 3. Shadowing

A directory holding its own `SKILL.md` is treated as one skill, and **every child
skill directory beneath it is silently dropped**.

```bash
for f in $(find skills -name 'SKILL.md'); do
  d=$(dirname "$f")
  if find "$d" -mindepth 2 -name 'SKILL.md' | grep -q .; then
    echo "SHADOWING: $d has SKILL.md and skill children"
  fi
done
```

Any hit is a defect. Category and container directories describe themselves with
`README.md`, never `SKILL.md`.

### 4. Leaked project skills

The CLI scans agent directories as well as `skills/` — `.claude/skills/`,
`.agents/skills/`, `.codex/skills/` and roughly two dozen others. A skill kept in
`.claude/skills/` for local development ships to everyone who installs the repo.

```bash
ls -d .claude/skills/*/ .agents/skills/*/ 2>/dev/null
```

For each hit, decide deliberately: publish it (move into a category folder) or
stop tracking it. Leaving it is the failure mode, because nothing warns you.

### 5. Name collisions

Discovery deduplicates by the frontmatter `name`, not by path. When two
directories declare the same name, **one silently wins on search order** and the
other vanishes.

```bash
find skills -name 'SKILL.md' -exec grep -m1 '^name:' {} + \
  | sed 's/:name: */ /' | awk '{print $NF}' | sort | uniq -d
```

Any duplicate is a defect even when the winner is the one you wanted — the
outcome depends on directory ordering, so it flips without warning when files
move. Positional luck is not curation.

### 6. Duplicate descriptions

Two skills with near-identical `description` fields give the model no basis to
choose between them.

```bash
find skills -name 'SKILL.md' -exec grep -m1 '^description:' {} + | sort -t: -k2
```

Read adjacent pairs. Identical or near-identical descriptions mean the skills
should be merged, or differentiated on the axis that actually distinguishes them.

### 7. Name matches directory

```bash
for f in $(find skills -name 'SKILL.md'); do
  d=$(basename "$(dirname "$f")")
  n=$(grep -m1 '^name:' "$f" | sed 's/^name: *//; s/^["'"'"']//; s/["'"'"']$//')
  [ "$d" = "$n" ] || echo "MISMATCH: dir=$d name=$n"
done
```

### 8. Manifest integrity

```bash
claude plugin validate .
```

Then verify by hand, because validation checks schema and not reality:

- Every path in every `skills` array resolves to a directory that exists. A
  directory move leaves these pointing at nothing, and validation still passes.
- No plugin ships the same skill from two locations (a duplicated copy is dead
  weight and drifts from its source).
- Paths listed for a marketplace-root entry (`source: "./"`) replace the default
  scan rather than adding to it.

### 9. Curation drift

The CLI and plugin paths do not ship the same set, by design:

| Path | Curated | Determined by |
|------|---------|---------------|
| `npx skills add <repo>` | No — everything in the repo | the directory walk |
| `/plugin install <name>` | Yes — listed paths only | `marketplace.json` |

State the difference explicitly in the report. Folder names like `lab/`,
`deprecated/`, or `in-progress/` signal status to a human reading the picker and
**exclude nothing** from the CLI. If the delta is unintentional, the fix is the
manifest, not the folder name.

## Report format

```
DISTRIBUTION AUDIT — <repo>

CLI     (npx skills add):    N skills offered
Plugins (marketplace.json):  M skills across P plugins

DEFECTS
  <check> — <what is wrong> — <the specific consequence>

INTENTIONAL DELTA
  <skills in the CLI set but not in any plugin, and why>

VERDICT: ships as intended / N defects
```

Lead with defects. For each one name the consequence in installer terms — "this
skill is invisible to every CLI user," not "the layout is unconventional." Every
check here is silent by nature, so a clean-looking tree proves nothing and the
report is the only signal.
