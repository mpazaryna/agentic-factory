---
name: PRD Creator
description: Launch the guided PRD creation workflow to build a structured Product Requirements Document for your feature or engagement. Answer 8-10 focused questions to generate a complete, stakeholder-ready PRD in markdown format.
---

# /prd

Launch the guided PRD creation workflow.

## Workflow

1. **Welcome** - Explain what this command does and set expectations (8-10 questions, ~30 minutes, outputs a markdown PRD)
2. **Guided Questions** - Ask the following 8-10 questions in sequence, collecting detailed responses:
   - **Q1: Problem Statement** - "What problem are you solving? What pain point or gap does this address?"
   - **Q2: Target Users** - "Who are the primary users or stakeholders affected by this feature?"
   - **Q3: User Goals** - "What do users want to achieve? List 2-3 specific user-facing goals."
   - **Q4: Business Goals** - "What business outcomes matter? (revenue, efficiency, market position, etc.)"
   - **Q5: Success Metrics** - "How will you measure success? Define 2-3 concrete metrics."
   - **Q6: User Stories** - "Write 2-3 user stories in the format: 'As a [user], I want [action], so that [outcome].'"
   - **Q7: Key Requirements** - "What must the solution do? List 3-5 core functional requirements."
   - **Q8: Non-Goals** - "What is explicitly out of scope? (optional if time-constrained)"
   - **Q9: Constraints or Dependencies** - "Are there technical, timeline, or resource constraints? (optional)"
   - **Q10: Acceptance Criteria** - "How will you know this is done? Define success conditions."

3. **Generate PRD** - Using the PRD Template & Guidance skill, construct a complete PRD markdown document from the user's answers, including:
   - Sections from template: Problem Statement, Goals (User + Business), Non-Goals, User Stories, Requirements, Success Metrics, Open Questions, Timeline Considerations, Acceptance Criteria
   - All core sections (Problem, Goals, Success Metrics, User Stories, Acceptance Criteria) filled with user answers
   - Optional sections (Non-Goals, Open Questions, Timeline) included if answers provided
   - Professional formatting with headers, lists, and emphasis

4. **Preview & Edit** - Display the generated PRD in a readable format and offer options:
   - "Review the draft PRD below. Any edits or changes?"
   - Allow the user to request specific edits (e.g., "Make the success metrics more specific")
   - Make edits in-place until satisfied
   - When ready: "Ready to lock and export?"

5. **Lock & Export** - Once locked, offer export options:
   - **Copy to Clipboard** - Copy full PRD text to clipboard
   - **Save as File** - Save as `PRD.md` file to the user's machine
   - **Display** - Show the final PRD for reference
   - Provide clear confirmation of what was exported

## Key Behaviors

- **Conversational tone** - Be encouraging and clear. Explain why each question matters.
- **Honor core vs. optional** - Core sections (Problem, Goals, Success Metrics, User Stories, Acceptance Criteria) are mandatory before export; non-core sections are optional.
- **Flexible Q&A** - If user provides a detailed answer early, don't repeat. Adapt flow based on what's already been answered.
- **Quality over speed** - Spend time ensuring answers are substantive; a 30-minute conversation beats a rushed 10-minute one.
- **No jargon gatekeeping** - The PRD should be understandable by non-technical stakeholders; rephrase technical details when generating the markdown.

## Tool Requirements

- Use the "PRD Template & Guidance" skill to guide answers and structure output
- Bash or file export tools for saving PRD.md to disk
- No external API calls needed

## Success Criteria

- User completes guided Q&A (answering at least 8 core questions)
- Generated PRD includes all required sections filled with user data
- User can preview, edit, and export without friction
- Exported PRD is immediately usable by stakeholders/engineers without additional formatting work
