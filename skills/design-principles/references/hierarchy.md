# Visual Hierarchy Principles

Hierarchy guides the eye. Without it, every element competes equally and users don't know where to look.

## The Hierarchy Toolkit

Five tools create visual hierarchy:

```
1. SIZE        → Larger = more important
2. CONTRAST    → Higher contrast = more attention
3. SPACING     → More space = more prominence
4. POSITION    → Top/left = seen first (in LTR)
5. DEPTH       → Elevated = more focus
```

## Size Hierarchy

### The Obvious Tool

Size is the most immediate hierarchy signal:

```
┌─────────────────────────────────────┐
│  HUGE HEADLINE                      │  ← First thing you see
│                                     │
│  Smaller subheading that supports   │  ← Second thing
│                                     │
│  Body text that provides detail     │  ← Third, if interested
│  and context for those who want     │
│  to read more about this topic.     │
│                                     │
│  [Button]                           │  ← Action after context
└─────────────────────────────────────┘
```

### Size Ratios

Use consistent ratios between levels:

| Ratio | Feel | Use Case |
|-------|------|----------|
| 1.2 (Minor Third) | Subtle | Dense UIs, apps |
| 1.25 (Major Third) | Balanced | Most interfaces |
| 1.333 (Perfect Fourth) | Clear | Marketing, content |
| 1.5 (Perfect Fifth) | Bold | Editorial, impact |
| 1.618 (Golden Ratio) | Dramatic | Hero moments |

## Contrast Hierarchy

### Light Mode

```
High contrast   → Primary content, headlines
Medium contrast → Body text, secondary info
Low contrast    → Metadata, hints, disabled
```

### Dark Mode

```
Full white      → Headlines, CTAs (sparingly)
Off-white (87%) → Primary content
Gray (60%)      → Secondary content
Dark gray (38%) → Hints, disabled
```

### Color as Contrast

Beyond light/dark:
- **Saturated color** draws attention
- **Muted color** recedes
- **Brand color** signals importance/interactivity

## Spacing Hierarchy

### Whitespace Communicates

```
More space around element = More important

┌──────────────────────────────────────────┐
│                                          │
│                                          │
│         Important Headline               │  ← Lots of breathing room
│                                          │
│                                          │
│    Less important supporting text        │  ← Less space
│    that provides additional context      │
│                                          │
└──────────────────────────────────────────┘
```

### Spacing Scale

Build a consistent scale:

```
--space-1: 4px    → Tight groupings
--space-2: 8px    → Related elements
--space-3: 12px   → Comfortable gaps
--space-4: 16px   → Section breathing room
--space-5: 24px   → Clear separation
--space-6: 32px   → Major sections
--space-7: 48px   → Page-level divisions
--space-8: 64px   → Hero spacing
```

### Proximity Principle

**Related things = close together**
**Unrelated things = far apart**

```
✅ Good grouping:
┌─────────────────┐
│ Label           │  ← Label close to input
│ [Input field  ] │
└─────────────────┘

❌ Bad grouping:
┌─────────────────┐
│ Label           │
│                 │  ← Too much space breaks relationship
│                 │
│ [Input field  ] │
└─────────────────┘
```

## Position Hierarchy

### Reading Patterns

**F-Pattern** (content-heavy pages):
```
████████████████████
████████████
████████████████
███████
```
Users scan top, then left edge.

**Z-Pattern** (minimal pages):
```
█───────────────█
       ╲
        ╲
█───────────────█
```
Users scan top-left → top-right → bottom-left → bottom-right.

### Position Implications

| Position | Implication |
|----------|-------------|
| Top-left | Logo, primary navigation |
| Top-right | Actions, account |
| Center | Hero content, primary focus |
| Bottom | CTAs, secondary actions |

## Depth Hierarchy

### Elevation Creates Focus

```
Layer 0: Base (background)
Layer 1: Cards, containers
Layer 2: Popovers, dropdowns
Layer 3: Modals, dialogs
Layer 4: Tooltips, notifications
```

### Creating Depth

**Light mode** (shadows):
```css
--shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
--shadow-md: 0 4px 6px rgba(0,0,0,0.1);
--shadow-lg: 0 10px 15px rgba(0,0,0,0.1);
--shadow-xl: 0 20px 25px rgba(0,0,0,0.15);
```

**Dark mode** (surface lightness):
```css
--surface-0: #121212;
--surface-1: #1E1E1E;
--surface-2: #232323;
--surface-3: #282828;
```

## The Squint Test

**How to use it**:
1. Step back from your design (or squint)
2. The most important element should still be obvious
3. Hierarchy should be readable even blurred

**If everything looks the same** → hierarchy is broken.

## Hierarchy in Action

### Hero Section

```
┌─────────────────────────────────────────┐
│                                         │
│     Big Bold Headline                   │  ← 1. Size: largest
│     That Grabs Attention                │     Contrast: highest
│                                         │     Space: most
│     Supporting text that provides       │  ← 2. Size: medium
│     context but doesn't compete         │     Contrast: medium
│                                         │
│     [Primary CTA]  [Secondary]          │  ← 3. Color/contrast
│                                         │     (Primary > Secondary)
└─────────────────────────────────────────┘
```

### Card Component

```
┌─────────────────────────────────────────┐
│  ┌─────────────────────────────────┐    │
│  │         [Image]                 │    │  ← 1. Visual anchor
│  └─────────────────────────────────┘    │
│                                         │
│  Card Title                             │  ← 2. What is this?
│  Supporting description that gives      │  ← 3. More detail
│  context without overwhelming.          │
│                                         │
│  metadata · more info                   │  ← 4. Least important
└─────────────────────────────────────────┘
```

## Anti-Patterns

### Don't

- ❌ Make everything the same size
- ❌ Use more than 3-4 hierarchy levels
- ❌ Rely only on color for hierarchy
- ❌ Crowd elements together
- ❌ Let secondary elements compete with primary

### Do

- ✅ Create clear visual levels
- ✅ Use multiple hierarchy tools together
- ✅ Test with the squint test
- ✅ Guide the eye intentionally
- ✅ Let whitespace do work
