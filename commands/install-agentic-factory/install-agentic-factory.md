---
description: Install a skill, agent, or command from the agentic-factory repo into the current project
argument-hint: <type> <name> (e.g., skill cloudflare, agent research-agent, command gh-issue)
allowed-tools: Bash(cp:*), Bash(mkdir:*), Bash(ls:*), Bash(test:*), Bash(echo:*)
---

## Your Task

Install a component from the agentic-factory repository into the current project's `.claude/` directory.

**Arguments received:** `$ARGUMENTS`

The first word is the component type (`skill`, `agent`, or `command`) and the second word is the component name.

### Step 1: Parse Arguments

Extract two arguments from `$ARGUMENTS`:
- **type**: Must be one of `skill`, `agent`, or `command`
- **name**: The component name (e.g., `cloudflare`, `research-agent`, `gh-issue`)

If arguments are missing or the type is invalid, show usage:
```
Usage: /install-agentic-factory <type> <name>

Types: skill, agent, command

Examples:
  /install-agentic-factory skill cloudflare
  /install-agentic-factory agent research-agent
  /install-agentic-factory command gh-issue
```

### Step 2: Resolve Source Path

Determine the agentic-factory repo location:
1. Use `$AGENTIC_FACTORY_HOME` environment variable if set
2. Otherwise fall back to `~/workspace/agentic-factory`

The source path is `<repo>/<type>s/<name>/` (e.g., `skills/cloudflare/`, `agents/research-agent/`, `commands/gh-issue/`).

Verify the source directory exists. If not, list available components of that type and report the error.

### Step 3: Determine Destination

The destination depends on the component type:
- **skill** → `.claude/skills/<name>/` in the current working directory
- **agent** → `.claude/agents/<name>/` in the current working directory
- **command** → `.claude/commands/<name>/` in the current working directory

### Step 4: Copy Component

1. Create the destination directory if it doesn't exist: `mkdir -p <destination>`
2. Copy the entire component directory: `cp -R <source>/* <destination>/`
3. Verify the copy succeeded by listing the destination contents

### Step 5: Report Result

On success, display:
```
Installed <type> "<name>" to .claude/<type>s/<name>/

Files:
  <list of files copied>

The <type> is now available in this project.
```

For skills, remind the user the skill will be auto-detected by Claude Code.
For agents, remind them to reference the agent in their workflows.
For commands, remind them the command is now available as `/<name>` in this project.
