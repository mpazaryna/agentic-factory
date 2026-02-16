# Installation Guide for `/gh-issue`

## Quick Install

### For This Project Only

```bash
cp commands/gh-issue/gh-issue.md .claude/commands/
```

### For All Projects (Global)

```bash
cp commands/gh-issue/gh-issue.md ~/.claude/commands/
```

## Prerequisites

Before using `/gh-issue`, ensure you have:

### 1. GitHub CLI (`gh`) installed

**macOS:**
```bash
brew install gh
```

**Linux:**
```bash
# Debian/Ubuntu
sudo apt install gh

# Fedora/RHEL
sudo dnf install gh
```

**Windows:**
```bash
winget install --id GitHub.cli
```

Or download from: https://cli.github.com/

### 2. Authenticate with GitHub

```bash
gh auth login
```

Follow the prompts to authenticate with your GitHub account.

### 3. Verify Installation

Test that `gh` is working:
```bash
gh --version
gh auth status
```

## Installation Steps

### Step 1: Copy Command File

**Local installation (this project only):**
```bash
# From the repository root
mkdir -p .claude/commands
cp commands/gh-issue/gh-issue.md .claude/commands/
```

**Global installation (all projects):**
```bash
# Works everywhere
mkdir -p ~/.claude/commands
cp commands/gh-issue/gh-issue.md ~/.claude/commands/
```

### Step 2: Verify Installation

In Claude Code, type:
```bash
/gh-issue
```

You should see the command is recognized. If you get an error about missing argument, that's correct - it means the command is installed!

### Step 3: Test the Command

Navigate to a git repository with GitHub issues and try:
```bash
/gh-issue 1
```

This should fetch and display issue #1 from your repository.

## Uninstallation

To remove the command:

**Local:**
```bash
rm .claude/commands/gh-issue.md
```

**Global:**
```bash
rm ~/.claude/commands/gh-issue.md
```

## Updating

To update to a newer version:

1. Delete the old file
2. Copy the new version using the installation commands above

## Troubleshooting

**Command not found after installation:**
- Restart Claude Code
- Check the file exists: `ls -la ~/.claude/commands/gh-issue.md`
- Verify file permissions: `chmod 644 ~/.claude/commands/gh-issue.md`

**Permission errors:**
```bash
chmod 644 commands/gh-issue/gh-issue.md
```

**Global vs Local:**
- **Local** (.claude/commands/): Only available in this project
- **Global** (~/.claude/commands/): Available in all projects
- Global commands take precedence over local ones

## File Locations

- **Command file**: `commands/gh-issue/gh-issue.md`
- **Local install**: `.claude/commands/gh-issue.md`
- **Global install**: `~/.claude/commands/gh-issue.md`
- **Usage guide**: `commands/gh-issue/HOW_TO_USE.md`
- **This file**: `commands/gh-issue/INSTALL.md`
