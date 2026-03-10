# Export Mode Template

Consolidate project documentation into numbered files for external LLM tools.

## Output Structure

Create the following files in `docs/exports/`:

```
docs/exports/
├── 01-project-overview.md        # CLAUDE.md content
├── 02-architecture-decisions.md  # All ADRs from .orchestra/decisions/
├── 03-architecture.md            # docs/architecture/*.md
├── 04-mlx-system.md              # docs/architecture/mlx-soap-generation.md
├── 05-devlog-current.md          # docs/devlog/2026-Q1/*.md
├── 06-devlog-archive.md          # docs/devlog/2025-Q3/*.md, docs/devlog/2025-Q4/*.md
├── 07-issues.md                  # .orchestra/specs/*.md
└── 08-uml.md                     # docs/uml/*.md
```

## Process

### Phase 1: Clear Output Directory

```bash
rm -rf docs/exports/*
mkdir -p docs/exports
```

### Phase 2: Generate Each File

For each output file:
1. Write a header describing the category
2. For each source file in the category:
   - Add separator: `---`
   - Add source header: `# Source: {relative_path}`
   - Add separator: `---`
   - Append file contents

### File Generation Details

#### 01-project-overview.md
```markdown
# Project Overview

This file consolidates the main project documentation and orientation materials.

---
# Source: CLAUDE.md
---

{CLAUDE.md content}
```

#### 02-architecture-decisions.md
**Sources**: `.orchestra/decisions/*.md`
```markdown
# Architecture Decision Records

Key architectural decisions documented as ADRs.

---
# Source: .orchestra/decisions/ADR-001-no-viewmodels-in-swiftui.md
---

{file content}

---
# Source: .orchestra/decisions/ADR-002-agentic-development-patterns.md
---

{file content}

... repeat for each ADR
```

#### 03-architecture.md
**Sources**: `docs/architecture/*.md`, `docs/architecture/*.md`
```markdown
# Architecture & Feature Documentation

Technical architecture documents, data models, and feature specifications.

{concatenated files with source headers}
```

#### 04-mlx-system.md
**Sources**: `docs/architecture/mlx-soap-generation.md`
```markdown
# MLX System Documentation

MLX model integration, SOAP generation workflow, and Apple Intelligence integration.

{concatenated files with source headers}
```

#### 05-devlog-current.md
**Sources**: `docs/devlog/2026-Q1/*.md`
```markdown
# Current Development Logs

Recent development logs and technical decisions.

{concatenated files with source headers}
```

#### 06-devlog-archive.md
**Sources**: `docs/devlog/archive/**/*.md`
```markdown
# Archived Development Logs

Historical development logs from previous quarters.

{concatenated files with source headers}
```

#### 07-specs.md
**Sources**: `docs/specs/*.md`
```markdown
# Issue Specs

Multi-session issue tracking and implementation specs.

{concatenated files with source headers}
```

#### 08-uml.md
**Sources**: `docs/uml/*.md`
```markdown
# UML Diagrams

Component and architecture diagrams.

{concatenated files with source headers}
```

## File Header Format

Each output file starts with:
```markdown
# {Category Title}

{Brief description of what this file contains.}
```

## Source File Format

Each source file is included as:
```markdown

---
# Source: {relative/path/to/file.md}
---

{file contents}
```

## Best Practices

1. **Run after major changes** - Regenerate when docs are significantly updated
2. **Verify file sizes** - Large files may need splitting for some tools
3. **Check for stale content** - Review before uploading to external tools
4. **Git-ignore exports** - Consider adding `docs/exports/` to `.gitignore` if regenerated frequently
