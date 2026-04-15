---
status: complete
created_on: 2026-04-05
---

# Frontmatter Contract

**Objective:** All orchestra-generated artifacts carry conforming YAML frontmatter so agents and bench can read metadata without parsing markdown prose.

## Success Criteria

- [x] ADR-001 written and accepted
- [x] PRD template uses `status: draft`, `ticket`, `created_on`
- [x] Spec template uses `status: draft`, `ticket`, `created_on`
- [x] Devlog examples use `created_on`
- [x] ADR reference template uses `status`, `created_on`
- [x] Scaffold emits frontmatter on milestone stubs and kickoff devlog
- [x] prd and spec skills document correct status vocabularies

## Context

Motivated by bench needing machine-readable metadata across all `.orchestra/` folders. Secondary driver: `ticket` field enables sub-agents to look up originating tickets at kickoff.

## Materials

| Material | Location | Status |
|----------|----------|--------|
| ADR-001 | .orchestra/adr/ADR-001-artifact-frontmatter-contract.md | Done |
| prd-template | references/prd-template.md | Done |
| spec-template | references/spec-template.md | Done |
| prd skill | prd/SKILL.md | Done |
| spec skill | spec/SKILL.md | Done |
| scaffold skill | scaffold/SKILL.md | Done |
| devlog examples | devlog/examples/ | Done |
| adr-000 reference | references/adr-000-the-score.md | Done |

## References

- ADR-001: Artifact Frontmatter Contract (.orchestra/adr/ADR-001-artifact-frontmatter-contract.md)
