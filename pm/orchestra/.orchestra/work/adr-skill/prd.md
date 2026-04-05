---
status: draft
created_on: 2026-04-05
---

# ADR Skill

**Objective:** A dedicated `orchestra:adr` skill that agents use to write Architecture Decision Records with conforming frontmatter, correct numbering, and proper integration into the `.orchestra/adr/` folder.

## Success Criteria

- [ ] `orchestra:adr` skill exists with correct frontmatter
- [ ] Skill writes ADRs with `status: proposed`, `created_on`, and correct sequential numbering
- [ ] Skill reads existing ADRs to determine next number
- [ ] Skill links new ADR to the triggering work item
- [ ] Skill is referenced in conventions as the canonical way to write ADRs

## Context

ADR-001 consequences call for an `orchestra:adr` skill. Currently ADRs are written ad hoc. A skill standardizes numbering, frontmatter, and placement. It also formalizes the pattern that ADRs are written by agents during execution, not pre-planned.

## Materials

| Material | Location | Status |
|----------|----------|--------|
| adr skill | adr/SKILL.md | Not Started |
| plugin.json update | .claude-plugin/plugin.json | Not Started |
| conventions skill update | conventions/SKILL.md | Not Started |

## References

- [ADR-001: Artifact Frontmatter Contract](../../adr/ADR-001-artifact-frontmatter-contract.md)
