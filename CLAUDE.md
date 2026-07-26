# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## What This Is

Agentic Factory is a curated skill library for Claude Code. Skills are proven, reusable components built in real projects and promoted here when they earn their place.

**Skills only.** The four subagents (`eddie`, `lenny`, `monk`, `slim`) were
removed — each loaded skills by plugin-relative path from its origin plugin, and
none of those paths resolved here. Recover any of them from git history
(`git show 8dd39e9:agents/<name>.md`) if they're ever rewired properly.

## Directory Layout

```
skills/     — 31 proven skills in 4 category folders, plus lab/
```

### Skill Categories

| Folder | Scope | Skills |
|--------|-------|--------|
| `platform/` | Target runtimes — Cloudflare and Apple | cloudflare, workers-best-practices, wrangler, durable-objects, cf-hono, agents-sdk, sandbox-sdk, cloudflare-email-service, swift-lang, swift-ui, swiftui-submission-prep |
| `practice/` | Personal rhythm, investigation, workflow | kairos-kickoff, kairos-shutdown, kairos-knote, kairos-review, kairos-weekly-plan, kairos-weekly-finalize, feynman-inquiry, feynman-decision, clickup-backfill, digest, writing-no-slop |
| `dev/` | Tooling for building and auditing | dev-enforcer, dev-playwright, dev-skills-auditor, web-perf |
| `yoga/` | Yoga class planning (multi-skill) | yoga-orchestrator, yoga-anatomy-expert, yoga-asana-strategist, yoga-professor, yoga-theme-developer |
| `lab/` | **In review — not proven.** Excluded from every plugin | dev-distribution-audit |

Domain prefixes in skill *names* are retained — the name is the invocation
identity and renaming breaks existing installs. The folder groups the source;
the prefix disambiguates the command.

## Skill Structure

```
skills/
└── <category>/
    ├── README.md          # Optional — describes the category
    └── <skill-name>/
        ├── SKILL.md       # Required — frontmatter + instructions
        ├── README.md      # Human-readable companion
        └── references/    # Optional supporting material
```

### Nesting Depth

**One category level. No more.** Both installers stop at
`skills/<category>/<skill>/SKILL.md`:

| Layout | `npx skills` | Notes |
|--------|--------------|-------|
| `skills/<skill>/SKILL.md` | ✅ | the pre-3.0 flat layout |
| `skills/<category>/<skill>/SKILL.md` | ✅ | current layout |
| `skills/<cat>/<sub>/<skill>/SKILL.md` | ❌ | found only with `--full-depth`, which the *installer* passes — you cannot enable it from this repo |

**A category folder must never contain its own `SKILL.md`.** The CLI treats a
directory holding `SKILL.md` as a single skill and silently skips every child.
Use `README.md` to describe a category.

## Distribution

Two paths with different curation behavior. Know which you're changing.

| Path | Curated? | Source of truth |
|------|----------|-----------------|
| `npx skills@latest add mpazaryna/agentic-factory` | **No** — offers all 32, every folder including `lab/` | convention: the directory walk |
| `/plugin install <name>@agentic-factory` | **Yes** — only listed paths | `.claude-plugin/marketplace.json` |

```
/plugin marketplace add mpazaryna/agentic-factory
/plugin install skills@agentic-factory        # 31, via the 4 category folders
/plugin install cloudflare@agentic-factory    # 8 Cloudflare skills only
```

Both marketplace entries use `source: "./"` with `strict: false`, so the entry
itself declares metadata and skill paths — there are no per-plugin
`plugin.json` files and no duplicated skill copies. When you add a skill, add it
to the relevant `skills` array if it belongs in a focused plugin; the `skills`
plugin picks it up automatically via its category folder.

Naming a folder `lab/`, `deprecated/`, or `in-progress/` signals status to a
human reading the picker but **does not hide anything** from the CLI. Anything in
the repo is installable. Delete what's superseded; git history is the archive.

## The Lab

`skills/lab/` holds skills under review — worth looking at, not yet proven.

The only real mechanism is the manifest: `lab/` is deliberately absent from every
`skills` array, so plugin installs skip it while CLI installs still offer it.
That asymmetry *is* the lab. A skill that must not reach anyone at all stays in
the project it's being built in, not here.

Three rules:

1. **Final name on day one.** A skill headed for `dev/` is named `dev-*` while it
   sits in the lab, so graduating is `git mv` with no rename and no broken
   installs. Add it to the relevant `skills` array at that point — that is what
   graduating means.
2. **Every lab skill carries a `REVIEW.md`** stating what feedback it needs, what
   the author is unsure about, and the criteria for promotion. Without it, "in
   review" is just a folder name.
3. **Retire freely.** A lab skill that doesn't earn promotion gets deleted.

See [skills/lab/README.md](skills/lab/README.md).

### SKILL.md Frontmatter

| Field | When Required | Notes |
|-------|--------------|-------|
| `name` | Always | kebab-case, matches directory name exactly |
| `description` | Always | 50+ chars, action verb, includes "Use when..." |
| `allowed-tools` | Recommended | Pre-approves tools for the invoking turn only. Accepts a comma/space-separated string **or** a YAML list — this repo uses the inline string form |
| `context: fork` | Research/verbose skills | Runs in isolated subagent |
| `agent` | When `context: fork` | `Explore`, `Plan`, or `general-purpose` |
| `argument-hint` | When skill takes args | Shown to users |
| `user-invocable: false` | Background knowledge only | Claude loads silently |
| `disable-model-invocation: true` | Orchestrators only | User-invoked only; still a slash command |

> **`allowed-tools` does not restrict anything.** Per the Claude Code docs it
> grants permission for the listed tools during the invoking turn so Claude
> isn't prompted; every other tool stays callable and normal permission settings
> still apply. Omitting it is not "implicit full-session access" — it just means
> no pre-approval. List the tools a skill actually needs to run unprompted, and
> use `disallowed-tools` when you genuinely need to remove a tool from the pool.

### Anti-Patterns

- `context: fork` on passive reference material — nothing to fork
- `disable-model-invocation: false` — that's the default; stating it is noise
- Descriptions without "Use when..." — Claude can't auto-load
- **Two skills with the same or near-identical `description`** — Claude has no
  basis to choose between them. Merge them or differentiate the descriptions.

## Conventions

- All names **kebab-case** with domain prefix (e.g., `kairos-kickoff`, `dev-enforcer`)
- Skill directory name must match `name` field in frontmatter
- New skills: build in a project first, promote here when proven
- Project-specific skills stay in the project repo as `.claude/skills/` — but
  note the CLI scans `.claude/skills/` too, so anything left there ships to
  consumers of this repo
- MCP servers → separate repos (`~/workspace/mcp-<name>/`), not here
- Subagents → not here. A skill that needs isolation uses `context: fork`. An
  agent that only exists to load skills by path is a broken indirection
