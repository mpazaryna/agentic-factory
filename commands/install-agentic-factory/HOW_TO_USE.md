# How to Use `/install-agentic-factory`

The `/install-agentic-factory` command copies components from the agentic-factory repo into your current project.

## Basic Usage

```
/install-agentic-factory <type> <name>
```

Where:
- `<type>` is one of: `skill`, `agent`, `command`
- `<name>` is the component name as it appears in the repo

## Examples

### Install a Skill

```
/install-agentic-factory skill cloudflare
```

This copies `skills/cloudflare/` from the factory repo to `.claude/skills/cloudflare/` in your current project. The skill becomes immediately available to Claude Code.

### Install an Agent

```
/install-agentic-factory agent research-agent
```

This copies `agents/research-agent/` to `.claude/agents/research-agent/`.

### Install a Command

```
/install-agentic-factory command gh-issue
```

This copies `commands/gh-issue/` to `.claude/commands/gh-issue/`.

## Available Components

### Skills
- `cloudflare` - Cloudflare Workers development
- `design-principles` - Design principles reference
- `design-review` - Design review workflows
- `dev-context` - Development context management
- `dev-explore` - Codebase exploration
- `dev-inquiry` - Technical inquiry workflows
- `dev-reports` - Development reporting
- `pytest` - Python testing with pytest
- `swift-lang` - Swift language development
- `swift-ui` - SwiftUI development
- `web-design` - Web design patterns
- `yoga-class-planner` - Yoga class planning

### Agents
- `github-pm-analyzer` - GitHub project management analysis
- `quality-control-enforcer` - Quality control workflows
- `research-agent` - Research and analysis
- `research-docs-fetcher` - Documentation research
- `work-completion-summarizer` - Work summary generation

### Commands
- `gh-issue` - GitHub issue fetching
- `plan-spec` - TDD plan from spec
- `rebuild-context` - Context rebuilding
- `rebuild-readme` - README generation
- `research` - Research tasks

## Configuration

### Source Path

The command resolves the factory repo in this order:
1. `$AGENTIC_FACTORY_HOME` environment variable
2. Default: `~/workspace/agentic-factory`

To set a custom path:
```bash
export AGENTIC_FACTORY_HOME=/path/to/agentic-factory
```

## Common Workflows

### Set Up a New Project

```
/install-agentic-factory skill dev-context
/install-agentic-factory skill dev-explore
/install-agentic-factory agent research-agent
/install-agentic-factory command gh-issue
```

### Add Testing Support

```
/install-agentic-factory skill pytest
/install-agentic-factory command plan-spec
```

## Troubleshooting

**"Source directory not found"**
- Check the component name matches what's in the repo
- Verify `$AGENTIC_FACTORY_HOME` points to the right location
- Run `ls ~/workspace/agentic-factory/skills/` to see available skills

**"Destination already exists"**
- The command will overwrite existing files
- Back up your local changes first if needed
