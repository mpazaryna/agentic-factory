# Agentic Factory

31 skills for Claude Code, each built to fix something that actually went wrong.

Every one of these came out of real work, got used until it earned its place, and
was promoted here. Start with the problem you have.

---

## "The agent is coding against last year's API."

Model weights lag the platform. Ask about Workers bindings or Wrangler config and
you get plausible, confident, outdated answers — signatures that moved, config
fields that were renamed, patterns that were deprecated two releases ago.

Eight skills refuse to answer from memory. Each one names its retrieval sources
and fetches current documentation *before* writing or reviewing code.

| Skill | Use when |
|-------|----------|
| [`cloudflare`](skills/platform/cloudflare) | Any Cloudflare task — umbrella over 60+ product references |
| [`workers-best-practices`](skills/platform/workers-best-practices) | Writing or reviewing a Worker; catching floating promises, global state, leaked secrets |
| [`wrangler`](skills/platform/wrangler) | Before running any `wrangler` command |
| [`durable-objects`](skills/platform/durable-objects) | Stateful coordination — rooms, games, bookings, RPC, SQLite, alarms |
| [`agents-sdk`](skills/platform/agents-sdk) | Stateful agents, durable workflows, real-time WebSocket agents |
| [`sandbox-sdk`](skills/platform/sandbox-sdk) | Executing untrusted code — interpreters, CI, dev environments |
| [`cloudflare-email-service`](skills/platform/cloudflare-email-service) | Transactional email via Email Sending / Routing |
| [`web-perf`](skills/dev/web-perf) | Auditing Core Web Vitals, render-blocking resources, layout shift |

## "It said it was done. It wasn't."

The agent reports success. You look, and find a stubbed function, a hardcoded
fixture standing in for a real API call, a `TODO` where the hard part was, or a
test that asserts nothing.

**[`dev-enforcer`](skills/dev/dev-enforcer)** reviews implementation quality
specifically for this: workarounds, simulated data, incomplete implementations,
shortcuts. Run it before you believe a completion report.

## "We chose the library in a Slack thread and nobody remembers why."

Technical decisions get made fast and lose their reasoning immediately. Six
months later the constraint that drove the choice is gone and nobody can tell
whether the choice still holds.

- **[`feynman-inquiry`](skills/practice/feynman-inquiry)** — structured
  investigation when you're exploring unfamiliar technology and need to
  understand it well enough to commit.
- **[`feynman-decision`](skills/practice/feynman-decision)** — comparison
  matrices, explicit scoring, and a drafted ADR so the reasoning survives the
  decision.

## "Where did the week go?"

Work happens, and none of it gets captured. Carry-overs pile up invisibly, you
can't tell a heavy week from a light one, and the retrospective is guesswork
because there's nothing to look back at.

The **kairos** rhythm — a loop, not a pile of scripts:

```
kickoff → knote (all day) → shutdown  ·  weekly-plan → weekly-finalize  ·  review
```

| Skill | Use when |
|-------|----------|
| [`kairos-kickoff`](skills/practice/kairos-kickoff) | Morning — tasks, carry-overs, project gaps, intensity patterns |
| [`kairos-knote`](skills/practice/kairos-knote) | Any time a thought is worth keeping |
| [`kairos-shutdown`](skills/practice/kairos-shutdown) | End of day — completions, uncommitted work, tomorrow's frog |
| [`kairos-weekly-plan`](skills/practice/kairos-weekly-plan) | Monday — project triage, load calculation, priorities |
| [`kairos-weekly-finalize`](skills/practice/kairos-weekly-finalize) | After acting on the draft plan |
| [`kairos-review`](skills/practice/kairos-review) | Weekly, monthly, quarterly, yearly zoom |

## "It reads like a robot wrote it."

Em-dash pileups, "it's not just X, it's Y," "delve," "leverage," dramatic
one-sentence paragraphs for emphasis. Fluent and unmistakably machine-made.

**[`writing-no-slop`](skills/practice/writing-no-slop)** is a style guide that
bans the specific clichés, filler, and vague vocabulary that give it away.

---

## Also here

Skills that are reference material or narrow tooling rather than answers to a
recurring failure:

| Skill | What it does |
|-------|--------------|
| [`cf-hono`](skills/platform/cf-hono) | Hono routing, middleware, typed handlers on Workers |
| [`swift-lang`](skills/platform/swift-lang) | Macros, concurrency, generics, protocol design |
| [`swift-ui`](skills/platform/swift-ui) | Views, state, layout, animation, app architecture |
| [`swiftui-submission-prep`](skills/platform/swiftui-submission-prep) | App Store review readiness before you submit |
| [`dev-playwright`](skills/dev/dev-playwright) | Generate E2E tests by exploring a site |
| [`dev-skills-auditor`](skills/dev/dev-skills-auditor) | Audit skills for frontmatter, descriptions, structure |
| [`digest`](skills/practice/digest) | Extract key points from a URL or YouTube video |
| [`clickup-backfill`](skills/practice/clickup-backfill) | Reconcile work items against ClickUp tickets |

And a domain vertical, kept because it's the clearest example of skills composing
into a system rather than acting alone — an orchestrator routing to four
specialists: [`yoga-orchestrator`](skills/yoga/yoga-orchestrator),
[`yoga-anatomy-expert`](skills/yoga/yoga-anatomy-expert),
[`yoga-asana-strategist`](skills/yoga/yoga-asana-strategist),
[`yoga-professor`](skills/yoga/yoga-professor),
[`yoga-theme-developer`](skills/yoga/yoga-theme-developer).

---

## Install

Skills install **per project** — each repo declares what it consumes. There is
no global install.

### Skills you'll adapt — editable copy

Pull skills into the current project with the [`skills`](https://www.skills.sh)
CLI. They land in the project's agent dir, editable and committed with the repo:

```bash
npx skills@latest add mpazaryna/agentic-factory                          # choose interactively
npx skills@latest add mpazaryna/agentic-factory --skill kairos-kickoff   # a single skill
npx skills@latest update                                                 # re-sync from source
```

The CLI offers every skill in the repo regardless of category folder — the
folders organize the source, they don't filter the install.

### Skills that must stay identical — read-only, versioned

Install a marketplace plugin: a managed bundle that moves as one unit. Read-only
means it *can't* drift — you can't edit it in place, only pull a new version.

```
/plugin marketplace add mpazaryna/agentic-factory
/plugin install skills@agentic-factory        # all 31 skills
/plugin install cloudflare@agentic-factory    # Cloudflare platform subset only
```

Unlike the CLI, plugins **are** curated: each entry in
`.claude-plugin/marketplace.json` lists exactly the paths it ships.

## Layout

```
skills/
├── platform/   11   target runtimes — Cloudflare, Apple
├── practice/   11   rhythm, investigation, capture
├── dev/         4   building and auditing
└── yoga/        5   domain vertical
```

Skills sit one level below a category folder:
`skills/<category>/<skill>/SKILL.md`. That is the deepest layout both installers
discover — see [CLAUDE.md](CLAUDE.md#nesting-depth) before adding a folder.

## Authoring

Build in a real project first. Promote here when the skill is proven and generic
enough to reuse — and when you can name the problem it solves.

Each skill needs:
- `SKILL.md` — YAML frontmatter (`name`, `description`, `allowed-tools`) + instructions
- `README.md` — human-readable companion

See [CLAUDE.md](CLAUDE.md) for conventions and quality standards.
