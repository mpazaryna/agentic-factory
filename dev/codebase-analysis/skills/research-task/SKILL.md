---
name: research-task
description: "Perform research on a technical topic and return structured findings with confidence levels, sources, and recommendations. Use when the user needs research on APIs, frameworks, libraries, or technical approaches."
context: fork
agent: general-purpose
allowed-tools: WebFetch, WebSearch, Read, Bash
argument-hint: "<research topic or question>"
---

# Research Task

Research $ARGUMENTS thoroughly and return structured findings.

## Workflow

### Step 1: Understand Research Scope

Parse the research questions:
- Primary questions (must answer)
- Secondary questions (nice to answer)
- Context (why it matters)

### Step 2: Identify Information Sources

Based on research questions, determine sources:
- **Official documentation** (API references, developer docs)
- **Technical articles** (developer blogs, Medium)
- **Code examples** (GitHub, Stack Overflow)
- **Community discussions** (forums, Reddit)

### Step 3: Gather Information

**Documentation**: Use WebFetch for official docs. Extract key concepts, APIs, limitations. Note version/compatibility requirements.

**Code Examples**: Search GitHub for relevant implementations. Look for patterns and best practices. Identify common pitfalls.

**Community Knowledge**: WebSearch for recent discussions. Find real-world experiences. Identify gotchas and workarounds.

### Step 4: Synthesize Findings

For each question:
- **Answer**: Direct answer if found
- **Details**: Supporting information
- **Sources**: Where information came from
- **Confidence**: High/Medium/Low
- **Caveats**: Limitations or conditions

### Step 5: Create Recommendations

- **Recommended approach**: What to do
- **Rationale**: Why this approach
- **Alternatives**: Backup options
- **Risks**: What to watch out for
- **Next steps**: How to proceed

## Design Principles

1. **Single Responsibility**: Only does research, doesn't write files
2. **Evidence-Based**: All claims backed by sources
3. **Actionable**: Provides clear recommendations
4. **Honest**: Admits when information not found or uncertain
