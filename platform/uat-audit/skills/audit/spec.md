# Spec: UAT Folder Organization & Autonomous Enforcement

**Status:** Draft
**Date:** 2026-03-06
**Owner:** paz
**ClickUp:** TBD
**ADR Reference:** ADR-023 (UAT Documentation and Guide Composition)

---

## Problem Statement

The `docs/uat/` folder currently contains 55+ test case files that serve dual purposes: UAT testing documentation and source content for generated user guides. As the app grows, new UAT files will be added regularly. Without explicit, machine-readable standards and automated enforcement, the folder will accumulate inconsistencies that break downstream automation (guide composition, coverage tracking) and create friction for agents working independently.

Engineers currently maintain UAT files manually—adding walkthroughs, updating manifest entries, ensuring naming conventions are consistent. This manual process is error-prone and creates invisible coupling between file structure, naming, and guide definitions.

**Cost of inaction:** Guides will fail to compose correctly when UAT files don't conform to standards, coverage gaps will go undetected, and agents will lack clear guidance on where new files belong and how to structure them.

---

## Goals

1. **Enable agents to autonomously create and update UAT files** — Agents should be able to add new test cases, update walkthroughs, and maintain manifest entries without human intervention for structural/organizational decisions.

2. **Maintain 100% coverage tracking** — Every UAT file is accounted for in `docs/guides/manifest.json`. Uncovered files are automatically detected.

3. **Enforce a single gold-standard format** — All UAT files follow the ADR-023 structure (Walkthrough, Steps, Notes) with no variance or dead-weight sections.

4. **Enable automated remediation** — An agent (or CI) can audit the folder, find violations, and fix them without human approval for structural corrections (file naming, section ordering, manifest entries).

5. **Support guide composition without manual intervention** — The `compose-guide.py` script should always work correctly, extracting walkthroughs and generating guides with no errors due to malformed UAT files.

---

## Non-Goals

- **Real-time validation during editing** — We are not building a pre-commit hook or live linting system for individual editors (too much overhead for manual editing).
- **Distributed ownership across teams** — This spec assumes engineers own the `docs/uat/` folder. Non-technical stakeholders (designers, PMs, domain experts) do not edit UAT files directly; they provide content via the project tracker, and engineers translate it into UAT format.
- **Versioning or branching strategy for UAT files** — Files follow a single version (git history tracks changes). No parallel versions or feature branches of test cases.
- **Audit trails or change attribution** — UAT files are not test tracking sheets. We do not track "who tested this" or "when was it last tested" (git commits handle attribution).
- **Ordering or sequencing of UAT files** — Guides define ordering via manifest; individual UAT files are not sequenced.

---

## User Stories

### Agents
- **As an agent building a new feature**, I want a clear specification for how to create a new UAT file so that I can add it to the folder in the correct location, with the correct name and format, and update the manifest without human guidance.
- **As an agent auditing the UAT folder**, I want a programmatic way to detect violations (malformed files, missing manifest entries, orphaned files) so that I can generate a report or auto-fix them.
- **As an agent composing guides**, I want to guarantee that every UAT file in the folder conforms to the gold standard so that `compose-guide.py` never fails due to file format issues.

### Engineers (Manual Maintenance)
- **As an engineer updating an existing test case**, I want to know which sections are required, which are optional, and in what order they should appear so that I maintain consistency with other files.
- **As an engineer adding a new guide**, I want a template for updating `docs/guides/manifest.json` so that I do not accidentally create invalid JSON or forget required fields.
- **As an engineer reviewing a PR that touches UAT files**, I want to be able to spot format violations at a glance (e.g., missing `## Walkthrough`, wrong file name) so that I can ask for fixes before merging.

---

## Requirements

### P0: Must-Have (Feature Cannot Ship Without)

#### R1: File Naming Convention
**Description:** Every UAT file follows the pattern `{id}-{title}.md` where:
- `{id}` is a numeric ID (3-4 digits) that maps to `docs/guides/manifest.json`
- `{title}` is a URL-safe kebab-case slug (lowercase, hyphens only, no spaces or special chars)
- Examples: `101-app-opens.md`, `304-generate-soap.md`, `1404-quit-relaunch.md`

**Acceptance Criteria:**
- [ ] All files in `docs/uat/` match the pattern `^\d{3,4}-[a-z0-9-]+\.md$`
- [ ] No spaces, underscores, or special characters in filenames
- [ ] ID portion is unique across all files (no duplicates)
- [ ] Title slug matches the heading text in the file (case-insensitive comparison)

**Rationale:** Consistent naming enables reliable file discovery and ID extraction. Agents can parse filenames to populate manifest entries.

---

