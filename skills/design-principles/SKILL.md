---
name: design-principles
description: Universal design principles for any UI platform. Use when establishing design direction, choosing typography, building color systems, or understanding visual hierarchy. Platform-agnostic theory that applies to web, SwiftUI, and beyond.
---

# Design Principles

Universal design theory. Platform-agnostic foundations that make interfaces feel **designed**, not generated.

> Good design is platform-agnostic. The principles work whether you're building for web, iOS, or any other medium.

## When to Use This Skill

**Establishing design direction**:
- "What's the right aesthetic for a developer tool?"
- "How should I approach design for this app?"

**Typography decisions**:
- "What fonts work for a technical product?"
- "How do I create type hierarchy?"

**Color systems**:
- "Build a color palette for this brand"
- "How do I choose accent colors?"

**Visual hierarchy**:
- "How do I guide the user's eye?"
- "What creates visual weight?"

**Motion principles**:
- "When should I animate?"
- "What makes motion feel natural?"

## Principle Areas

This skill covers five universal areas:

| Area | What It Covers | Reference |
|------|----------------|-----------|
| **Typography** | Font selection, hierarchy, scale | `references/typography.md` |
| **Color** | Palettes, contrast, emotion | `references/color.md` |
| **Hierarchy** | Visual weight, spacing, flow | `references/hierarchy.md` |
| **Motion** | Animation principles, timing | `references/motion.md` |
| **Accessibility** | Universal design, inclusive patterns | `references/accessibility.md` |

## How to Use This Skill

1. **Identify the principle area** from the request
2. **Load the appropriate reference**
3. **Apply principles** to the specific context
4. **Hand off to platform skill** for implementation (web-design, swift-ui)

## Quick Principles

### Typography

**Avoid generic**:
- ❌ Inter, Roboto, Arial, system defaults as primary

**Choose with intent**:
- Technical → IBM Plex, JetBrains Mono
- Editorial → Playfair Display, Crimson Pro
- Modern → Space Grotesk, Cabinet Grotesk
- Elegant → Cormorant, Libre Baskerville

### Color

**Build systems, not random colors**:
- 1 dominant color (with light/dark variants)
- 1 sharp accent (for CTAs, highlights)
- 3-4 neutral shades (backgrounds, text hierarchy)

**Consider context**:
- Technical tools → Deep blues, teals, dark modes
- Creative products → Vibrant, energetic palettes
- Professional services → Refined, trustworthy tones

### Hierarchy

**Guide the eye**:
- Size creates importance
- Contrast creates focus
- Spacing creates relationships
- Alignment creates order

**The squint test**: If you squint, the most important element should still be obvious.

### Motion

**Purposeful, not decorative**:
- Entrance → Orient the user
- Feedback → Confirm interactions
- Transitions → Maintain context

**Timing**:
- Fast (100-200ms) → Immediate feedback
- Medium (200-400ms) → Transitions
- Slow (400-600ms) → Emphasis moments

### Accessibility

**Universal by default**:
- Contrast ratios (4.5:1 minimum for text)
- Touch targets (44pt minimum)
- Focus states (visible and clear)
- Motion preferences (respect reduced-motion)

## Design Direction Framework

Before designing, establish:

```markdown
## Design Direction

**Context**: What is this? (app, website, tool)
**Audience**: Who uses it? (developers, consumers, enterprise)
**Mood**: What should it feel like? (professional, playful, technical)
**Constraints**: What limitations exist? (brand, platform, accessibility)
```

This informs all subsequent choices.

## Anti-Patterns

1. **Generic font stack** → Choose fonts with intent
2. **Random colors** → Build systematic palettes
3. **Flat everything** → Create depth and hierarchy
4. **Animation everywhere** → Motion with purpose
5. **Ignoring context** → Design for the specific use case

## Part of the design-* Family

| Skill | Purpose |
|-------|---------|
| `design-principles` | Universal theory (this skill) |
| `web-design` | Web implementation (CSS, HTML) |
| `swift-ui` | SwiftUI implementation (HIG, Swift) |
| `design-review` | Audits and reviews (App Store, accessibility) |

## Workflow

```
design-principles: "What's the right approach?"
        ↓
web-design OR swift-ui: "Build it for this platform"
        ↓
design-review: "Is it ready for production?"
```
