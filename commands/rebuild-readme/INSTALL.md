# Installation Guide: Rebuild README Command

## Quick Install

### For Claude Code

```bash
# Global installation (available everywhere)
cp commands/rebuild-readme/rebuild_readme.md ~/.claude/commands/

# Project-specific installation
cp commands/rebuild-readme/rebuild_readme.md .claude/commands/
```

### Verify Installation

```bash
# List available commands
ls ~/.claude/commands/

# Should see: rebuild_readme.md
```

## Test the Installation

```
/rebuild-readme .
```

Should analyze current directory and create README.md.

## Prerequisites

- Claude Code CLI
- Bash command access (for file analysis)
- Read/Write permissions in project directory
- package.json or similar config files (helpful but not required)

## File Structure

```
rebuild-readme/
├── rebuild_readme.md  # Main command file
├── README.md          # Overview
├── HOW_TO_USE.md     # Usage guide
└── INSTALL.md        # This file
```

## Command Configuration

The command is configured with:
- **Name**: Rebuild README
- **Allowed Tools**: Bash, Read, Write
- **Description**: Generate developer-focused README.md

## Usage After Installation

Once installed, the command is available as:

```
/rebuild-readme [folder-path]
```

Examples:
```
/rebuild-readme .
/rebuild-readme ~/projects/my-app
/rebuild-readme /absolute/path/to/project
```

## Customization

### Change Generated Sections

Edit `rebuild_readme.md` to modify what sections are included:

```markdown
## Workflow
...
Analyze the target directory and create a README.md that includes:

1. **Project Overview** (keep/modify/remove)
2. **Getting Started** (keep/modify/remove)
3. **Architecture** (keep/modify/remove)
...
```

### Adjust Format/Style

Customize the markdown format:

```markdown
## Report

```markdown
# [Project Name]      # Change to ## or add emoji

[Description]

## 🚀 Getting Started  # Add/remove emojis

### Prerequisites     # Change heading levels
- Node.js            # Change list style
```

### Add Custom Sections

Include project-specific sections:

```markdown
9. **Security** (if applicable)
   - Security practices
   - Vulnerability reporting
   - Compliance notes

10. **Performance** (if applicable)
   - Performance benchmarks
   - Optimization tips
   - Monitoring setup
```

## Troubleshooting

### Command Not Found

**Problem**: `/rebuild-readme` not recognized

**Solutions:**
1. Verify file location: `ls ~/.claude/commands/rebuild_readme.md`
2. Check filename is exactly `rebuild_readme.md`
3. Restart Claude Code CLI
4. Try full path: `/rebuild-readme $(pwd)`

### Permission Denied

**Problem**: Cannot create README.md

**Solutions:**
```bash
# Check directory permissions
ls -la

# Ensure write access
chmod 755 .

# Check if README.md exists and is writable
chmod 644 README.md
```

### Overwrites Existing README

**Problem**: Accidentally overwrote custom README

**Solutions:**
```bash
# Restore from git (if tracked)
git checkout README.md

# Or restore from backup
cp README.md.backup README.md

# Prevention: Always backup first
cp README.md README.md.backup
/rebuild-readme .
```

**Best Practice**: Review diff before committing:
```bash
/rebuild-readme .
git diff README.md
# Keep changes you like, revert others
```

### Incomplete README

**Problem**: Generated README missing expected sections

**Solutions:**
1. Ensure project has package.json or equivalent
2. Add config files (tsconfig.json, jest.config.js, etc.)
3. Customize command to include more sections
4. Manually add missing sections after generation

## Team Installation

### Shared Installation

```bash
# Add to team dotfiles
cp commands/rebuild-readme/rebuild_readme.md team-dotfiles/claude/commands/

# Team members install
cp team-dotfiles/claude/commands/rebuild_readme.md ~/.claude/commands/
```

### Project-Specific

```bash
# Install in project
mkdir -p .claude/commands
cp commands/rebuild-readme/rebuild_readme.md .claude/commands/

# Commit to version control
git add .claude/commands/rebuild_readme.md
git commit -m "Add rebuild-readme command"

# Team members get it automatically
git pull
```

## Workflow Integration

### Project Template

Create project templates with the command:

```bash
# Create template directory
mkdir -p templates/react-app

# Add basic structure
cd templates/react-app
npm init -y
# ... set up project

# Generate README
/rebuild-readme .

# Save template
cd ../..
tar -czf react-app-template.tar.gz templates/react-app

# Use template for new projects
tar -xzf react-app-template.tar.gz
cd react-app
# Already has professional README!
```

### CI/CD (Optional)

**Warning**: Generally NOT recommended to auto-generate README in CI, but possible:

```yaml
# .github/workflows/docs.yml
name: Update Docs
on:
  workflow_dispatch:  # Manual trigger only

jobs:
  update-readme:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Generate README
        run: claude-code /rebuild-readme .
      - name: Create PR
        # Create PR with updated README for review
```

### VS Code Task

Add to `.vscode/tasks.json`:

```json
{
  "label": "Rebuild README",
  "type": "shell",
  "command": "claude-code",
  "args": ["/rebuild-readme", "${workspaceFolder}"],
  "group": "none",
  "problemMatcher": []
}
```

## Version Control Best Practices

### Backup Before Regenerating

```bash
# Always backup custom content
cp README.md README.md.backup

# Regenerate
/rebuild-readme .

# Review changes
diff README.md.backup README.md

# Merge custom sections if needed
vim README.md
```

### Commit Strategy

```bash
# Generate README
/rebuild-readme .

# Review changes carefully
git diff README.md

# Commit with clear message
git add README.md
git commit -m "docs: regenerate README with current project state"
```

### Preserve Custom Sections

If you have custom sections to preserve:

```bash
# Extract custom sections
sed -n '/## Custom Section/,/## Next Section/p' README.md > custom.txt

# Regenerate README
/rebuild-readme .

# Re-add custom sections
cat custom.txt >> README.md
```

## Uninstall

```bash
# Global installation
rm ~/.claude/commands/rebuild_readme.md

# Project-specific
rm .claude/commands/rebuild_readme.md
```

## Related Commands

Install both commands for complete documentation:

```bash
# Install rebuild-readme (stable docs)
cp commands/rebuild-readme/rebuild_readme.md ~/.claude/commands/

# Install rebuild-context (dynamic context)
cp commands/rebuild-context/rebuild_context.md ~/.claude/commands/

# Use together:
/rebuild-readme .      # Once or when structure changes
/rebuild-context .     # Daily or when context changes
```

## Common Use Cases

### New Open Source Project

```bash
# Set up project
npm init -y
# ... create code

# Generate professional README
/rebuild-readme .

# Add badges
# Add license
# Add contributing guidelines

# Publish
gh repo create --public
```

### Internal Documentation

```bash
# Generate README for internal service
/rebuild-readme .

# Customize for team
# Add internal links
# Add deployment procedures
# Add on-call procedures

# Share with team
git push
```

### Monorepo Packages

```bash
# Generate README for each package
for pkg in packages/*; do
  /rebuild-readme "$pkg"
done

# Each package has consistent documentation
```

## Support

For issues or questions:
- Review `HOW_TO_USE.md` for usage examples
- Check command definition for customization
- Verify file permissions
- Test with simple project first

---

Generated by Claude Code Skills Factory
