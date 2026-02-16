# How to Use the Research Docs Fetcher Agent

## Quick Start

Ask the agent to research topics or fetch URLs:

```
"Research FastAPI documentation and save to ai_docs/research"
"Fetch https://docs.stripe.com/api and organize it"
"Gather technical specs for Next.js 14"
```

## What This Agent Does

The Research Docs Fetcher systematically:
1. Parses your research request (URLs or topics)
2. Checks if content was recently fetched (24-hour cache)
3. Fetches new or stale content from the web
4. Converts to clean markdown format
5. Saves to `ai_docs/research/` with timestamps

## Workflow

### Step 1: Parse Input
Analyzes your request to determine:
- Direct URLs to fetch
- Research topics requiring web search
- Mix of both

### Step 2: Check Existing Content
For each URL or topic:
- Checks if `ai_docs/research/*.md` already exists
- Reads metadata comments for creation timestamp
- Skips files created within last 24 hours (unless forced refresh)

### Step 3: Fetch Content
- Uses WebFetch tool to retrieve content
- Processes HTML to markdown
- Preserves structure and formatting

### Step 4: Save Organized Files
- Creates descriptive filenames
- Adds metadata comments (timestamp, source URL)
- Saves to `ai_docs/research/` directory

## Usage Examples

### Example 1: Fetch Specific Documentation

```
User: "Fetch the Anthropic Claude API reference documentation"

Agent: I'll fetch the Claude API documentation.

1. Checking existing research files...
   - No existing file found for Claude API reference

2. Fetching content...
   - URL: https://docs.anthropic.com/claude/reference
   - Converting to markdown...

3. Saving to ai_docs/research/
   - File: claude-api-reference.md
   - Timestamp: 2024-11-14T13:45:00Z

✅ Documentation saved successfully!

Summary:
- Fetched: Claude API Reference
- Location: ai_docs/research/claude-api-reference.md
- Size: 45KB
```

### Example 2: Research a Topic

```
User: "Research FastAPI async patterns and best practices"

Agent: I'll research FastAPI async patterns for you.

1. Searching for: "FastAPI async patterns best practices"

2. Found relevant sources:
   - FastAPI official docs (async/await section)
   - Tutorial on async database operations
   - Best practices guide

3. Fetching content...
   - Fetching FastAPI async documentation
   - Fetching async patterns tutorial
   - Fetching best practices guide

4. Saving organized files:
   - ai_docs/research/fastapi-async-patterns.md
   - ai_docs/research/fastapi-async-db-operations.md
   - ai_docs/research/fastapi-async-best-practices.md

✅ Research complete! 3 files saved.
```

### Example 3: Avoid Re-Fetching Recent Content

```
User: "Fetch the TypeScript 5.0 release notes"

Agent: Checking existing research files...

Found existing file: ai_docs/research/typescript-5-0-release-notes.md
- Created: 6 hours ago (2024-11-14T07:30:00Z)
- Still fresh (within 24-hour window)

⏭️ Skipping fetch - using existing file.

To force refresh: "Fetch TypeScript 5.0 release notes (force refresh)"
```

### Example 4: Bulk Documentation Gathering

```
User: "Fetch documentation for React 18, Next.js 14, and Tailwind CSS 3"

Agent: I'll fetch documentation for all three frameworks.

1. Checking existing files...
   - react-18-docs.md: Not found
   - nextjs-14-docs.md: Found (12 hours old) - skipping
   - tailwind-css-3-docs.md: Not found

2. Fetching new content:
   - Fetching React 18 documentation...
   - Skipping Next.js 14 (recent)
   - Fetching Tailwind CSS 3 documentation...

3. Saving files:
   - ai_docs/research/react-18-docs.md (new)
   - ai_docs/research/nextjs-14-docs.md (existing)
   - ai_docs/research/tailwind-css-3-docs.md (new)

✅ 2 new files fetched, 1 existing file reused.
```

## File Organization

### Directory Structure

```
ai_docs/
└── research/
    ├── react-18-docs.md
    ├── fastapi-async-patterns.md
    ├── typescript-5-0-release-notes.md
    └── stripe-api-reference.md
```

### File Format

Each markdown file includes:

```markdown
<!--
Fetched: 2024-11-14T13:45:00Z
Source: https://docs.example.com/api
-->

# Page Title

[Clean markdown content here]
```

## Best Practices

### Do's ✅

- Provide specific URLs when possible
- Use descriptive topic names for research
- Let the agent organize files automatically
- Review fetched content for completeness
- Force refresh for rapidly changing docs

### Don'ts ❌

- Don't manually create files in ai_docs/research/
- Don't fetch entire websites (be specific)
- Don't ignore the 24-hour cache (saves bandwidth)
- Don't delete metadata comments (breaks caching)

## Force Refresh

To refresh recently fetched content:

```
"Fetch [URL/topic] (force refresh)"
"Refresh the FastAPI documentation even if recent"
```

## Integration with Workflow

### Before Starting New Project

```
# Research relevant technologies
"Fetch documentation for [framework], [library], [tool]"

# Build knowledge base
ls ai_docs/research/

# Reference during development
cat ai_docs/research/framework-docs.md
```

### During Development

```
# Need API reference
"Fetch latest Stripe API docs"

# Check what's already researched
ls ai_docs/research/

# Force update if outdated
"Refresh OpenAI API docs (force refresh)"
```

### For Learning

```
# Research new technology
"Research Rust async programming patterns"

# Gather tutorials
"Fetch beginner guides for GraphQL"

# Build reference library
# All organized in ai_docs/research/
```

## Common Questions

**Q: Where are files saved?**
A: `ai_docs/research/` directory (created automatically if needed)

**Q: How are files named?**
A: Agent creates descriptive kebab-case names from content titles

**Q: What if file already exists?**
A: Skipped if less than 24 hours old, otherwise refreshed

**Q: Can I fetch multiple URLs at once?**
A: Yes, provide a list: "Fetch [URL1], [URL2], [URL3]"

**Q: What formats are supported?**
A: Any web content that can be converted to markdown

**Q: How do I force refresh?**
A: Add "(force refresh)" to your request

## Tips for Effective Research

1. **Be Specific** - "FastAPI async patterns" vs "Python web frameworks"
2. **Use Direct URLs** - More reliable than topic search
3. **Batch Requests** - Fetch multiple related docs at once
4. **Check Existing** - Review ai_docs/research/ before fetching
5. **Force Refresh** - Use for rapidly changing documentation

## Error Handling

### URL Not Found

```
Agent: ⚠️ Unable to fetch https://example.com/docs
- Status: 404 Not Found
- Suggestion: Check URL and try again
```

### Content Conversion Issues

```
Agent: ⚠️ Partial conversion for [URL]
- PDF content may need manual review
- Some formatting lost in conversion
- File saved with available content
```

### Permission Issues

```
Agent: ⚠️ Cannot create ai_docs/research/ directory
- Check directory permissions
- Ensure write access to project
```

## Related Agents

- **quality-control-enforcer** - Review fetched documentation quality
- **work-completion-summarizer** - Summarize research gathering work

---

Generated by Claude Code Skills Factory
