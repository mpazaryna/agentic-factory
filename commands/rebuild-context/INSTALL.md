# Installation Guide: Rebuild Context Command

## Quick Install

### For Claude Code

```bash
# Global installation (available everywhere)
cp commands/rebuild-context/rebuild_context.md ~/.claude/commands/

# Project-specific installation
cp commands/rebuild-context/rebuild_context.md .claude/commands/
```

### Verify Installation

```bash
# List available commands
ls ~/.claude/commands/

# Should see: rebuild_context.md
```

## Test the Installation

```
/rebuild-context .
```

Should analyze current directory and create CONTEXT.md.

## Prerequisites

- Claude Code CLI
- Bash command access (for file analysis)
- Read/Write permissions in project directory
- Git (optional, for better recent activity detection)

## File Structure

```
rebuild-context/
├── rebuild_context.md  # Main command file
├── README.md           # Overview
├── HOW_TO_USE.md      # Usage guide
└── INSTALL.md         # This file
```

## Command Configuration

The command is configured with:
- **Name**: Rebuild Context File
- **Allowed Tools**: Bash, Read, Write
- **Description**: Update CONTEXT.md with current project state

## Usage After Installation

Once installed, the command is available as:

```
/rebuild-context [folder-path]
```

Examples:
```
/rebuild-context .
/rebuild-context ~/projects/my-app
/rebuild-context /absolute/path/to/project
```

## Customization

### Change Output Filename

Edit `rebuild_context.md` to change the output file:

```markdown
# Default: CONTEXT.md
# Change to: PROJECT_CONTEXT.md, DEV_NOTES.md, etc.
```

### Adjust Sections

Customize what sections are included:

```markdown
## Workflow
...
Analyze the target directory and create a CONTEXT.md that includes:

1. **Active Work Areas** (keep/modify/remove)
2. **Quick Reference** (keep/modify/remove)
3. **Known Issues & Blockers** (keep/modify/remove)
...
```

### Change Recent Files Count

```markdown
# Default: last 10 files
- Files recently modified (last 10 files)

# Change to: last 20 files
- Files recently modified (last 20 files)
```

## Troubleshooting

### Command Not Found

**Problem**: `/rebuild-context` not recognized

**Solutions:**
1. Verify file location: `ls ~/.claude/commands/rebuild_context.md`
2. Check filename is exactly `rebuild_context.md`
3. Restart Claude Code CLI
4. Try full path: `/rebuild-context $(pwd)`

### Permission Denied

**Problem**: Cannot create CONTEXT.md

**Solutions:**
```bash
# Check directory permissions
ls -la

# Ensure write access
chmod 755 .

# Check if CONTEXT.md exists and is writable
chmod 644 CONTEXT.md
```

### No Recent Files Found

**Problem**: Says no recent activity

**Solutions:**
1. Ensure you're in correct directory
2. Check if git is initialized: `git status`
3. Verify files exist: `ls -la`
4. Try with absolute path: `/rebuild-context /full/path`

### Git Not Available

**Problem**: Command expects git but it's not installed

**Solutions:**
- Command falls back to file modification times
- Install git for better results: `brew install git` (macOS)
- Or modify command to only use file mtimes

## Team Installation

### Shared Installation

```bash
# Add to team dotfiles
cp commands/rebuild-context/rebuild_context.md team-dotfiles/claude/commands/

# Team members install
cp team-dotfiles/claude/commands/rebuild_context.md ~/.claude/commands/
```

### Project-Specific

```bash
# Install in project
mkdir -p .claude/commands
cp commands/rebuild-context/rebuild_context.md .claude/commands/

# Commit to version control
git add .claude/commands/rebuild_context.md
git commit -m "Add rebuild-context command"

# Team members get it automatically
git pull
```

## Workflow Integration

### Git Hooks

Add to `.git/hooks/post-merge`:

```bash
#!/bin/bash
# Auto-update context after pulling changes
claude-code /rebuild-context .
```

### Daily Automation

Add to cron or task scheduler:

```bash
# Crontab: Update context every morning at 9 AM
0 9 * * * cd ~/projects/my-app && claude-code /rebuild-context .
```

### VS Code Task

Add to `.vscode/tasks.json`:

```json
{
  "label": "Rebuild Context",
  "type": "shell",
  "command": "claude-code",
  "args": ["/rebuild-context", "${workspaceFolder}"],
  "group": "build"
}
```

## .gitignore Recommendations

**Option 1: Track CONTEXT.md (Recommended)**

```bash
# Commit for team visibility
# Don't add to .gitignore
git add CONTEXT.md
git commit -m "docs: update project context"
```

**Option 2: Ignore CONTEXT.md**

```bash
# Add to .gitignore for developer-specific context
echo "CONTEXT.md" >> .gitignore
```

Most teams benefit from tracking CONTEXT.md for shared awareness.

## Uninstall

```bash
# Global installation
rm ~/.claude/commands/rebuild_context.md

# Project-specific
rm .claude/commands/rebuild_context.md

# Remove generated file (optional)
rm CONTEXT.md
```

## Related Commands

Install related commands for complete documentation workflow:

```bash
# Also install rebuild-readme
cp commands/rebuild-readme/rebuild_readme.md ~/.claude/commands/

# Use together:
# /rebuild-readme . (stable documentation)
# /rebuild-context . (dynamic context)
```

## Support

For issues or questions:
- Review `HOW_TO_USE.md` for usage examples
- Check command definition for customization
- Verify file permissions and git availability

---

Generated by Claude Code Skills Factory
