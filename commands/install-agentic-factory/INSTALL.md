# Installation Guide for `/install-agentic-factory`

## Quick Install

### Global (Recommended - available in all projects)

```bash
mkdir -p ~/.claude/commands
cp commands/install-agentic-factory/install-agentic-factory.md ~/.claude/commands/
```

### For This Project Only

```bash
mkdir -p .claude/commands
cp commands/install-agentic-factory/install-agentic-factory.md .claude/commands/
```

## Prerequisites

### 1. Agentic Factory Repository

You need a local clone of the agentic-factory repo:

```bash
git clone <repo-url> ~/workspace/agentic-factory
```

### 2. Set Source Path (Optional)

By default, the command looks for the repo at `~/workspace/agentic-factory`. To use a different location, set the environment variable:

```bash
export AGENTIC_FACTORY_HOME=/path/to/agentic-factory
```

Add this to your `~/.zshrc` or `~/.bashrc` to make it permanent.

## Installation Steps

### Step 1: Copy Command File

```bash
# Global installation (recommended)
mkdir -p ~/.claude/commands
cp commands/install-agentic-factory/install-agentic-factory.md ~/.claude/commands/
```

### Step 2: Verify Installation

In Claude Code, type:
```
/install-agentic-factory
```

You should see usage instructions if no arguments are provided.

### Step 3: Test the Command

Navigate to any project and try:
```
/install-agentic-factory skill cloudflare
```

This should copy the cloudflare skill to `.claude/skills/cloudflare/` in that project.

## Uninstallation

```bash
# Global
rm ~/.claude/commands/install-agentic-factory.md

# Local
rm .claude/commands/install-agentic-factory.md
```

## File Locations

- **Command file**: `commands/install-agentic-factory/install-agentic-factory.md`
- **Local install**: `.claude/commands/install-agentic-factory.md`
- **Global install**: `~/.claude/commands/install-agentic-factory.md`
