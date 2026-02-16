---
name: web-design
description: Web/CSS implementation patterns for building polished frontends. Use when implementing designs in HTML/CSS, building components, or creating responsive web interfaces.
---

# web-design

CSS implementation patterns for building distinctive web interfaces.

## Scope

This skill covers **web implementation**—the CSS, HTML, and patterns needed to build polished frontends. For design theory (typography choices, color systems, hierarchy principles), see `design-principles`.

## Routing

Based on what you're building, I'll reference the appropriate implementation guide:

### CSS System Setup
**When**: Starting a project, establishing CSS architecture
**Reference**: `references/css-system.md`
- CSS custom properties (variables)
- Token systems (spacing, sizing, colors)
- Theme structure and dark mode
- Reset and baseline styles

### Component Patterns
**When**: Building UI components, semantic markup
**Reference**: `references/components.md`
- Semantic HTML structure
- BEM-style naming conventions
- Common component patterns (cards, buttons, forms)
- Accessibility patterns

### Backgrounds & Depth
**When**: Adding visual interest, creating depth
**Reference**: `references/backgrounds.md`
- Gradient techniques
- Pattern overlays
- Texture and noise
- Layered compositions

### Responsive Design
**When**: Mobile-first, breakpoints, fluid layouts
**Reference**: `references/responsive.md`
- Breakpoint systems
- Fluid typography and spacing
- Container queries
- Layout patterns (grid, flexbox)

## Quick Reference

### Essential CSS Variables

```css
:root {
  /* Colors - from design-principles */
  --color-primary: #0066FF;
  --color-accent: #FF6B35;
  --color-bg: #FAFAFA;
  --color-surface: #FFFFFF;
  --color-text: #1A1A1A;
  --color-text-secondary: #666666;

  /* Spacing scale */
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.5rem;   /* 8px */
  --space-3: 0.75rem;  /* 12px */
  --space-4: 1rem;     /* 16px */
  --space-6: 1.5rem;   /* 24px */
  --space-8: 2rem;     /* 32px */
  --space-12: 3rem;    /* 48px */

  /* Typography */
  --font-sans: 'IBM Plex Sans', system-ui, sans-serif;
  --font-mono: 'IBM Plex Mono', monospace;

  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);

  /* Transitions */
  --transition-fast: 150ms ease-out;
  --transition-base: 200ms ease-out;
  --transition-slow: 300ms ease-out;
}
```

### Dark Mode Pattern

```css
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #0A0A0A;
    --color-surface: #1A1A1A;
    --color-text: #FAFAFA;
    --color-text-secondary: #A0A0A0;
  }
}
```

### Responsive Breakpoints

```css
/* Mobile first */
.component { /* mobile styles */ }

@media (min-width: 640px) { /* sm */ }
@media (min-width: 768px) { /* md */ }
@media (min-width: 1024px) { /* lg */ }
@media (min-width: 1280px) { /* xl */ }
```

## Anti-Patterns

- Inline styles instead of CSS variables
- Magic numbers instead of spacing scale
- Pixel units for typography (use rem)
- No dark mode consideration
- Div soup instead of semantic HTML
- Ignoring focus states

## Related Skills

- **design-principles** - Theory behind the choices
- **swift-ui** - iOS/SwiftUI implementation
- **design-review** - Audit and polish
