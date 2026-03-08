# Example: Export Mode Output

This shows the expected output format for the `docs/exports/` files.

## Generated File Structure

```
docs/exports/
├── 01-project-overview.md        # ~30KB
├── 02-architecture-decisions.md  # ~50KB
├── 03-design-docs.md             # ~100KB
├── 04-mlx-system.md              # ~100KB
├── 05-devlog-current.md          # ~80KB
├── 06-devlog-archive.md          # ~300KB
├── 07-specs.md                   # ~20KB
└── 08-uml.md                     # ~10KB
```

---

## Example: docs/exports/02-architecture-decisions.md

```markdown
# Architecture Decision Records

Key architectural decisions documented as ADRs.

---
# Source: docs/adr/ADR-001-no-viewmodels-in-swiftui.md
---

# ADR-001: No ViewModels in SwiftUI

**Status:** Accepted
**Date:** December 2025
**Deciders:** Development Team

---

## Context

SwiftUI was designed with a different paradigm than UIKit. The MVVM pattern...

[full content of ADR-001]

---
# Source: docs/adr/ADR-002-agentic-development-patterns.md
---

# ADR-002: Agentic Development Patterns

**Status:** Accepted
**Date:** December 2025
**Deciders:** Development Team

---

## Context

AI-assisted development with Claude requires specific patterns...

[full content of ADR-002]

... continues for each ADR file
```

---

## Example: docs/exports/05-devlog-current.md

```markdown
# Current Development Logs

Recent development logs and technical decisions.

---
# Source: docs/devlog/2025-12-15-soap-format.md
---

# 2025-12-15: SOAP Format Standardization

## Summary
Implemented JSON format for SOAP notes with format indicator field...

[full devlog content]

---
# Source: docs/devlog/2025-12-18-mlx-integration.md
---

# 2025-12-18: MLX Integration Complete

## Summary
Verified MLX processors work with Apple Intelligence SOAP generation...

[full devlog content]

... continues for each devlog file
```

---

## Key Characteristics

1. **Numbered files** - Easy to upload in order
2. **Source headers** - Every included file identified by path
3. **Separator lines** - Clear boundaries between source files
4. **Category headers** - Each output file has descriptive title
5. **Concatenated content** - Full file contents preserved
6. **Relative paths** - Source paths relative to project root

## Usage

After running export mode:

1. Navigate to `docs/exports/`
2. Upload files to your LLM tool (NotebookLM, etc.)
3. Files are numbered for logical ordering
4. Source headers help trace content origin

## File Size Guidance

| File | Typical Size | Notes |
|------|-------------|-------|
| 01-project-overview | ~30KB | Just CLAUDE.md |
| 02-architecture-decisions | ~50KB | All ADRs |
| 03-design-docs | ~100KB | Design specs |
| 04-mlx-system | ~100KB | MLX documentation |
| 05-devlog-current | ~80KB | Recent logs |
| 06-devlog-archive | ~300KB | Historical logs |
| 07-specs | ~20KB | Issue specs |
| 08-uml | ~10KB | Diagrams |

**Total**: ~700KB across 8 files

Most LLM tools handle files up to 500KB-1MB each.