#### R2: Gold-Standard File Format (ADR-023)
**Description:** Every UAT file contains exactly these sections in this order:
1. Markdown heading: `# {id} — {Title}` (with em dash, not hyphen)
2. `## Walkthrough` section (required, min. 100 words describing the feature for end users)
3. `## Steps` section (required, numbered test steps)
4. `## Notes` section (optional, edge cases and platform caveats)

No other sections allowed. No metadata block, no `## Results`, no `## Expected Results`.

**Acceptance Criteria:**
- [ ] File starts with `# {id} — {Title}` heading (exact format with em dash)
- [ ] `## Walkthrough` section exists and contains >100 words
- [ ] `## Steps` section exists and contains numbered or scenario-grouped steps
- [ ] `## Notes` section is optional but, if present, contains relevant context
- [ ] No sections appear after `## Notes` (or after `## Steps` if Notes is absent)
- [ ] No metadata block (no `Priority:`, `Status:`, `Last Updated:`, `ClickUp:` fields)
- [ ] No `## Results` or `## Expected Results` sections

**Rationale:** ADR-023 defines the gold standard. Enforcing it ensures `compose-guide.py` can reliably extract content.

---

#### R3: Manifest Coverage (docs/guides/manifest.json)
**Description:** Every UAT file ID must appear in at least one guide definition in `manifest.json`. The manifest is the source of truth for which UAT files are "known to the system."

**Acceptance Criteria:**
- [ ] `manifest.json` is valid JSON
- [ ] For every `{id}-*.md` file in `docs/uat/`, that ID appears in at least one guide's `ids` array
- [ ] For every ID in the manifest, a corresponding `{id}-*.md` file exists in `docs/uat/`
- [ ] No duplicate IDs within a single guide
- [ ] IDs in the manifest are sortable (lexicographic ordering is readable)

**Rationale:** Coverage tracking prevents orphaned files and ensures all features are included in at least one guide. Bidirectional checking (files -> manifest and manifest -> files) catches both missing files and stale manifest entries.

---

#### R4: Walkthrough Content Quality
**Description:** The `## Walkthrough` section is the primary deliverable for guide composition. It must be written for end users (not developers), be self-contained, and clearly explain the feature.

