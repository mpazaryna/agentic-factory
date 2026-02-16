# Installation Guide: Goose Recipes Skill

## Quick Install

### For Claude Code

```bash
# Global installation (available in all projects)
cp -r generated-skills/goose-recipes ~/.claude/skills/

# Project-specific installation
cp -r generated-skills/goose-recipes .claude/skills/
```

### For Claude Web/Desktop

1. Navigate to Skills settings
2. Click "Add Custom Skill"
3. Upload entire `goose-recipes` directory (includes templates and references)

## Verification

Test the installation:

```
User: "Create a basic Goose recipe for code review"

Claude: "I'll create a Goose recipe using the basic template..."
```

## Prerequisites

- Claude Code or Claude with Skills support
- Goose AI agent framework (to run recipes)
- YAML knowledge helpful but not required (Claude assists!)

## File Structure

```
goose-recipes/
├── SKILL.md                              # Main skill definition
├── README.md                             # Overview
├── HOW_TO_USE.md                        # Detailed usage guide
├── INSTALL.md                           # This file
├── assets/                               # Recipe templates (required)
│   ├── basic-recipe-template.yaml       # Simple structure
│   ├── advanced-recipe-template.yaml    # Complex features
│   └── mcp-server-recipe-template.yaml  # HTTP MCP servers
└── references/                           # Documentation (required)
    └── recipe-structure.md              # Complete field reference
```

**Important:** Keep all directories together! The skill loads templates from `assets/` and references from `references/`.

## Install Goose Framework

To run the recipes Claude creates, install Goose:

```bash
# Using pipx (recommended)
pipx install goose-ai

# Or using pip
pip install goose-ai

# Verify installation
goose --version
```

## Verification Steps

### 1. Verify Skill Installation

```bash
# Check skill files are present
ls ~/.claude/skills/goose-recipes/

# Should show:
# SKILL.md  README.md  HOW_TO_USE.md  INSTALL.md  assets/  references/
```

### 2. Test Template Access

Ask Claude:
```
"Show me the basic Goose recipe template"
```

Claude should be able to read and display the template from `assets/basic-recipe-template.yaml`.

### 3. Create Test Recipe

```
User: "Create a simple Goose recipe that says hello"

Claude: [Creates recipe...]

# Save the output
cat > test-recipe.yaml

# Run with Goose
goose run --recipe test-recipe.yaml
```

## Customization

### Add Your Own Templates

Create custom templates in the `assets/` directory:

```bash
# Create a new template
cat > ~/.claude/skills/goose-recipes/assets/my-custom-template.yaml << 'EOF'
version: "1.0.0"
title: "My Custom Template"
description: "Template for my specific use case"

# Your template structure here
EOF
```

Update `SKILL.md` to reference it:
```yaml
## Recipe Templates

Ready-to-use templates in `assets/`:
- `basic-recipe-template.yaml` - Simple recipe structure
- `advanced-recipe-template.yaml` - Complex features showcase
- `mcp-server-recipe-template.yaml` - HTTP-based MCP servers
- `my-custom-template.yaml` - Custom use case  # NEW
```

### Add Reference Documentation

Add your own reference docs:

```bash
cat > ~/.claude/skills/goose-recipes/references/my-patterns.md << 'EOF'
# Common Recipe Patterns

## Pattern 1: Data Processing
...

## Pattern 2: Code Generation
...
EOF
```

## Integration with Goose

### Set Up MCP Servers

Many recipes use MCP (Model Context Protocol) servers for extended functionality:

```bash
# Example: Install GitHub MCP server
npm install -g @modelcontextprotocol/server-github

# Set environment variable
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"
```

### Configure Recipe Directory

Organize your recipes:

```bash
# Create recipes directory
mkdir -p ~/.goose/recipes

# Save recipes there
# Claude will help you create them
```

### Add to Path (Optional)

For easy recipe access:

```bash
# Add to your shell rc file (~/.bashrc or ~/.zshrc)
export GOOSE_RECIPES_DIR="$HOME/.goose/recipes"

# Create alias for quick recipe running
alias grecipe='goose run --recipe'

# Usage
grecipe ~/.goose/recipes/code-review.yaml --param file=app.py
```

## Troubleshooting

### Skill Not Recognized

**Problem:** Claude doesn't recognize the skill

**Solutions:**
1. Verify installation: `ls ~/.claude/skills/goose-recipes/SKILL.md`
2. Check YAML frontmatter in SKILL.md is valid
3. Try explicit: "Use goose-recipes skill to create a recipe"
4. Restart Claude Code if using CLI

### Templates Not Loading

**Problem:** Claude can't find templates

**Solutions:**
1. Verify assets directory: `ls ~/.claude/skills/goose-recipes/assets/`
2. Check file names match exactly:
   - `basic-recipe-template.yaml`
   - `advanced-recipe-template.yaml`
   - `mcp-server-recipe-template.yaml`
3. Ensure read permissions: `chmod +r ~/.claude/skills/goose-recipes/assets/*`
4. Re-copy entire directory (not just SKILL.md)

### Recipe Validation Errors

**Problem:** Created recipe fails validation

**Solutions:**
1. Ask Claude: "Validate this recipe for errors"
2. Check for common issues:
   - Missing required fields (version, title, description)
   - Template variables without parameters
   - Optional parameters without defaults
3. Reference documentation: "Show me the recipe structure reference"

### Goose Command Not Found

**Problem:** Can't run `goose` command

**Solutions:**
```bash
# Install Goose
pipx install goose-ai

# Or reinstall
pipx reinstall goose-ai

# Verify
which goose
goose --version
```

## Updating

To update the skill with new templates or documentation:

```bash
# Pull latest changes
cd claude-toolkit
git pull origin main

# Re-copy to skills directory
cp -r generated-skills/goose-recipes ~/.claude/skills/

# Verify update
ls -la ~/.claude/skills/goose-recipes/
```

## Uninstall

```bash
# Remove skill
rm -rf ~/.claude/skills/goose-recipes

# Optionally remove Goose framework
pipx uninstall goose-ai
```

## Team Installation

Share with your team:

### Option 1: Shared Repository

```bash
# Add to team's dotfiles
cp -r generated-skills/goose-recipes team-dotfiles/claude/skills/

# Team members install
git clone team-dotfiles
cp -r team-dotfiles/claude/skills/goose-recipes ~/.claude/skills/
```

### Option 2: Distribution Package

```bash
# Create package
cd generated-skills
tar -czf goose-recipes-skill.tar.gz goose-recipes/

# Share and extract
tar -xzf goose-recipes-skill.tar.gz -C ~/.claude/skills/
```

## Additional Resources

- **Goose Documentation**: https://github.com/square/goose
- **MCP Servers**: https://github.com/modelcontextprotocol
- **Recipe Examples**: See `references/recipe-structure.md` in the skill

## Support

For issues or questions:
- Review `HOW_TO_USE.md` for usage guidance
- Check templates in `assets/` directory
- Refer to `references/recipe-structure.md` for complete field documentation
- Ask Claude to debug specific recipe errors

---

Generated by Claude Code Skills Factory
