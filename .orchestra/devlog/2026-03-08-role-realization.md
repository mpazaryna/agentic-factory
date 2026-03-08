# The Developer Role Has Changed

**Date**: 2026-03-08

---

After a session that removed 37,000 lines of templating infrastructure and reshaped the factory repo's identity, a realization crystallized about what the developer role actually is now.

## The Role

The developer's job is:

- **Write PRDs** — define what should be built and why
- **Generate specs** — translate requirements into technical designs
- **Review specs** — validate that the design solves the right problem
- **Review PRDs** — gate-check that requirements are complete and coherent
- **Run UAT** — verify that what was built actually works end-to-end

The coding itself is commoditized. Agentic coding platforms handle implementation. The hard part — the part that requires judgment — is knowing what to build, recognizing when the solution is right, and catching when the agent took a shortcut.

## Evidence From This Session

No code was written by hand, but the following architectural decisions were made:

1. Recognized the 5,175-line templating system was obsolete because Claude natively understands component formats now
2. Identified the plugin distribution channel as the next frontier (something the agent missed)
3. Pushed back on surface-level analysis to find the real architectural question
4. Decided to split domain components into a private repo rather than filtering a public fork
5. Reframed the repo's identity from "meta-generator factory" to "component registry"

None of these decisions are automatable. They require context, taste, and judgment built from experience.

## The Toolchain Matches the Role

The components already in the factory map directly to this workflow:

- `ticket-refiner` — PRD generation from tickets
- `prd-to-spec` — spec generation from PRDs
- `quality-control-enforcer` — implementation review
- `convention-auditor` — compliance checking
- `uat-audit` — UAT validation

The tools for this role were being built before the role was fully articulated.
