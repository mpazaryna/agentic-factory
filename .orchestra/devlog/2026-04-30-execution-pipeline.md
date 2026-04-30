---
created_on: 2026-04-30
---

# Orchestra Gets an Execution Pipeline

## What Changed

Orchestra has always covered the left side of the development lifecycle — ticket, PRD, spec, gherkin. Today we built the right side: three skills that take a locked spec from approved to merged.

```
Before: ticket → PRD → spec → gherkin → [nothing]
After:  ticket → PRD → spec → gherkin → implement → review → merge
```

## The Trigger

A work item to evaluate Sand Castle (`@aihero/sandcastle`) — Matt Pocock's TypeScript library for running AI coding agents AFK in Docker sandboxes. The original plan was a seven-step evaluation: read the source, spike it, run a pipeline, score it, write an ADR.

We didn't do any of that.

Instead, studying Sand Castle's design surfaced something more useful: orchestra already had the right conceptual pieces, just not the execution half. Sand Castle's planner → implementer → reviewer → merger pattern mapped almost exactly onto what orchestra was missing. The question shifted from "should we adopt this?" to "why don't we have this already?"

The PRD and spec were rewritten to reflect what we actually decided to do.

## Key Decisions

**Skills, not sub-agents.** The instinct was to make Lenny orchestrate the pipeline. We pushed back on that. Skills are the right layer — each stage is a discrete human invocation. Once the skills are solid, AFK execution is a trivial loop controller. The hard part is the skill definitions, not the automation.

**Three explicit stages, not one `orchestra-run`.** It would have been easy to wrap everything in a single skill. Instead: implement, review, merge as separate invocations. The human controls the handoff. You can inspect between stages. The pipeline is visible, not hidden inside a black box.

**The Q&A phase is load-bearing.** Sand Castle assumes the backlog item is already implementation-ready. Orchestra's Q&A → PRD → spec phase is what makes that true. The tighter the spec, the less judgment the implementer needs. Keeping Q&A as a human-in-the-loop phase is what makes AFK execution viable downstream.

**Status vocabulary is now complete.** Previously the vocabulary stopped at `approved`. It now runs end-to-end:

```
draft → approved → in-progress → complete → reviewed → closed
```

Each skill owns a transition. No skill crosses into another's territory.

## The Program

`orchestra-program` was added as a companion: a user-invocable orientation skill that explains what orchestra is, the full pipeline, file structure, status vocabulary, and skill index. The framing: it's the program handed to everyone who walks into the venue before the lights go dark. A new collaborator or a bootstrapping agent can ask "what is orchestra?" and get a complete answer.

## Dev Friction Fix

`~/.claude/skills/` was a real directory populated by the plugin install workflow. Every skill edit required a reinstall. Replaced it with a symlink to the repo:

```bash
ln -s /Users/mpaz/workspace/agentic-factory/skills ~/.claude/skills
```

The repo is now the install. Edit a skill, it's live globally with no intermediate step. `clickup-backfill` was the only skill in `~/.claude` not yet in the repo — promoted and committed before the swap.

## What's Next

The pipeline exists as skills. Running it AFK is now a loop controller away — a shell script or cron that calls the skills in sequence. The natural next question is whether Lenny gets updated to conduct that loop, or whether a lighter trigger is enough.
