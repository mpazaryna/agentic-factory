# Continued Improvement Workflow Skill

## Purpose
After documentation alignment and baseline functionality verification, systematically identify and prioritize high-impact improvements across the code workflow pipeline—from MLX model injection through final result delivery—that address architectural or process bottlenecks rather than surface-level refactoring.

## Available Code

### `pab/pab/Kits/MLXKIt/.*`
**When to use:** Check for review

### `pab/pab/Kits/IntelligenceKit/.*`
**When to use:** Check for review

### `pab/pab/Kits/MLXKIt/.*`
**When to use:** Check for review

### `pab/pabTests/*`
**When to use:** Check for review

## When to Use
- After a codebase reaches documentation parity and functional baseline
- When results aren't meeting quality or performance expectations
- When looking for improvements that yield meaningful architectural or workflow shifts
- Before diving into routine maintenance or minor refactoring

## Core Philosophy
Step back from incremental tweaks. Surface and address the root constraints in the workflow pipeline that prevent reaching desired outcomes. This is about finding the systemic limitations, not polishing the edges.

## The Inquiry Framework

### Entry Point
"OK, now that we are in line with documentation—let's take a step back and push harder. We're still not generating the kind of result I'd like to see. What improvements in the workflow—from [start point] to [end point]—can be addressed? I'm looking for something big, not just a minor refactor."

### Analysis Dimensions

**Pipeline Segment Identification**
- Where does the work originate (model loading, data injection, request handling)?
- What intermediate transformations occur?
- Where does work conclude (output generation, validation, delivery)?
- What are the failure or degradation points?

**Bottleneck Classification**
- *Architectural*: System design limits scalability, extensibility, or correctness
- *Data Flow*: Information transformation or passing is inefficient or lossy
- *Abstraction*: Wrong level of abstraction creates friction or hidden complexity
- *Context Management*: State, dependencies, or scope handling creates blind spots
- *Integration*: Seams between components leak concerns or create fragmentation

**Impact Assessment**
- How does this bottleneck affect final result quality or behavior?
- What becomes possible if this constraint is removed or shifted?
- Is this a recurring problem across multiple code paths?
- What else currently works around this limitation?

## Improvement Categories (Big vs. Small)

### Big Improvements (Workflow-Level)
- Restructuring how models are injected or managed across the pipeline
- Reframing context passing or state management approach
- Consolidating fragmented logic into unified patterns
- Changing abstraction boundaries to align with domain concepts
- Shifting from pull-based to push-based information flow (or vice versa)
- Introducing missing intermediary processing stages
- Decoupling tightly-bound concerns

### Small Improvements (Local-Level)
- Variable naming or code organization
- Reducing function complexity through extraction
- Removing redundant checks or conditions
- Optimizing specific algorithms or loops

## Output Structure

When working through this workflow, produce:

1. **Pipeline Map**: Visual or textual representation of current flow from start to end
2. **Constraint Inventory**: Specific bottlenecks with justification for why they matter
3. **Root Cause Analysis**: What assumption, design decision, or limitation created each bottleneck?
4. **Improvement Proposals**: For each significant bottleneck, propose a restructuring (not a patch)
5. **Impact Hypothesis**: How would the results change if each bottleneck were addressed?
6. **Prioritization**: Which improvements have the highest leverage for the effort required?

## Questions to Guide Analysis

- What decision early in the workflow creates downstream constraints?
- Where is information transformed in a way that loses fidelity or context?
- What pattern repeats across multiple code paths as a workaround?
- If we removed this limitation, what would the architecture look like?
- Where does the code have to be "defensive" because of earlier design choices?
- What would need to change in the abstraction layers to make results better?
- Are there missing stages in the pipeline that other successful systems include?
- How coupled are concerns that should be independent?

## Integration with Claude Code Workflow

- Use this skill after `documentation-alignment` verification
- Deploy before detailed implementation sprints
- Treat findings as architectural guidance for subsequent changes
- Document decisions for the project record

## Success Criteria

- Identifies improvements that are *architectural*, not cosmetic
- Proposals address root causes, not symptoms
- Analysis connects workflow constraints to observable result quality issues
- Recommendations are actionable within your codebase's scale and scope