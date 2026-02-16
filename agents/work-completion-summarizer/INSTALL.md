# Installation Guide: Work Completion Summarizer Agent

## Quick Install

### For Claude Code

```bash
# Global installation (available everywhere)
cp -r agents/work-completion-summarizer ~/.claude/agents/

# Project-specific installation
cp -r agents/work-completion-summarizer .claude/agents/
```

### For Claude Web/Desktop

1. Navigate to Agents settings (if available)
2. Click "Add Custom Agent"
3. Upload `work-completion-summarizer.md`

## Verification

Test the installation:

```
User: "Summarize the work I just completed"

Claude: "I'll use the work-completion-summary agent to document this..."
```

## Prerequisites

- Claude Code or Claude with Agents support
- Write permissions for `docs/devlog/` directory
- No external dependencies

## File Structure

```
work-completion-summarizer/
├── work-completion-summarizer.md  # Main agent definition
├── README.md                       # Overview
├── HOW_TO_USE.md                  # Usage guide
└── INSTALL.md                     # This file
```

## Agent Configuration

The agent is configured with:
- **Name**: work-completion-summary
- **Color**: Green (success/completion)
- **Description**: Proactive after work completion

## Directory Setup

The agent saves summaries to `docs/devlog/`. It will be created automatically, or you can create it manually:

```bash
# Manual creation (optional)
mkdir -p docs/devlog

# Or let the agent create it on first use
```

## Usage After Installation

Once installed, invoke the agent:

### Explicitly

```
"Use work-completion-summary to document this work"
```

### Implicitly (Proactive Trigger)

Claude will suggest using the agent after you complete work:

```
User: "I finished implementing the authentication system"
Claude: "Great! I'll use the work-completion-summary agent to document this..."
```

## Customization

### Set Your Name

Edit `work-completion-summarizer.md`:

```yaml
## Variables
USER_NAME: "Your Name"
```

### Change Output Directory

Default is `docs/devlog/`. To change:

```markdown
# In the instructions section, change:
Save to absolute path: `{current_directory}/docs/devlog/{YYYYMMDD}-{slug}.md`
# To:
Save to absolute path: `{current_directory}/your-directory/{YYYYMMDD}-{slug}.md`
```

### Adjust Summary Format

Modify the template in the agent definition:

```markdown
## Instructions
...
5. **Generate markdown**:
   - [Customize format here]
```

### Change Filename Pattern

Default: `YYYYMMDD-descriptive-slug.md`

To change:

```markdown
# Example: Add time
{YYYYMMDD}-{HHMM}-{slug}.md

# Example: Different date format
{YYYY-MM-DD}-{slug}.md

# Example: Category prefix
{category}-{YYYYMMDD}-{slug}.md
```

## Troubleshooting

### Agent Not Invoked

**Solutions:**
1. Explicitly request: "Use work-completion-summary to..."
2. Check file location: `ls ~/.claude/agents/work-completion-summarizer/`
3. Verify YAML frontmatter is valid
4. Restart Claude Code if using CLI

### Directory Permission Error

**Problem**: Cannot create `docs/devlog/` directory

**Solutions:**
```bash
# Create directory manually
mkdir -p docs/devlog

# Check permissions
ls -la docs/

# Fix permissions if needed
chmod 755 docs/devlog/
```

### Filename Too Long

**Problem**: Generated slug exceeds 40 characters

**Solutions:**
- Agent should auto-truncate, but you can specify shorter description
- Edit agent to increase limit if needed

### Summary Not Saved

**Problem**: Agent generates summary but doesn't save file

**Solutions:**
1. Check directory exists: `ls docs/devlog/`
2. Verify write permissions
3. Check disk space

## Team Installation

Share with your team:

### Option 1: Team Repository

```bash
# Add to team dotfiles
cp -r agents/work-completion-summarizer team-dotfiles/claude/agents/

# Team members install
cp -r team-dotfiles/claude/agents/work-completion-summarizer ~/.claude/agents/
```

### Option 2: Project-Level

```bash
# Install in project .claude/agents/
mkdir -p .claude/agents
cp -r agents/work-completion-summarizer .claude/agents/

# Add to version control
git add .claude/agents/work-completion-summarizer

# Keep devlog in version control
git add docs/devlog/
git commit -m "Add devlog entries"
```

### Option 3: Shared Devlog

```bash
# Use shared network location
# Edit agent to save to shared path:
/mnt/shared/team-devlog/{USER_NAME}/{YYYYMMDD}-{slug}.md

# All team members contribute to shared devlog
```

## Git Integration

### Track Devlog in Git

```bash
# Add devlog to version control
git add docs/devlog/
git commit -m "docs: add devlog entries"

# Or add to .gitignore if private
echo "docs/devlog/" >> .gitignore
```

### Automatic Commits

Create a git hook:

```bash
# .git/hooks/post-devlog
#!/bin/bash
git add docs/devlog/*.md
git commit -m "docs: update devlog $(date +%Y-%m-%d)"
```

## Workflow Integration

### Daily Routine

```bash
# Morning: Review yesterday's summary
cat docs/devlog/$(date -d yesterday +%Y%m%d)-*.md

# End of day: Summarize work
# Ask Claude: "Summarize today's work"

# Review and commit
git add docs/devlog/
git commit -m "docs: daily devlog"
```

### Sprint Planning

```bash
# Review sprint devlogs
ls docs/devlog/202411*.md

# Create sprint report
cat docs/devlog/202411*.md > sprint-11-summary.md
```

## Uninstall

```bash
# Remove agent
rm -rf ~/.claude/agents/work-completion-summarizer

# Optionally remove devlog
rm -rf docs/devlog/
```

## Support

For issues or questions:
- Review `HOW_TO_USE.md` for usage guidance
- Check examples for common patterns
- Verify directory permissions
- Customize agent definition as needed

---

Generated by Claude Code Skills Factory
