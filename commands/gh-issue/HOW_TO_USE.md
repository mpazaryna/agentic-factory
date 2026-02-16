# How to Use `/gh-issue`

The `/gh-issue` command fetches GitHub issue details and loads them into context for the coding agent to work with.

## Basic Usage

```bash
/gh-issue 123
```

This will:
1. Fetch issue #123 from the current repository
2. Display the full issue details (title, body, labels, etc.)
3. Extract key requirements and technical context
4. Present it in a format optimized for the coding agent

## Example Workflow

### Scenario: Implement a feature from GitHub issue

```bash
# Step 1: Load the issue into context
/gh-issue 456

# Step 2: Review the loaded issue details
# The command will display:
# - Issue title and description
# - Key requirements
# - Technical context
# - Implementation notes

# Step 3: Ask the coding agent to implement
"Based on the issue above, please implement the requested feature"
```

## What You Get

The command presents the issue in this structure:

```
# Issue #456: Add dark mode support

## Status
- State: open
- Labels: enhancement, frontend
- Assignee: @username
- Milestone: v2.0

## Description
[Full issue description with all formatting]

## Key Requirements
- Add toggle button in settings
- Persist user preference
- Apply theme across all pages

## Technical Context
- Files: src/components/Settings.tsx, src/theme/colors.ts
- API: Uses localStorage for persistence

## Implementation Notes
Need to update theme provider and add CSS variables for colors
```

## Prerequisites

- GitHub CLI (`gh`) must be installed
- You must be authenticated: `gh auth login`
- Command must be run from within a git repository

## Tips

- **Check issue exists**: The command will show an error if the issue doesn't exist
- **Private repos**: Works with private repositories if you're authenticated
- **Large issues**: For issues with many comments, the main body is prioritized
- **Cross-repo**: Currently works only for issues in the current repository

## Common Use Cases

1. **Feature implementation**
   ```bash
   /gh-issue 789
   # Then ask: "Implement this feature following the requirements"
   ```

2. **Bug fixing**
   ```bash
   /gh-issue 321
   # Then ask: "Debug and fix the issue described above"
   ```

3. **Code review context**
   ```bash
   /gh-issue 555
   # Then ask: "Review the PR linked to this issue"
   ```

## Troubleshooting

**Error: "gh: command not found"**
- Install GitHub CLI: https://cli.github.com/

**Error: "issue not found"**
- Check the issue number is correct
- Ensure you have access to the repository

**Error: "not in a git repository"**
- Navigate to your git repository first
- Or specify the repo with `gh issue view 123 --repo owner/repo`
