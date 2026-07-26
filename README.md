# Agentic Factory

A curated skill library for Claude Code. 31 skills in 4 categories, built from real work and promoted here when proven.

## Structure

```
skills/     — 31 skills in 4 category folders
```

Skills live one level below a category folder: `skills/<category>/<skill>/SKILL.md`.
That is the deepest layout both installers discover — see [CLAUDE.md](CLAUDE.md#nesting-depth).

## Skills

| Category | Skills |
|----------|--------|
| `platform/` | **Cloudflare:** cloudflare, workers-best-practices, wrangler, durable-objects, cf-hono, agents-sdk, sandbox-sdk, cloudflare-email-service<br>**Apple:** swift-lang, swift-ui, swiftui-submission-prep |
| `practice/` | **Kairos rhythm:** kairos-kickoff, kairos-shutdown, kairos-knote, kairos-review, kairos-weekly-plan, kairos-weekly-finalize<br>**Investigation:** feynman-inquiry, feynman-decision<br>**Workflow:** clickup-backfill, digest, writing-no-slop |
| `dev/` | dev-enforcer, dev-playwright, dev-skills-auditor, web-perf |
| `yoga/` | yoga-orchestrator, yoga-anatomy-expert, yoga-asana-strategist, yoga-professor, yoga-theme-developer |

## Install

Skills install **per project** — each repo (substation) declares the skills it
consumes. There is no global install.

### Skills you'll adapt — editable copy (capabilities)

Pull skills into the current project with the [`skills`](https://www.skills.sh)
CLI. They land in the project's agent dir, editable and committed with the repo:

```bash
npx skills@latest add mpazaryna/agentic-factory                          # choose interactively
npx skills@latest add mpazaryna/agentic-factory --skill kairos-kickoff   # a single skill
npx skills@latest update                                                # re-sync from source
```

The CLI offers every skill in the repo regardless of category folder — the
folders organize the source, they don't filter the install.

### Skills that must stay identical — read-only, versioned (contracts)

Install a marketplace plugin: a managed, read-only bundle that moves as one
unit. Read-only means it *can't* drift — you can't edit it in place, only pull a
new version.

```
/plugin marketplace add mpazaryna/agentic-factory
/plugin install skills@agentic-factory        # all 31 skills
/plugin install cloudflare@agentic-factory    # Cloudflare platform subset only
```

Unlike the CLI, plugins **are** curated: each entry in
`.claude-plugin/marketplace.json` lists exactly the paths it ships.

## Authoring

Build in a real project first. Promote here when the skill is proven and generic enough to reuse.

Each skill needs:
- `SKILL.md` — YAML frontmatter (`name`, `description`, `allowed-tools`) + instructions
- `README.md` — human-readable companion

See [CLAUDE.md](CLAUDE.md) for conventions and quality standards.
