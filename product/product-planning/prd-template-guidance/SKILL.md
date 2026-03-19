---
name: PRD Template & Guidance
description: "Guide PRD creation with structured questions, quality checks, and best practices. Use when creating or refining Product Requirements Documents, defining acceptance criteria, or translating feature ideas into precise specifications."
---

# PRD Template & Guidance

This skill provides expert guidance for creating clear, stakeholder-ready Product Requirements Documents (PRDs). It encodes best practices for problem framing, goal setting, success metrics, and translating vague feature ideas into precise specifications.

## Core PRD Structure

A complete PRD contains these sections:

1. **Problem Statement** - The pain point or opportunity being addressed
2. **Goals** - User goals and business goals
3. **Non-Goals** - What is explicitly out of scope
4. **User Stories** - Concrete user-centric requirements
5. **Requirements** - Functional and non-functional requirements
6. **Success Metrics** - How success will be measured
7. **Open Questions** - Blocking or non-blocking questions to resolve
8. **Timeline Considerations** - Phasing, dependencies, constraints
9. **Acceptance Criteria** - Concrete "done" conditions

### Mandatory Sections (Must Have)
- Problem Statement
- Goals (User + Business)
- Success Metrics
- User Stories
- Acceptance Criteria

### Optional Sections (Nice to Have)
- Non-Goals
- Open Questions
- Timeline Considerations

## Question Guide for Q&A Workflow

When guiding users through PRD creation, ask these questions in sequence:

### Q1: Problem Statement
**Ask:** "What problem are you solving? What pain point, gap, or opportunity does this feature address? (Be specific—avoid vague language like 'improve efficiency.')"

**What makes a good answer:**
- Describes a real user pain or business gap
- Is specific (not "users need better features")
- Example: "Sales reps spend 30 min/day manually updating CRM; they want deal status to sync automatically from email"

**Red flag:** "Users want X feature" without explaining why

---

### Q2: Target Users & Stakeholders
**Ask:** "Who are the primary users or stakeholders affected by this feature? (List role, maybe count.)"

**What makes a good answer:**
- Identifies specific user personas or stakeholder groups
- Gives context (internal team, external customers, partners)
- Example: "Sales reps (50 people), sales managers (15 people), and C-level stakeholders who care about data accuracy"

**Red flag:** "Everyone" or "the whole company"

---

### Q3: User Goals
**Ask:** "What do users want to achieve with this feature? List 2-3 specific, user-centric goals."

**What makes a good answer:**
- Phrased from user perspective ("I want to...")
- Concrete and achievable
- Examples:
  - "Save 30 min/day on CRM updates"
  - "Have confidence that deal status is always current"
  - "Reduce manual data entry errors by 50%"