**Acceptance Criteria:**
- [ ] Walkthrough is written in plain English, not technical jargon (or jargon is explained)
- [ ] Walkthrough explains "what it does" and "how to get there" clearly
- [ ] Walkthrough is self-contained (reader doesn't need to read other UAT files to understand)
- [ ] Walkthrough includes screenshot references where helpful (format: `![description](../screenshots/filename.png)`)
- [ ] Walkthrough is >100 words but <1000 words (concise but complete)
- [ ] No cross-references to other UAT files (too brittle)

**Rationale:** Walkthrough text is extracted verbatim into guides. Poor quality walkthroughs result in poor guides.

---

#### R5: Steps Section Clarity
**Description:** The `## Steps` section defines test steps. Steps should be numbered and grouped by scenario (A, B, C) when a feature has multiple test paths.

**Acceptance Criteria:**
- [ ] Steps are numbered (1, 2, 3... or 1A, 2A, 1B, 2B... for scenarios)
- [ ] Each step is a concise, single action ("tap X", "verify Y appears")
- [ ] Steps use imperative mood ("tap", "enter", "verify") not past tense ("tapped", "entered")
- [ ] If scenarios exist, they are clearly labeled (e.g., "Scenario A: Happy Path", "Scenario B: Error Case")
- [ ] Steps are testable — a QA engineer can follow them and determine pass/fail

**Rationale:** Clear steps enable UAT execution and form the basis for functional testing.

---

#### R6: Directory Structure
**Description:** The `docs/uat/` folder is flat (no subdirectories). Supporting files (screenshots, etc.) live in their own directories alongside `docs/uat/`.

**Acceptance Criteria:**
- [ ] `docs/uat/` contains only `.md` files and `.json` metadata (`.sync-map.json`, etc.)
- [ ] No subdirectories exist within `docs/uat/`
- [ ] Screenshots referenced in walkthroughs live in a parallel `docs/screenshots/` directory
- [ ] Relative paths in walkthrough image refs are `../screenshots/{filename}.png`

**Rationale:** Flat structure simplifies file discovery and glob patterns. Agents can reliably find all UAT files with a simple `docs/uat/*.md` glob.

---

#### R7: Metadata Mapping (.sync-map.json)
**Description:** UAT IDs are mapped to ClickUp task IDs in `docs/uat/.sync-map.json`. This file is the single source of truth for UAT <-> ClickUp linkage.

**Acceptance Criteria:**
- [ ] `.sync-map.json` exists in `docs/uat/` and is valid JSON
- [ ] Structure is `{ "{id}": "ClickUp_task_id", ... }`
- [ ] Every UAT file ID in the folder appears in `.sync-map.json`
- [ ] ClickUp IDs are strings (preserve leading zeros and special chars)

**Rationale:** ClickUp links are stored separately from UAT files (not in metadata blocks) to avoid duplication with the manifest and keep UAT files clean.

---

### P1: Nice-to-Have (Improves Experience, Not Blocking)

#### R8: Notes Section Completeness
**Description:** For complex features, the `## Notes` section documents platform differences, feature flags, blockers, and edge cases.

**Acceptance Criteria:**
- [ ] If a feature has platform-specific behavior (iOS vs. macOS), it is documented in Notes
- [ ] If a feature is behind a feature flag, the flag name is mentioned
- [ ] If there are known blockers or TODOs, they are listed with context
- [ ] Notes are brief and bullet-pointed (not prose)

**Rationale:** Notes provide context for guide readers and QA testers. Incomplete notes are better than missing ones; this is non-blocking.

---

#### R9: Visual Consistency
**Description:** Screenshots in walkthroughs are consistent in style, size, and labeling.

**Acceptance Criteria:**
- [ ] Screenshots are PNGs or JPGs, not SVGs or other formats
- [ ] Screenshot filenames are descriptive and match the UAT ID (e.g., `304-generating.png`, `304-results.png`)
- [ ] Captions for images are present and descriptive

**Rationale:** Consistency improves guide appearance. Low priority because guide composition does not fail on missing screenshots.

---

### P2: Future Considerations (Not in v1, But Design for Them)

#### R10: Multi-Language Support
**Description:** UAT files may eventually need translations for international guides. The structure should support translation without requiring file duplication.

**Design consideration:** Walkthroughs are separated from steps; this enables translating walkthrough text independently if needed later.

**Rationale:** Current implementation is English-only. No work needed now, but the modular structure supports localization later.

---

#### R11: UAT Metadata Queries
**Description:** As the folder grows, we may want to query UAT files by feature area, platform, or guide membership.

**Design consideration:** IDs use a hierarchical numbering scheme (100s = onboarding, 200s = core feature area 1, 300s = core feature area 2, etc.). This is maintained but not enforced in code.

**Rationale:** Manual structure is sufficient for now. If automated querying becomes necessary, the ID scheme provides a foundation.

---

## ID Numbering Scheme

| Range | Feature Area |
|-------|-------------|
| 100s | Onboarding & First Launch |
| 200s | Core Feature Area 1 |
| 300s | Core Feature Area 2 |
| 400s | Core Feature Area 3 |
| 500s | Editing & Amendments |
| 600s | Billing & Integrations |
| 700s | References & Resources |
| 800s | Content Library |
| 900s | Media & Reports |
| 1000s | Analytics |
| 1100s | Data Management |
| 1200s | Settings |
| 1300s | Platform & Navigation |
| 1400s | Edge Cases |

New files use the next available ID in their feature area range.

---

## Success Metrics

### Leading Indicators (Measure During/Right After Launch)

1. **Zero Manifest Validation Errors** — The audit script finds zero files without manifest entries and zero manifest entries without corresponding files.
   - **Target:** 100% coverage immediately after implementation
   - **Measurement:** Run `audit-uat-folder.py --coverage` after implementation; expect zero violations

2. **Format Compliance Rate** — All 55+ existing UAT files conform to R2 (gold-standard format).
   - **Target:** 100% compliance within 1 week
   - **Measurement:** Run `audit-uat-folder.py --format-check`; expect zero violations

3. **Agent Success Rate** — When an agent creates a new UAT file following the spec, the file requires zero manual corrections.
   - **Target:** 100% first-pass acceptance
   - **Measurement:** Track agent-created files; count rework requests

4. **Guide Composition Reliability** — `compose-guide.py` runs without errors when operating on the standardized folder.
   - **Target:** 100% success rate
   - **Measurement:** Run full guide composition weekly; expect zero failures

### Lagging Indicators (Measure Over Time)

5. **Onboarding Time for New Features** — Time from "we need a new feature tested" to "UAT file is created and in manifest" decreases.
   - **Target:** <30 minutes for agents to create a new UAT file (down from 1-2 hours of uncertainty)
   - **Measurement:** Track timestamps of feature request vs. UAT file creation in git history

6. **Maintenance Burden** — Number of "UAT organization" or "manifest cleanup" manual tasks per quarter decreases to near zero.
   - **Target:** <1 manual fix per quarter
   - **Measurement:** Count maintenance commits tagged `[uat-org]`
