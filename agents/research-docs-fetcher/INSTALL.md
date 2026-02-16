# Installation Guide: Research Docs Fetcher Agent

## Quick Install

### For Claude Code

```bash
# Global installation (available everywhere)
cp -r agents/research-docs-fetcher ~/.claude/agents/

# Project-specific installation
cp -r agents/research-docs-fetcher .claude/agents/
```

### For Claude Web/Desktop

1. Navigate to Agents settings (if available)
2. Click "Add Custom Agent"
3. Upload `research-docs-fetcher.md`

## Verification

Test the installation:

```
User: "Research FastAPI documentation"

Claude: "I'll use the research agent to fetch FastAPI documentation..."
```

## Prerequisites

- Claude Code or Claude with Agents support
- Internet access for web fetching
- Write permissions for `ai_docs/research/` directory

## File Structure

```
research-docs-fetcher/
├── research-docs-fetcher.md  # Main agent definition
├── README.md                  # Overview
├── HOW_TO_USE.md             # Usage guide
└── INSTALL.md                # This file
```

## Agent Configuration

The agent is configured with:
- **Name**: research agent
- **Color**: Purple (research/knowledge)
- **Tools**: WebFetch, Read, Glob, Bash
- **Model**: Sonnet

## Directory Setup

The agent saves research to `ai_docs/research/`. Create it manually or let the agent create it:

```bash
# Manual creation (optional)
mkdir -p ai_docs/research

# Or let the agent create it automatically on first use
```

## Usage After Installation

Once installed, invoke the agent:

### Explicitly

```
"Use the research agent to fetch TypeScript documentation"
```

### Implicitly

Claude will suggest using the agent for research tasks:

```
User: "I need documentation for React Hooks"
Claude: "I'll use the research agent to gather React Hooks documentation..."
```

## Customization

### Change Output Directory

Edit `research-docs-fetcher.md` to customize the output location:

```markdown
# Default: ai_docs/research/
# Change to your preferred location:
docs/research/
references/external/
```

### Adjust Cache Duration

Default is 24 hours. To change:

```markdown
# In the workflow section, change:
- Skip files created within the last 24 hours
# To:
- Skip files created within the last [X] hours
```

### Add Default Sources

Pre-configure commonly used documentation sources:

```markdown
**Common Documentation Sources:**
- React: https://react.dev
- TypeScript: https://www.typescriptlang.org/docs
- FastAPI: https://fastapi.tiangolo.com
```

## Troubleshooting

### Agent Not Invoked

**Solutions:**
1. Explicitly request: "Use research agent to..."
2. Check file location: `ls ~/.claude/agents/research-docs-fetcher/`
3. Verify YAML frontmatter is valid
4. Restart Claude Code if using CLI

### Directory Permission Error

**Problem**: Cannot create `ai_docs/research/` directory

**Solutions:**
```bash
# Create directory manually
mkdir -p ai_docs/research

# Check permissions
ls -la ai_docs/

# Fix permissions if needed
chmod 755 ai_docs/research/
```

### WebFetch Not Working

**Problem**: Unable to fetch URLs

**Solutions:**
1. Check internet connection
2. Verify URL is accessible
3. Try fetching URL manually: `curl [URL]`
4. Some sites may block automated access

### Files Not Caching Properly

**Problem**: Agent re-fetches recent content

**Solutions:**
1. Check metadata comments in existing files
2. Ensure timestamps are properly formatted
3. Verify file naming consistency

## Team Installation

Share with your team:

### Option 1: Team Repository

```bash
# Add to team dotfiles
cp -r agents/research-docs-fetcher team-dotfiles/claude/agents/

# Team members install
cp -r team-dotfiles/claude/agents/research-docs-fetcher ~/.claude/agents/
```

### Option 2: Project-Level

```bash
# Install in project .claude/agents/
mkdir -p .claude/agents
cp -r agents/research-docs-fetcher .claude/agents/

# Add to version control
git add .claude/agents/research-docs-fetcher

# Add ai_docs to .gitignore (optional)
echo "ai_docs/" >> .gitignore
```

### Option 3: Shared Research Directory

```bash
# Use shared network location for research
# Edit agent to save to shared path:
/mnt/shared/team-research/

# All team members access same knowledge base
```

## .gitignore Recommendations

Consider adding to `.gitignore`:

```bash
# Research files (team preference)
ai_docs/research/

# Or keep in version control for team sharing
# and remove from .gitignore
```

## Workflow Integration

### Daily Research Routine

```bash
# Morning: Update key documentation
echo "Research morning update" > research-tasks.txt

# Invoke agent
# "Refresh all documentation in ai_docs/research/ (force refresh)"

# Review new content
ls -lt ai_docs/research/ | head
```

### Pre-Project Setup

```bash
# Before starting new project
# "Fetch documentation for [tech stack]"

# Verify all docs fetched
ls ai_docs/research/

# Begin development with full context
```

## Uninstall

```bash
# Remove agent
rm -rf ~/.claude/agents/research-docs-fetcher

# Optionally remove research files
rm -rf ai_docs/research/
```

## Support

For issues or questions:
- Review `HOW_TO_USE.md` for usage guidance
- Check examples for common research patterns
- Verify directory permissions
- Ensure internet access for WebFetch

---

Generated by Claude Code Skills Factory
