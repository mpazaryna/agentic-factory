# Portfolio Document Template

Generate a professional PROJECT.md suitable for portfolios, resumes, and technical interviews.

## Output File

Create `PROJECT.md` in project root.

## Analysis Phases

### Phase 1: Repository Discovery
- Identify project type (web app, CLI, library, mobile, etc.)
- Map directory structure
- Locate entry points and core modules
- Find configuration and build files

### Phase 2: Technology Stack
- Extract dependencies from manifests
- Identify frameworks from imports
- Catalog databases, APIs, services
- Note testing frameworks and tools
- Document deployment setup

### Phase 3: Architecture Understanding
- Identify patterns (MVC, microservices, etc.)
- Map component relationships
- Document system boundaries
- Analyze code organization

### Phase 4: Challenge Identification
- Look for complex algorithms
- Find performance optimizations
- Identify security implementations
- Note integration challenges

## Document Structure

```markdown
# [Project Name] - Project Portfolio

## Elevator Pitch
[2-3 sentences: What it does, who it's for, why it matters]

---

## Context & Problem

### The Problem
[What problem does this solve?]

### Domain Context
[Industry, user base, environment]

### User Needs
[Who uses this and what do they need?]

---

## Solution & Approach

### High-Level Solution
[How does this solve the problem?]

### Design Principles
- [Principle 1]: [How it's applied]
- [Principle 2]: [How it's applied]

---

## Technical Implementation

### Architecture

​```mermaid
flowchart TB
    A[Client] --> B[API]
    B --> C[Service Layer]
    C --> D[(Database)]
​```

[Architecture description]

### Technology Stack

| Category | Technology | Purpose |
|----------|------------|---------|
| Language | [Tech] | [Why chosen] |
| Framework | [Tech] | [Why chosen] |
| Database | [Tech] | [Why chosen] |
| Deployment | [Tech] | [Why chosen] |

### Key Design Decisions

#### Decision 1: [Title]
**Context**: [Why this decision was needed]
**Choice**: [What was chosen]
**Rationale**: [Why this choice]
**Trade-offs**: [What was sacrificed]

[Repeat for 2-3 key decisions]

---

## Key Features

- **[Feature 1]**: [Description and technical highlight]
- **[Feature 2]**: [Description and technical highlight]
- **[Feature 3]**: [Description and technical highlight]
- **[Feature 4]**: [Description and technical highlight]
- **[Feature 5]**: [Description and technical highlight]

[5-10 features, focus on technically interesting ones]

---

## Outcomes & Metrics

### Quantifiable Results
- [Metric 1]: [Number and context]
- [Metric 2]: [Number and context]

### Qualitative Impact
- [Impact 1]
- [Impact 2]

[If metrics unavailable, note "Metrics to be gathered" and focus on qualitative impact]

---

## Technical Challenges & Solutions

### Challenge 1: [Title]
**Problem**: [What was difficult]
**Approach**: [How you tackled it]
**Solution**: [What you built]
**Outcome**: [Result achieved]

### Challenge 2: [Title]
[Same structure]

### Challenge 3: [Title]
[Same structure]

[3-5 challenges, pick the most technically interesting]

---

## Learnings & Growth

### Technical Skills Developed
- [Skill 1]: [How it was developed through this project]
- [Skill 2]: [Specific application]

### Insights Gained
- [Insight 1]: [What you learned]
- [Insight 2]: [How it changed your approach]

---

## Future Enhancements

- [ ] [Enhancement 1]: [Brief description]
- [ ] [Enhancement 2]: [Brief description]
- [ ] [Enhancement 3]: [Brief description]

[Keep realistic and interesting]

---

## Project Links

- **Repository**: [GitHub URL]
- **Live Demo**: [URL if available]
- **Documentation**: [URL if available]

---

## Tags

`[tag1]` `[tag2]` `[tag3]` `[tag4]` `[tag5]`

[Include: languages, frameworks, patterns, domains]

---

## Portfolio Use Cases

### Resume Bullet Points
- [Action verb] [what] using [tech], resulting in [outcome]
- [Action verb] [what] with [tech] to achieve [result]

### Interview Talking Points
- **Architecture Question**: Discuss [specific pattern/decision]
- **Challenge Question**: Use [Challenge section] as example
- **Impact Question**: Reference [Outcomes section]

### LinkedIn Summary
[1-2 sentence version for LinkedIn project section]
```

## Writing Guidelines

### Tone
- Professional but not stiff
- Technical but accessible
- Confident but honest

### Content
- Focus on what YOU did
- Be specific, not vague
- Include concrete numbers where possible
- Acknowledge trade-offs

### What to Include
- Technical depth that demonstrates skill
- Problem-solving narrative
- Measurable outcomes
- Real challenges (not fake ones)

### What to Avoid
- Overstatement of impact
- Vague descriptions
- Obvious features (user can log in!)
- Pretending there were no challenges
