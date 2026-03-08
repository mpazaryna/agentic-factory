---
name: form-22a-report
description: Generate weekly business-focused progress summaries (Form 22-A) from GitHub data for non-technical stakeholders. Use when asked to create weekly reports, business summaries, progress assessments, or translate technical work into business impact. Focuses on shipped features and completed work only.
---

# Form 22-A: Weekly Operational Progress Assessment

## Instructions

You are being asked to generate a Form 22-A report - a weekly business-focused progress summary designed for non-technical stakeholders. These reports translate technical accomplishments into business value and impact.

The main audience is business partners, executives, and other non-technical stakeholders who want to understand what capabilities have been delivered and their impact on users. They need clear, jargon-free updates that can be quickly scanned in 30-60 seconds.

Form 22-A reports focus exclusively on:
- **Completed work** from the past week
- **Business capabilities** delivered (not technical implementation)
- **User impact** (how it helps end users)
- **Velocity metrics** (percentage complete, features shipped)

Form 22-A explicitly excludes:
- Future plans or upcoming work
- Timeline estimates or dates
- Technical implementation details
- Problems or blockers
- Work in progress

## Tools Available

Use GitHub CLI to gather data about completed work:

1. **GitHub Issues**: Pull recently closed issues to identify shipped features
   - Focus on issues closed within the past 7 days
   - Extract feature names and descriptions
   - Identify associated milestones

2. **Milestone Progress**: Track overall phase/sprint completion
   - Calculate percentage complete
   - Count closed vs open features
   - Track week-over-week progress

Always translate technical information into business language that non-technical stakeholders can understand.

## Workflow

1. **Determine time period**: Calculate the current week's date range (Monday to Sunday)

2. **Gather completed work data**:
```bash
   # Get recently closed issues
   gh issue list --state closed --limit 20 --json number,title,closedAt,labels,milestone
   
   # Get milestone progress
   gh api repos/{owner}/{repo}/milestones --jq '.[] | {title, open_issues, closed_issues}'
```

3. **Translate to business language**:
   - ❌ "Implemented SwiftData model with cascade delete"
   - ✅ "Users can now add and manage notes for their records"

4. **Generate the report**: Create a concise summary focusing on delivered value

5. **Update documentation**: Prepend new week to FORM-22-A.md, keeping last 6 weeks visible

## Formatting

The format follows strict guidelines for consistency and scannability:
```markdown
## Week of [Start Date] - [End Date], [Year]

**Phase [X] Progress:** [Y]% complete ([closed]/[total] features) ⬆️ from [previous]%

### ✅ What We Shipped This Week

**[Feature Name]** ✨
- [Business capability in plain English]
- [Another capability if applicable]
- **Impact:** [How this helps users/business]

**[Another Feature]** 📊
- [Business capability]
- **Impact:** [Business value]

### 📈 What This Means
- [High-level summary of progress]
- [Key milestone achieved if applicable]
- [Velocity/momentum indicator]

---
```

## Key Principles

### Language Translation
Always translate technical terms to business language:
- ❌ "API endpoint for record CRUD operations"
- ✅ "Staff can create, view, update, and remove records"

- ❌ "Implemented OAuth 2.0 authentication flow"
- ✅ "Secure login system for protecting user data"

### Focus Areas
- **Capabilities delivered**: What users can do now that they couldn't before
- **User impact**: Specific benefits to end users and staff
- **Business value**: How features improve workflow, efficiency, or service quality

### What to Exclude
- Technical implementation details
- Future work or plans (belongs in Form 22-C)
- Timeline estimates or target dates
- Problems, blockers, or challenges
- Work in progress or partially complete features

## Examples

### Good Example:
```markdown
## Week of October 14 - October 20, 2024

**Phase 1 Progress:** 55.6% complete (5/9 features) ⬆️ from 44.4%

### ✅ What We Shipped This Week

**User Activity History** ✨
- Users can view complete history of past activity
- Quick access to past records and details
- **Impact:** Reduces time spent searching through old records

**Automated Reminders** 📊
- Users receive text reminders 24 hours before scheduled events
- **Impact:** 30% reduction in no-shows expected

### 📈 What This Means
- System now handles core user workflows end-to-end
- Momentum increased with 2 major features shipped this week
- System ready for initial user testing
```

### Poor Example (too technical):
```markdown
## Week of October 14 - October 20, 2024

### Completed
- Refactored database schema for better normalization
- Added Redux state management for frontend
- Implemented WebSocket connections for real-time updates
- Fixed CSS grid layout issues
```

## Output

When generating a Form 22-A report:

1. Create the formatted report content
2. Save to FORM-22-A.md (prepending to existing content)
3. Provide a brief confirmation:
```
   Generated Form 22-A for Week of [dates]
   
   Summary:
   - [X] major features shipped
   - Phase [Y]: [Z]% complete
   - [Notable achievement or velocity metric]
   
   Added to: FORM-22-A.md
```

## Notes

- Use emojis sparingly but effectively for visual scanning (✨ new features, 📊 analytics, 🔧 improvements)
- Keep sections brief - entire report should be readable in 30-60 seconds
- Focus on "what's working now" rather than "what we built"
- Remember the audience likely has minimal technical knowledge
- Emphasize concrete benefits and practical impact
- Maintain consistent week-over-week format for easy comparison