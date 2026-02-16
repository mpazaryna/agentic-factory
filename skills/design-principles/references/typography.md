# Typography Principles

Typography is the foundation of visual design. The right type choices make interfaces feel intentional; the wrong ones make them feel generated.

## The Problem with Generic Fonts

**Why Inter/Roboto/Arial feel like "AI slop"**:
- They're defaults, not choices
- They signal "no one thought about this"
- They blend into forgettable sameness

**Distinctive typography says**: "Someone designed this."

## Font Selection by Context

### Technical / Developer Tools

| Font | Vibe | Use Case |
|------|------|----------|
| **IBM Plex Sans/Mono** | Technical, modern, geometric | APIs, dev tools, documentation |
| **JetBrains Mono** | Code-focused, precise | Code editors, terminals, technical UI |
| **Fira Code** | Readable code, ligatures | Code display, monospace needs |
| **Source Code Pro** | Clean, neutral monospace | Code blocks, data displays |

### Editorial / Content

| Font | Vibe | Use Case |
|------|------|----------|
| **Playfair Display** | Elegant, editorial | Headings, hero text, magazines |
| **Crimson Pro** | Refined, readable | Long-form content, articles |
| **Libre Baskerville** | Classic, trustworthy | Professional content, reports |
| **Cormorant** | Luxurious, distinctive | High-end, editorial |

### Modern / SaaS

| Font | Vibe | Use Case |
|------|------|----------|
| **Space Grotesk** | Contemporary, geometric | Modern apps, SaaS products |
| **Cabinet Grotesk** | Fresh, distinctive | Startups, innovative products |
| **Syne** | Bold, unconventional | Creative tools, bold brands |
| **Outfit** | Friendly, approachable | Consumer apps, friendly UI |

### System Fonts (When Appropriate)

| Platform | Font | When to Use |
|----------|------|-------------|
| iOS/macOS | SF Pro | Native feel, HIG compliance |
| Android | Roboto | Material Design alignment |
| Windows | Segoe UI | Windows native feel |

Use system fonts when **platform consistency** matters more than **brand distinction**.

## Type Hierarchy

### The Scale

```
Display    → 48-72px  → Hero headlines, major moments
Heading 1  → 32-40px  → Page titles
Heading 2  → 24-28px  → Section titles
Heading 3  → 20-22px  → Subsections
Body       → 16-18px  → Primary content
Small      → 14px     → Secondary content
Caption    → 12px     → Labels, metadata
```

### Hierarchy Through Weight

```
Bold (700)     → Headlines, emphasis
Semibold (600) → Subheadings, labels
Medium (500)   → UI elements, buttons
Regular (400)  → Body text
Light (300)    → Subtle, decorative (use sparingly)
```

### Hierarchy Through Contrast

```
Primary text   → Full opacity (100%)
Secondary text → Reduced opacity (70-80%)
Muted text     → Low opacity (50-60%)
Disabled       → Very low (30-40%)
```

## Type Pairing

### Safe Combinations

**Sans + Serif**:
- Space Grotesk (headings) + Crimson Pro (body)
- IBM Plex Sans (UI) + Playfair Display (display)

**Sans + Mono**:
- Inter (body) + JetBrains Mono (code)
- IBM Plex Sans (UI) + IBM Plex Mono (code)

**Same Family**:
- IBM Plex Sans + IBM Plex Serif + IBM Plex Mono
- Source Sans Pro + Source Serif Pro + Source Code Pro

### Pairing Rules

1. **Contrast in style** (sans + serif, or weight contrast)
2. **Harmony in structure** (similar x-height, similar feel)
3. **Maximum 2-3 fonts** per project
4. **One display, one body** as baseline

## Line Height & Spacing

### Line Height by Use

| Use Case | Line Height | Why |
|----------|-------------|-----|
| Headlines | 1.1-1.2 | Tight, impactful |
| UI text | 1.3-1.4 | Compact, scannable |
| Body text | 1.5-1.6 | Readable, comfortable |
| Long form | 1.6-1.8 | Extended reading |

### Letter Spacing

| Use Case | Letter Spacing |
|----------|----------------|
| Large headlines | -0.02em to -0.01em (tighter) |
| Normal text | 0 (default) |
| All caps | +0.05em to +0.1em (looser) |
| Small text | +0.01em (slightly looser) |

## Responsive Typography

### Fluid Sizing

```css
/* Example: Fluid type scale */
--text-base: clamp(1rem, 0.9rem + 0.5vw, 1.125rem);
--text-lg: clamp(1.125rem, 1rem + 0.6vw, 1.25rem);
--text-xl: clamp(1.25rem, 1rem + 1vw, 1.5rem);
--text-2xl: clamp(1.5rem, 1rem + 1.5vw, 2rem);
--text-display: clamp(2rem, 1rem + 3vw, 4rem);
```

### Breakpoint Adjustments

- **Mobile**: Reduce display sizes, maintain body size
- **Tablet**: Scale proportionally
- **Desktop**: Full scale, consider max-width for readability

## Anti-Patterns

### Don't

- ❌ Use more than 3 fonts
- ❌ Mix conflicting styles (playful + serious)
- ❌ Set body text below 14px
- ❌ Use light weights for small text
- ❌ Ignore line height

### Do

- ✅ Choose fonts with intent for context
- ✅ Build a clear hierarchy
- ✅ Test at actual sizes
- ✅ Consider accessibility (contrast, size)
- ✅ Be consistent across the product
