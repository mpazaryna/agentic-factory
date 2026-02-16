# Installation Guide: Research Agent

## Quick Install

### For Claude Code

```bash
# Global installation (available everywhere)
cp -r agents/research-agent ~/.claude/agents/

# Project-specific installation
cp -r agents/research-agent .claude/agents/
```

### For Claude Web/Desktop

1. Navigate to Agents settings (if available)
2. Click "Add Custom Agent"
3. Upload `research-agent.md`

## Verification

Test the installation:

```
User: "Research Python async/await patterns and save to docs"

Claude: "I'll use the research-agent to gather this information..."
```

## Prerequisites

- Claude Code or Claude with Agents support
- Internet access for web fetching
- No external dependencies required

## File Structure

```
research-agent/
├── research-agent.md           # Main agent definition
├── README.md                   # Overview
├── HOW_TO_USE.md              # Usage guide
└── INSTALL.md                 # This file
```

## Agent Configuration

The agent is configured with:
- **Name**: research-agent
- **Color**: Purple (research/exploration)
- **Tools**: WebFetch, Read, Glob, Bash
- **Model**: Sonnet (balanced performance)

## Usage After Installation

Once installed, the agent can be invoked:

### Explicitly

```
"Use the research-agent to gather documentation about GraphQL subscriptions"
```

### Implicitly

Claude will suggest using the agent when appropriate:

```
User: "I need to understand how WebSockets work"
Claude: "Let me use the research-agent to gather comprehensive documentation on WebSockets..."
```

## Customization

### Adjust Output Directory

Edit `research-agent.md` to change where files are saved:

```markdown
markdown files in the ai_docs/research directory.
```

Change to your preferred location:

```markdown
markdown files in the docs/research directory.
```

### Add Custom Metadata Fields

Modify the metadata section to include project-specific fields:

```markdown
- Add metadata header with:
  - Source URL
  - Fetch timestamp
  - Topic/category
  - Summary
  - [Your custom fields]
```

### Configure Refresh Policy

Adjust how long files are considered fresh:

```markdown
- Skip files created within the last 24 hours
```

Change to your preferred timeframe (e.g., "7 days", "1 week", "always refresh").

## Troubleshooting

### Agent Not Creating Files

**Problem**: Research runs but no files created

**Solutions:**
1. Check directory exists: `ls -la ai_docs/research/`
2. Verify write permissions
3. Check agent logs for errors
4. Ensure Bash tool is available

### Duplicate Content

**Problem**: Same content fetched multiple times

**Solutions:**
1. Agent should check existing files first
2. Explicitly request: "Check if we already have this research"
3. Review timestamp checking logic
4. Use `--force-refresh` in your request if needed

### Web Fetching Fails

**Problem**: Cannot fetch content from URLs

**Solutions:**
1. Verify internet connection
2. Check if URL is accessible
3. Some sites may block automated access
4. Try alternative URLs or official documentation

### Poor Markdown Formatting

**Problem**: Generated markdown is hard to read

**Solutions:**
1. The agent processes HTML to markdown automatically
2. Request specific formatting: "Use clear headings and code blocks"
3. Edit generated files to match your style
4. Provide feedback to improve agent instructions

## Team Installation

Share with your team:

### Option 1: Team Repository

```bash
# Add to team dotfiles
cp -r agents/research-agent team-dotfiles/claude/agents/

# Team members install
cp -r team-dotfiles/claude/agents/research-agent ~/.claude/agents/
```

### Option 2: Project-Level

```bash
# Install in project .claude/agents/
mkdir -p .claude/agents
cp -r agents/research-agent .claude/agents/

# Commit to version control
git add .claude/agents/research-agent
git commit -m "Add research agent for documentation gathering"
```

## Building a Research Library

Create a shared research directory:

```bash
# Project structure
mkdir -p ai_docs/research
git add ai_docs/research/.gitkeep

# Add to .gitignore if research is too large
echo "ai_docs/research/*.md" >> .gitignore

# Or commit research for team sharing
git add ai_docs/research/
git commit -m "Add research documentation"
```

## Integration with Workflow

### During Project Setup

```bash
# Research key technologies
"Research Next.js App Router best practices"
"Gather Tailwind CSS documentation"
"Find TypeScript strict mode guide"

# All saved to ai_docs/research/
```

### Before Implementing Features

```bash
# Research before coding
"Research OAuth 2.0 implementation patterns"
"Gather Stripe webhook integration docs"

# Reference during implementation
cat ai_docs/research/oauth-2-implementation.md
```

### Building Onboarding Docs

```bash
# Compile research for team
"Research our tech stack: React, Node.js, PostgreSQL"

# Share with new team members
ls ai_docs/research/
```

## Uninstall

```bash
# Global installation
rm -rf ~/.claude/agents/research-agent

# Project-specific
rm -rf .claude/agents/research-agent

# Remove research directory if needed
rm -rf ai_docs/research/
```

## Support

For issues or questions:
- Review `HOW_TO_USE.md` for usage guidance
- Check examples for common research patterns
- Adjust agent definition to match your needs

---

Generated by Claude Code Skills Factory