**Red flag:** "Build a sync feature" (that's the solution, not the goal)

---

### Q4: Business Goals
**Ask:** "What business outcomes matter for this feature? (Revenue, cost savings, efficiency, user retention, market position, risk reduction, etc.)"

**What makes a good answer:**
- Tied to organizational strategy
- Measurable
- Examples:
  - "Reduce churn by improving UX for sales teams"
  - "Increase deal close rate by 10% through better visibility"
  - "Save 200 hours/quarter in manual data entry"

**Red flag:** "Achieve product-market fit" (too broad) or "Be faster" (too vague)

---

### Q5: Success Metrics
**Ask:** "How will you measure success? Define 2-3 concrete metrics with targets."

**What makes a good answer:**
- Measurable and trackable
- Has a baseline and target
- Examples:
  - "CRM sync latency: <2 min (from 30 min manual)"
  - "Sales rep adoption: 80% within 4 weeks"
  - "Data accuracy: 99% match between email and CRM"
  - "Time saved per rep: avg 25 min/day"

**Red flag:** "Users will be happy" or "Improve performance" (not quantifiable)

---

### Q6: User Stories
**Ask:** "Write 2-3 user stories in the format: 'As a [role], I want [action], so that [outcome].'"

**What makes a good answer:**
- Follows standard user story format
- Describes specific user behavior, not system capability
- Examples:
  - "As a sales rep, I want deal status to auto-sync from email, so I don't have to manually update CRM"
  - "As a sales manager, I want to see real-time deal status, so I can prioritize team support"
  - "As a finance analyst, I want accurate deal data, so I can forecast revenue"

**Red flag:** "The system should sync data" (that's a requirement, not a user story)

---

### Q7: Key Requirements
**Ask:** "What must the solution do to meet the goals? List 3-5 core functional requirements."

**What makes a good answer:**
- Describes what the feature must do, not how
- Testable
- Examples:
  - "Detect deal updates in email attachments"
  - "Extract key fields (deal name, amount, close date) from email"
  - "Match email deals to existing CRM records"
  - "Sync updates back to CRM in <2 min"
  - "Notify user of conflicts if manual CRM entry differs from email"

**Red flag:** "Use machine learning" or "Build in the cloud" (those are implementation details)

---

### Q8: Non-Goals (Optional)
**Ask:** "What is explicitly out of scope for this feature? (What won't we build, and why?)"

**What makes a good answer:**
- Clarifies boundaries to prevent scope creep
- Explains why something is out of scope
- Examples:
  - "Not integrating with Salesforce API (we only read email)"
  - "Not handling custom CRM fields (only standard ones)"
  - "Not providing historical sync (only forward from launch date)"

**Red flag:** "None" or "Everything is in scope" (ask again!)

---

### Q9: Constraints or Dependencies (Optional)
**Ask:** "Are there technical, timeline, or resource constraints? Any dependencies on other teams?"

**What makes a good answer:**
- Identifies real blockers or limitations
- Examples:
  - "Must integrate with our email provider's API (they limit calls to 100/sec)"
  - "Engineering has 2 weeks available in Q2"
  - "Depends on IT team approving data handling policy by EOQ1"
  - "Sales team will pilot; needs <5 day turnaround for feedback"

**Red flag:** "No constraints" (there always are; dig deeper!)

---

### Q10: Acceptance Criteria
**Ask:** "How will you know this feature is done and successful? Define specific acceptance conditions."

**What makes a good answer:**
- Testable by QA and stakeholders
- Covers happy path and edge cases
- Examples:
  - "✓ 95% of emailed deals are matched and synced to CRM within 2 min"
  - "✓ Conflicts are logged and user is notified with action options"
  - "✓ 80% of sales team adopts feature within 4 weeks"
  - "✓ No data loss or duplication observed in UAT"
  - "✓ Performance impact on CRM <100ms latency added"

**Red flag:** "Users are happy" or "No bugs" (too vague; be specific)

---

## PRD Markdown Template

Use this structure when generating the final PRD markdown:

```markdown
# PRD: [Feature Name]

**Version:** 1.0
**Date:** [Current Date]
**Author:** [User Name]
**Status:** Ready for Review

---

## Problem Statement

[User's answer to Q1]

---

## Goals

### User Goals
[User's answer to Q3, formatted as list]

### Business Goals
[User's answer to Q4, formatted as list]

---

## Non-Goals

[User's answer to Q8, or "None for this version" if omitted]

---

## User Stories

[User's answer to Q6, formatted as list]

---

## Requirements

[User's answer to Q7, formatted as list]

---

## Success Metrics

[User's answer to Q5, formatted as list]

---

## Open Questions

[User can add any questions or ambiguities]

---

## Timeline Considerations

[User's answer to Q9, or TBD]

---

## Acceptance Criteria

[User's answer to Q10, formatted as checklist]

---

## Summary

[Brief summary: what's the feature, who benefits, why does it matter?]
```

## Common Pitfalls & How to Avoid Them

| Pitfall | What It Looks Like | How to Fix |
|---------|-------------------|-----------|
| **Vague problem** | "Users want better features" | Ask "What specifically frustrates them?" and "How much time/cost does it affect?" |
| **Solution-first thinking** | "We'll build an AI recommendation engine" | Ask "What user need does this solve?" and "Why a recommendation engine vs. other solutions?" |
| **Missing success metrics** | "We'll know it's done when it's shipped" | Ask "What will change for users?" and "How will you measure it?" |
| **Bloated requirements** | 20+ requirements listed | Ask "Which 3-5 are non-negotiable?" and defer others to v2 |
| **No acceptance criteria** | "It should work well" | Ask "What specific tests would pass?" and "What would fail?" |
| **Unrealistic timelines** | 2-week timeline for 3-month feature | Ask "What can we ship in 2 weeks?" and scope down |

## Tips for Facilitating Q&A

- **Listen actively** - Users often answer multiple questions in their first response; acknowledge and build on it
- **Dig deeper** - If an answer is vague, ask follow-up questions ("Tell me more..." or "Give me an example...")
- **Reflect back** - Summarize their answer to confirm understanding
- **Don't judge scope** - If they want too much, ask "If you could only pick 3, which would be non-negotiable?"
- **Make it conversational** - This is a dialogue, not a form; react naturally to their answers
- **Set realistic expectations** - "This will take ~30 min and produce a draft you can iterate on"

## Review Checklist

Before exporting the PRD, verify:

- [ ] Problem statement is specific (pain point or opportunity is clear)
- [ ] Goals are user-centric and business-aligned
- [ ] Success metrics are measurable with clear targets
- [ ] User stories follow the "As a / I want / so that" format
- [ ] Requirements are not redundant and cover the core functionality
- [ ] Acceptance criteria are testable and specific
- [ ] Non-goals clarify scope boundaries
- [ ] Timeline and constraints are realistic
- [ ] No jargon or unclear language (could a non-technical stakeholder understand it?)

---

## See Also

- `references/prd-examples.md` - Real examples of good vs. problematic PRDs
- `references/templates.md` - Customizable PRD templates for different feature types
