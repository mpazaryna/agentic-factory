# Motion Principles

Motion should feel purposeful, not decorative. Every animation should have a reason to exist.

## The Purpose of Motion

Motion serves specific functions:

| Purpose | What It Does | Example |
|---------|--------------|---------|
| **Orient** | Help users understand where they are | Page transitions |
| **Focus** | Direct attention to what matters | Highlighting new content |
| **Feedback** | Confirm actions were received | Button press states |
| **Continuity** | Maintain context during changes | Expanding cards |
| **Delight** | Add personality (sparingly) | Success celebrations |

If motion doesn't serve one of these, remove it.

## Timing & Easing

### Duration Guidelines

| Duration | Use Case |
|----------|----------|
| 100-150ms | Immediate feedback (hovers, toggles) |
| 200-300ms | Simple transitions (fades, color changes) |
| 300-400ms | Complex transitions (slides, expands) |
| 400-600ms | Emphasis moments (success, onboarding) |
| 600ms+ | Rare, intentional moments only |

**Rule**: If users notice the animation, it's probably too slow.

### Easing Functions

| Easing | Feel | Use Case |
|--------|------|----------|
| `ease-out` | Decelerating | Elements entering (most common) |
| `ease-in` | Accelerating | Elements exiting |
| `ease-in-out` | Smooth | Continuous motion |
| `linear` | Mechanical | Progress bars, loading |
| `cubic-bezier(0.4, 0, 0.2, 1)` | Material motion | General purpose |

**Default**: Use `ease-out` for entrances, `ease-in` for exits.

## Animation Patterns

### Entrance Animations

**Fade In Up** (most versatile):
```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-enter {
  animation: fadeInUp 300ms ease-out forwards;
}
```

**Scale In** (for emphasis):
```css
@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
```

### Staggered Reveals

Create visual rhythm for lists:

```css
.stagger-item {
  opacity: 0;
  animation: fadeInUp 300ms ease-out forwards;
}

.stagger-item:nth-child(1) { animation-delay: 0ms; }
.stagger-item:nth-child(2) { animation-delay: 50ms; }
.stagger-item:nth-child(3) { animation-delay: 100ms; }
.stagger-item:nth-child(4) { animation-delay: 150ms; }
/* ... */
```

**Timing**: 50-100ms between items. Don't exceed 500ms total.

### Hover States

**Subtle lift**:
```css
.card {
  transition: transform 200ms ease-out,
              box-shadow 200ms ease-out;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0,0,0,0.15);
}
```

**Color transition**:
```css
.button {
  transition: background-color 150ms ease-out;
}

.button:hover {
  background-color: var(--color-primary-dark);
}
```

### Loading States

**Skeleton pulse**:
```css
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.skeleton {
  background: #e0e0e0;
  animation: pulse 1.5s ease-in-out infinite;
}
```

**Spinner** (use sparingly):
```css
@keyframes spin {
  to { transform: rotate(360deg); }
}

.spinner {
  animation: spin 1s linear infinite;
}
```

## Platform Considerations

### Web

- CSS animations preferred (GPU-accelerated)
- JavaScript for complex orchestration
- Respect `prefers-reduced-motion`

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### SwiftUI

- Use `withAnimation` for state-driven motion
- `.animation()` modifier for continuous
- Match system motion feel

```swift
withAnimation(.easeOut(duration: 0.3)) {
    isExpanded.toggle()
}
```

### iOS Human Interface Guidelines

- Use system animations when possible
- Motion should feel physical (inertia, spring)
- Don't fight platform conventions

## Motion Hierarchy

Not all motion is equal:

```
Level 1: Page/Screen transitions (most prominent)
Level 2: Section reveals, major state changes
Level 3: Component animations (cards, lists)
Level 4: Micro-interactions (buttons, toggles)
```

**Higher levels = longer duration, more prominent**
**Lower levels = faster, subtler**

## Anti-Patterns

### Don't

- ❌ Animate everything
- ❌ Use bouncy/elastic effects for UI
- ❌ Make users wait for animations
- ❌ Loop animations indefinitely
- ❌ Ignore reduced-motion preferences

### Do

- ✅ Animate with purpose
- ✅ Use subtle, fast animations
- ✅ Prefer CSS over JavaScript
- ✅ Respect accessibility preferences
- ✅ Test on low-powered devices

## The Motion Test

Ask for each animation:

1. **What purpose does this serve?** (Orient, Focus, Feedback, Continuity, Delight)
2. **Would the UI work without it?** (If yes, consider removing)
3. **Does it feel too slow?** (When in doubt, speed up)
4. **Does it respect user preferences?** (reduced-motion)

If you can't answer #1, remove the animation.
