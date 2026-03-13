---
name: issue
description: "Fetch GitHub issue details and load into context for analysis and implementation. Use when the user wants to load a GitHub issue before working on it."
argument-hint: "<issue-number>"
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---

## Context

Current repository: !`gh repo view --json nameWithOwner -q .nameWithOwner`

## Your task

Fetch the full details of GitHub issue #$ARGUMENTS and present it in a structured format for analysis and implementation.

**Steps:**

1. **Fetch Issue Details**
   - Use `gh issue view $ARGUMENTS` to retrieve the complete issue.
   - Include title, body, labels, assignees, and milestone if present.
   - Capture any linked pull requests or related issues.

2. **Present for Context**
   - Display the issue in a clear, readable format.
   - Highlight key requirements and acceptance criteria.
   - Extract any code snippets, file references, or technical specifications.
   - Note any discussion points or clarifications from comments.

3. **Prepare for Implementation**
   - Summarize the main task and objectives.
   - List any dependencies or prerequisites mentioned.
   - Identify files or components likely to be affected.
   - Flag any edge cases or special considerations.

**Output Format:**

```
# Issue #$ARGUMENTS: [Title]

## Status
- State: [open/closed]
- Labels: [labels list]
- Assignee: [assignee if any]
- Milestone: [milestone if any]

## Description
[Full issue body with formatting preserved]

## Key Requirements
- [Extracted requirement 1]
- [Extracted requirement 2]

## Technical Context
[Any code snippets, file paths, API endpoints, or technical details]

## Implementation Notes
[Summary of what needs to be done]
```
