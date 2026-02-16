# How to Use the Work Completion Summarizer Agent

## Quick Start

After completing work, invoke the agent:

```
"Summarize what I just accomplished"
"Create a devlog for the authentication feature"
"Document today's work on the payment integration"
```

## What This Agent Does

Creates ultra-concise summaries that:
1. Capture what was accomplished (1 sentence)
2. Generate descriptive filename slugs
3. Suggest next logical steps
4. Save to chronological devlog

## Summary Format

Each summary includes:
- **Achievement** - What was done (1 sentence max)
- **Next Steps** - 1 logical next action
- **Timestamp** - Automatic date-based filename

## Usage Examples

### Example 1: Feature Completion

```
User: "I just finished implementing OAuth2 authentication. Can you summarize this work?"

Agent: Creating work summary...

**Achievement:**
Implemented OAuth2 authentication with Google and GitHub providers, including token refresh and session management.

**Next Steps:**
- Add multi-factor authentication support

✅ Summary saved to: docs/devlog/20241114-oauth2-authentication-implementation.md

Summary generated successfully!
```

### Example 2: Bug Fix

```
User: "Fixed the memory leak in the image processor"

Agent: Documenting bug fix...

**Achievement:**
Resolved memory leak in ImageProcessor by adding weak self references and proper cleanup in deinit.

**Next Steps:**
- Add memory regression test to CI

✅ Summary saved to: docs/devlog/20241114-image-processor-memory-leak-fix.md
```

### Example 3: Refactoring Work

```
User: "Summarize the database migration work"

Agent: Creating summary...

**Achievement:**
Migrated PostgreSQL from v14 to v15, optimized 12 slow queries, and implemented connection pooling.

**Next Steps:**
- Monitor query performance metrics

✅ Summary saved to: docs/devlog/20241114-postgresql-migration-optimization.md
```

### Example 4: Daily Work Summary

```
User: "Summarize today's work on the dashboard"

Agent: Documenting daily progress...

**Achievement:**
Built responsive dashboard with real-time metrics, charts, and export functionality using React and D3.

**Next Steps:**
- Add filtering and date range selection

✅ Summary saved to: docs/devlog/20241114-dashboard-real-time-metrics.md
```

## File Naming

### Automatic Slug Generation

The agent creates descriptive slugs from your work:

| Work Description | Generated Filename |
|-----------------|-------------------|
| "OAuth2 authentication" | `20241114-oauth2-authentication-implementation.md` |
| "Memory leak fix" | `20241114-memory-leak-fix.md` |
| "Dashboard UI" | `20241114-dashboard-ui-development.md` |
| "API endpoints" | `20241114-api-endpoints-creation.md` |

### Rules for Slugs

- Kebab-case (lowercase with hyphens)
- Under 40 characters
- Descriptive and specific
- Understandable without opening file

## Directory Structure

```
docs/
└── devlog/
    ├── 20241110-user-authentication-oauth2.md
    ├── 20241111-payment-stripe-integration.md
    ├── 20241112-dashboard-ui-components.md
    ├── 20241113-api-rate-limiting.md
    └── 20241114-database-optimization.md
```

## Summary Content Format

Each file contains:

```markdown
# [Descriptive Title]

## Achievement
[1 sentence describing what was accomplished]

## Next Steps
- [Logical next action]

---
Created: 2024-11-14
```

## Best Practices

### Do's ✅

- Summarize after completing significant work
- Be specific about what was accomplished
- Let agent generate descriptive filenames
- Review suggested next steps
- Build chronological development history

### Don'ts ❌

- Don't write summaries manually (let agent do it)
- Don't use vague descriptions
- Don't skip summarizing completed work
- Don't delete old summaries (they're your history)

## Integration with Workflow

### Standard Development Cycle

```
1. Complete feature/bug fix
2. Invoke work-completion-summarizer
3. Review generated summary
4. Commit both code and summary
5. Move to suggested next step
```

### Daily Routine

```
# End of day
"Summarize today's work"

# Review devlog
ls -lt docs/devlog/ | head -5

# Plan tomorrow based on next steps
cat docs/devlog/$(date +%Y%m%d)-*.md
```

### Sprint Retrospective

```
# Review sprint work
ls docs/devlog/202411*.md

# Create sprint summary from devlog
cat docs/devlog/202411*.md > sprint-summary.md
```

## Customization

### Change User Name

Edit the agent definition:

```yaml
## Variables
USER_NAME: "Your Name"
```

### Change Directory

Default is `docs/devlog/`. To change:

```markdown
# In agent definition, change:
docs/devlog/{YYYYMMDD}-{slug}.md
# To:
your-directory/{YYYYMMDD}-{slug}.md
```

### Adjust Summary Length

Default is 1 sentence. For more detail, request explicitly:

```
"Create a detailed summary of today's work"
```

## Common Questions

**Q: Where are summaries saved?**
A: `docs/devlog/` directory (created automatically if needed)

**Q: What if I want more detail?**
A: Request it: "Create a detailed summary with technical notes"

**Q: Can I edit summaries after creation?**
A: Yes, they're markdown files you can edit freely

**Q: How far back do summaries go?**
A: They're kept chronologically - review with `ls docs/devlog/`

**Q: Can I delete old summaries?**
A: Yes, but they provide valuable project history

**Q: What if filename already exists?**
A: Agent will create unique name or ask for clarification

## Advanced Usage

### Weekly Summaries

```
# Combine week's devlogs
cat docs/devlog/2024111*.md > weekly-summary.md
```

### Project Timeline

```
# View chronological project history
ls -lt docs/devlog/*.md

# Create timeline visualization
# Use devlog filenames to build project timeline
```

### Team Sharing

```
# Share relevant devlogs
cp docs/devlog/20241114-api-design.md team-docs/

# Or commit to version control
git add docs/devlog/
git commit -m "Add devlog for API design work"
```

## Error Handling

### Directory Creation Issues

```
Agent: ⚠️ Cannot create docs/devlog/ directory
- Checking permissions...
- Creating directory: docs/devlog/
- Retry summary generation
```

### Filename Conflicts

```
Agent: ⚠️ File already exists: docs/devlog/20241114-feature.md
- Suggestion: Use more specific description
- Or: Append time: 20241114-1430-feature.md
```

## Tips for Better Summaries

1. **Be Specific** - "OAuth2 authentication" not "worked on auth"
2. **Include Tech** - "React dashboard with D3 charts" not "built dashboard"
3. **Mention Outcomes** - "Fixed memory leak, reduced usage 77%" not "fixed bug"
4. **List Key Features** - "Added X, Y, Z" provides more context
5. **Update Next Steps** - Help future you know what to do

## Related Agents

- **quality-control-enforcer** - Review work before summarizing
- **research-docs-fetcher** - Research before starting next steps

---

Generated by Claude Code Skills Factory
