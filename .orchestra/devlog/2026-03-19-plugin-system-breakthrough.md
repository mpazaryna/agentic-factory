# 2026-03-19: Plugin System Breakthrough — From Broken Discovery to Autonomous Agents on a Schedule

Single session. Started with "why don't my skills show up" and ended with Monk running on a cron in Claude Desktop.

## What Happened

### The Discovery Problem

Plugin skills weren't appearing as slash commands when installed in consumer projects. Spent the first half of the session debugging why. Root causes, in order of discovery:

1. **`disable-model-invocation: true` hides skills from slash commands.** Every skill with this flag was invisible. Removed it from all 18 plugin skills.

2. **`"agents": "./"` is not a valid plugin.json field.** Caused hard install failures. Removed from all 5 plugin.json files that had it.

3. **Skills nested under `skills/` weren't discovered.** The `"skills": "./"` field in plugin.json discovers `*/SKILL.md` one level deep from the root. Our `skills/<name>/SKILL.md` structure was two levels deep. Flattened all 15 plugins — 168 files moved.

4. **Cache keys on version number, not file content.** Multiple cache clears failed because we didn't bump versions. The cache saw "I already have 1.1.0" and served the stale copy. Version bump on every change — no exceptions.

5. **`/reload-plugins` doesn't clear in-memory state.** Must quit and restart Claude entirely after cache clear.

### The Architecture

Once skills were working, we aligned with Anthropic's official plugin structure by studying [claude-plugins-official](https://github.com/anthropics/claude-plugins-official):

- **Skills** = `name/SKILL.md` at plugin root. Slash commands. Interactive, present for approval.
- **Agents** = `agents/name.md` with `name`, `description`, `model` frontmatter. Conversational invocation. Autonomous, no checkpoints.
- **Agents read skills as subject matter expertise.** Same domain knowledge powers both interactive and autonomous workflows.

Key insight: agents are NOT slash commands. You don't type `/orchestra:lenny`. You say "ask lenny to review the milestones" and Claude delegates to the agent.

### The Agents

Built two agents following the pattern:

**Lenny** (orchestra) — Named after Leonard Bernstein. The autonomous conductor. Runs the full milestone loop: PRD → spec → ticket → implement → update score. Loads conventions, milestone, prd, spec, ticket, devlog skills before executing.

**Slim** (product-planning) — Named after Slim Harpo. Autonomous ticket-to-PRD agent. Fetches a ticket, investigates the codebase, writes a formal PRD. Loads prd-template-guidance and ticket-refiner skills.

**Monk** (kairos) — Named after Thelonious Monk. Autonomous daily rhythm keeper. Runs kickoff and shutdown without human interaction. Loads kickoff, shutdown, interstitial skills.

### Kairos Goes Portable

Stripped all Obsidian vault paths (`50-log/`, `_data/`, `_tools/`) and replaced with a self-contained `kairos/` folder. Drop it in any project, install the plugin, Monk runs. No vault, no Obsidian, no configuration.

Also removed the "modification" concept — subjective nudging about encouraged projects doesn't fit an agentic world. The board is the score. If a project has tickets, they get picked up.

### Claude Desktop

The session's climax: kairos works in Claude Desktop Cowork mode. All 6 skills visible as slash commands. Monk available as an agent.

Then: **scheduled tasks.** Monk on a cron.

- Kickoff: 6 AM Eastern, every day
- Shutdown: 11 PM Eastern, every night

The system runs itself. Morning kickoff queries ClickUp, pulls carryovers, writes the daily note. Evening shutdown captures completions, estimates intensity, names tomorrow's frog. No human initiation required.

### MCP Cleanup

Moved `mcp/clickup-daily-queue` out of agentic-factory to its own repo at `~/workspace/mcp-clickup`. The factory holds plugins, not MCP servers. Updated Claude Desktop config. Tested and verified.

## Key Learnings

1. **Flat structure is mandatory.** Skills as direct children of plugin root. No `skills/` nesting.
2. **Version bump on every change.** The cache keys on version. No bump = stale copies forever.
3. **Agents are conversational, not slash commands.** Different discovery model than skills.
4. **Agents compose skills.** Skills are knowledge. Agents are autonomous execution that reads that knowledge.
5. **Plugins work in Claude Desktop.** Same marketplace, same skills, same agents — plus scheduled tasks.
6. **The board is the score.** Agentic work is driven by the task board, not subjective nudging.

## Numbers

- 15 plugins restructured
- 168 files moved (flatten)
- 13 agents converted to skills
- 3 new autonomous agents created (Lenny, Slim, Monk)
- 1 MCP server extracted to standalone repo
- Kairos v2.0.0 with portable data folder
- 2 scheduled tasks running in Claude Desktop

## What's Next

- E2E greenfield test for kairos (ticket: 86e0fn02d)
- Bootstrap logic in Monk — auto-scaffold kairos/ if missing
- More agents: clickup agent, conduct → lenny migration complete, research-docs-fetcher
- Update CLAUDE.md quality standards to reflect agent patterns
