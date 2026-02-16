# Color Principles

Color creates emotion, guides attention, and establishes identity. A systematic approach prevents random colors and creates cohesion.

## Building a Color System

### The Structure

```
┌─────────────────────────────────────────┐
│ Primary Color (Brand)                   │
│   └─ Light, Base, Dark variants         │
├─────────────────────────────────────────┤
│ Accent Color (Action)                   │
│   └─ For CTAs, highlights, emphasis     │
├─────────────────────────────────────────┤
│ Neutrals (Structure)                    │
│   └─ Backgrounds, borders, text         │
├─────────────────────────────────────────┤
│ Semantic Colors (Meaning)               │
│   └─ Success, warning, error, info      │
└─────────────────────────────────────────┘
```

### Primary Color

Your dominant color. It should:
- Reflect brand/product identity
- Work at multiple values (light to dark)
- Be distinct and recognizable

**Create variants**:
```
Primary Light  → Backgrounds, hover states
Primary Base   → Main brand usage
Primary Dark   → Text on light, emphasis
```

### Accent Color

Your action color. It should:
- Contrast sharply with primary
- Draw attention to CTAs
- Be used sparingly (scarcity = impact)

**Good accent relationships**:
- Complementary (opposite on wheel)
- Split-complementary (adjacent to complement)
- Triadic (three-way relationship)

### Neutral Palette

Your structural colors. Build a scale:

```
Neutral 50   → Lightest background
Neutral 100  → Subtle backgrounds
Neutral 200  → Borders, dividers
Neutral 300  → Disabled states
Neutral 400  → Placeholder text
Neutral 500  → Secondary text
Neutral 600  → Body text
Neutral 700  → Headings
Neutral 800  → Emphasis
Neutral 900  → Maximum contrast
```

## Color by Context

### Technical / Developer Tools

```
Primary:   Deep blue (#0066FF) or Teal (#00A693)
Accent:    Orange (#FF6B35) or Cyan (#00D4FF)
Neutrals:  Cool grays with blue undertone
Mode:      Often dark-first
```

**Why**: Blue conveys trust/stability, dark mode reduces eye strain for extended use.

### Creative / Consumer

```
Primary:   Vibrant, energetic (brand-specific)
Accent:    High-contrast complement
Neutrals:  Warm or cool based on brand
Mode:      Light-first, dark as option
```

**Why**: Energy and personality matter more than neutrality.

### Professional / Enterprise

```
Primary:   Refined blues, greens, or brand color
Accent:    Conservative, purposeful
Neutrals:  Balanced grays
Mode:      Light-first
```

**Why**: Trust and clarity over personality.

## Dark Mode

### Don't Just Invert

❌ White → Black (too harsh)
✅ White → Dark gray (#121212 to #1E1E1E)

❌ Black text → White text (too bright)
✅ Black text → Off-white (#E0E0E0 to #FFFFFF at 87%)

### Dark Mode Palette

```
Background:     #0A0A0A to #1A1A1A
Surface:        #1E1E1E to #2D2D2D (elevated)
Border:         rgba(255,255,255,0.1)
Primary text:   rgba(255,255,255,0.87)
Secondary text: rgba(255,255,255,0.60)
Disabled:       rgba(255,255,255,0.38)
```

### Elevation in Dark Mode

Light mode: shadows create elevation
Dark mode: lighter surfaces create elevation

```
Level 0: #121212
Level 1: #1E1E1E (cards)
Level 2: #232323 (dialogs)
Level 3: #282828 (menus)
Level 4: #2D2D2D (tooltips)
```

## Contrast & Accessibility

### WCAG Requirements

| Element | Minimum Ratio | Enhanced Ratio |
|---------|---------------|----------------|
| Normal text | 4.5:1 | 7:1 |
| Large text (18px+) | 3:1 | 4.5:1 |
| UI components | 3:1 | - |

### Testing Tools

- WebAIM Contrast Checker
- Stark (Figma plugin)
- Xcode Accessibility Inspector
- Chrome DevTools

### Safe Combinations

**On white/light**:
- Black text ✅
- Dark gray (#333) ✅
- Medium gray (#666) for secondary ✅
- Light gray (#999) ⚠️ borderline

**On dark backgrounds**:
- White text ✅
- Light gray (#E0E0E0) ✅
- Medium gray (#A0A0A0) for secondary ✅
- Dark gray (#666) ⚠️ borderline

## Color Emotion

| Color | Emotions | Common Uses |
|-------|----------|-------------|
| **Blue** | Trust, stability, calm | Tech, finance, healthcare |
| **Green** | Growth, nature, success | Eco, health, money |
| **Red** | Energy, urgency, passion | Sales, alerts, food |
| **Orange** | Creativity, warmth, action | CTAs, creative, youth |
| **Purple** | Luxury, creativity, wisdom | Premium, creative, spiritual |
| **Yellow** | Optimism, attention, caution | Highlights, warnings |
| **Pink** | Playful, feminine, modern | Beauty, youth, creative |
| **Black** | Sophistication, power | Luxury, fashion, tech |

## Anti-Patterns

### Don't

- ❌ Pick colors randomly
- ❌ Use too many colors (max 3-4 plus neutrals)
- ❌ Ignore contrast ratios
- ❌ Make dark mode an afterthought
- ❌ Use color as only indicator (accessibility)

### Do

- ✅ Build a systematic palette
- ✅ Test in context (not just swatches)
- ✅ Check contrast at every combination
- ✅ Design dark mode intentionally
- ✅ Use color + shape/text for meaning
