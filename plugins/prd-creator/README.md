# PRD Creator Plugin

A Claude Desktop plugin that guides users through creating clear, structured Product Requirements Documents (PRDs) for features, engagements, and product initiatives.

## Overview

The PRD Creator plugin provides a conversational, guided workflow for generating stakeholder-ready PRDs in 30 minutes. Instead of staring at a blank page or copying template text, users answer 8-10 focused questions and receive a complete, markdown-formatted PRD ready for review and iteration.

**Perfect for:** Product managers, technical leaders, founders, and anyone structuring a new feature or engagement.

## Features

✨ **Guided Q&A Workflow** - Answer 8-10 focused questions covering problem, goals, success metrics, user stories, and acceptance criteria

📋 **Structured Output** - Generates professional, markdown-formatted PRD with all required sections

✏️ **Edit & Refine** - Review the draft PRD and make edits before finalizing

💾 **Flexible Export** - Copy to clipboard, save as PRD.md file, or display for reference

🎯 **Mandatory Core Sections** - Ensures all critical sections (Problem, Goals, Success Metrics, User Stories, Acceptance Criteria) are filled before export

## Getting Started

### Installation

1. Install the PRD Creator plugin in Claude Desktop
2. The plugin will be available as a command

### Usage

Run `/prd` to start the guided PRD creation workflow:

```
/prd
```

The plugin will:
1. Welcome you and explain the workflow
2. Ask 8-10 focused questions (you can skip optional ones)
3. Generate a complete PRD from your answers
4. Show you a preview for review and editing
5. Export the final PRD as markdown

**Estimated time:** 20-30 minutes

### Example Workflow

```
You: /prd

Plugin: Welcome! Let's create a clear, structured PRD for your feature...
Plugin: [Q1] What problem are you solving?

You: Sales reps spend 30 min/day manually updating CRM...

Plugin: [Q2] Who are the primary users?

You: Sales reps and managers...

[... continue through Q10 ...]

Plugin: Here's your draft PRD:
---
# PRD: [Feature Name]
...
---

Would you like to edit anything before exporting?

You: Make the success metrics more specific

Plugin: [Updated metrics displayed]

Ready to export? Choose your option:
- Copy to clipboard
- Save as PRD.md file
- Display for reference
```

## PRD Structure

The generated PRD includes these sections:

**Required (Mandatory):**
- Problem Statement
- Goals (User + Business)
- Success Metrics
- User Stories
- Acceptance Criteria

**Optional:**
- Non-Goals
- Open Questions
- Timeline Considerations

All sections are filled from your Q&A answers. Optional sections only appear if you provide answers during the interview.

## Tips for Best Results

### Be Specific
- ❌ "Improve user experience"
- ✅ "Sales reps spend 30 min/day on manual data entry; we want to reduce it to 5 min"

### Define Success Concretely
- ❌ "Users will be happy"
- ✅ "80% of reps adopt the feature within 4 weeks; time saved averages 25 min/day"

### Focus on User Needs, Not Solutions
- ❌ "Build an AI-powered recommendation engine"
- ✅ "Sales managers can't spot at-risk deals until month-end; we need real-time visibility"

### Keep Scope Realistic
If the scope feels too large, the plugin will help you identify what's truly non-negotiable (v1) vs. what can defer to v2.

## Examples

See the plugin's reference materials for examples of:
- **Good PRDs** - Clear problem statement, measurable metrics, testable criteria
- **Problematic PRDs** - Vague goals, unmeasurable success, lack of scope boundaries
- **Feature-Specific Templates** - Patterns for common feature types (APIs, dashboards, integrations, etc.)

## Export Options

After reviewing your PRD, you can:

1. **Copy to Clipboard** - Copy the full PRD text and paste elsewhere
2. **Save as File** - Save as `PRD.md` to your computer for version control
3. **Display** - View in Claude for reference (can copy-paste from there)

The exported PRD is in clean markdown format, ready to share with stakeholders, engineers, or version control systems.

## Who Should Use This

- 👤 **Product Managers** - Structure feature requests before engineering handoff
- 🏢 **Founders** - Clarify product vision before team building
- 🛠️ **Technical Leaders** - Frame technical initiatives with clear goals and metrics
- 📋 **Project Leads** - Structure engagements or customer projects
- 🤝 **Cross-Functional Teams** - Get alignment on what "done" means

## Limitations & Scope

**This plugin focuses on PRD generation.** Downstream workflows are separate:

- ✅ Creates the PRD document
- ❌ Does not integrate with ClickUp, Jira, or other project tools
- ❌ Does not generate feature specs (that's a separate workflow)
- ❌ Does not generate UAT test cases (that's downstream)
- ❌ Does not generate code (engineer's job!)

**The PRD is the artifact.** Everything else consumes the PRD as input.

## Support & Feedback

If you have questions, feedback, or encounter issues:
- Review the plugin's reference materials (examples, tips, templates)
- Reach out to your Product team

---

**Ready to create your PRD?** Run `/prd` and let's get started!
