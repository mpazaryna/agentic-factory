# Accessibility Principles

Accessibility isn't a feature—it's a quality standard. Accessible design is better design for everyone.

## The Foundation

### Why It Matters

- **15%+ of people** have some form of disability
- **Temporary disabilities** affect everyone (broken arm, bright sunlight)
- **Situational limitations** are universal (one-handed, noisy environment)
- **Legal requirements** exist in many jurisdictions
- **Better UX for all** (captions help in noisy rooms, high contrast helps in sunlight)

### The Four Principles (POUR)

| Principle | Meaning | Example |
|-----------|---------|---------|
| **Perceivable** | Users can perceive the content | Alt text, captions, contrast |
| **Operable** | Users can operate the interface | Keyboard nav, touch targets |
| **Understandable** | Users can understand content/UI | Clear labels, consistent patterns |
| **Robust** | Content works with assistive tech | Semantic HTML, ARIA |

## Visual Accessibility

### Contrast

**WCAG Requirements**:

| Element | AA (minimum) | AAA (enhanced) |
|---------|--------------|----------------|
| Normal text | 4.5:1 | 7:1 |
| Large text (18px+) | 3:1 | 4.5:1 |
| UI components | 3:1 | - |
| Non-text (icons) | 3:1 | - |

**Testing**: Use WebAIM Contrast Checker or built-in dev tools.

### Color Independence

Never use color alone to convey meaning:

```
❌ Bad:  Red = error (color only)
✅ Good: Red + icon + text = error

❌ Bad:  Green dot = online (color only)
✅ Good: Green dot + "Online" label
```

### Text Sizing

- **Minimum**: 16px for body text
- **Allow scaling**: Don't break layout at 200% zoom
- **Use relative units**: rem, em (not px for text)

```css
/* Good: Scales with user preferences */
font-size: 1rem;

/* Avoid: Fixed size */
font-size: 16px;
```

## Motor Accessibility

### Touch Targets

**Minimum sizes**:
- iOS: 44×44 points
- Android: 48×48 dp
- Web: 44×44 CSS pixels

**Spacing**: At least 8px between targets

```css
.button {
  min-height: 44px;
  min-width: 44px;
  padding: 12px 24px;
}
```

### Keyboard Navigation

All interactive elements must be:
1. **Focusable** (can reach via Tab)
2. **Activatable** (can trigger via Enter/Space)
3. **Visibly focused** (clear focus indicator)

```css
/* Never do this */
:focus { outline: none; }

/* Do this instead */
:focus {
  outline: 2px solid var(--color-primary);
  outline-offset: 2px;
}

/* Or custom focus styles */
:focus-visible {
  box-shadow: 0 0 0 3px var(--color-focus);
}
```

### Focus Order

Focus should flow logically:
1. Top to bottom
2. Left to right (in LTR languages)
3. Match visual order

```html
<!-- Good: Visual order matches DOM order -->
<nav>...</nav>
<main>...</main>
<aside>...</aside>

<!-- Bad: CSS reorders visually but not in DOM -->
```

## Screen Reader Accessibility

### Semantic HTML

Use the right elements:

```html
<!-- Good: Semantic -->
<button>Submit</button>
<nav>...</nav>
<main>...</main>
<article>...</article>

<!-- Bad: Divs for everything -->
<div onclick="submit()">Submit</div>
<div class="nav">...</div>
```

### ARIA When Needed

ARIA supplements HTML, doesn't replace it:

```html
<!-- Good: Native element -->
<button>Close</button>

<!-- If you must use a div -->
<div role="button" tabindex="0" aria-label="Close">×</div>
```

**Common ARIA attributes**:

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `aria-label` | Accessible name | Icon buttons |
| `aria-labelledby` | Reference to label | Complex components |
| `aria-describedby` | Additional description | Form help text |
| `aria-hidden` | Hide from screen readers | Decorative elements |
| `aria-live` | Announce updates | Notifications |
| `aria-expanded` | Toggle state | Accordions |

### Images

```html
<!-- Informative image -->
<img src="chart.png" alt="Sales increased 25% in Q4">

<!-- Decorative image -->
<img src="decoration.png" alt="" role="presentation">

<!-- Complex image -->
<figure>
  <img src="diagram.png" alt="System architecture overview">
  <figcaption>Detailed description...</figcaption>
</figure>
```

## Motion Accessibility

### Respect Preferences

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

### SwiftUI

```swift
@Environment(\.accessibilityReduceMotion) var reduceMotion

withAnimation(reduceMotion ? nil : .easeOut) {
    // ...
}
```

## Forms Accessibility

### Labels

Every input needs a label:

```html
<!-- Good: Explicit label -->
<label for="email">Email address</label>
<input type="email" id="email" name="email">

<!-- Good: Implicit label -->
<label>
  Email address
  <input type="email" name="email">
</label>

<!-- Bad: No label -->
<input type="email" placeholder="Email">
```

### Error Messages

```html
<label for="email">Email</label>
<input
  type="email"
  id="email"
  aria-describedby="email-error"
  aria-invalid="true"
>
<span id="email-error" role="alert">
  Please enter a valid email address
</span>
```

### Required Fields

```html
<label for="name">
  Name <span aria-hidden="true">*</span>
  <span class="sr-only">(required)</span>
</label>
<input type="text" id="name" required aria-required="true">
```

## Testing Checklist

### Automated

- [ ] Run axe DevTools or similar
- [ ] Check Lighthouse accessibility score
- [ ] Validate HTML

### Manual

- [ ] Navigate entire UI with keyboard only
- [ ] Test with screen reader (VoiceOver, NVDA)
- [ ] Check at 200% zoom
- [ ] Test with high contrast mode
- [ ] Verify focus is always visible

### User Testing

- [ ] Test with actual users who use assistive tech
- [ ] Include in regular usability testing

## Platform-Specific

### Web

- Use semantic HTML
- ARIA as supplement
- Test with multiple screen readers

### iOS/SwiftUI

- Use standard controls (get accessibility free)
- Add `.accessibilityLabel()` for custom views
- Test with VoiceOver
- Support Dynamic Type

```swift
Text("Hello")
    .accessibilityLabel("Greeting message")
    .accessibilityHint("Displays welcome text")
```

### Android

- Use standard Material components
- Add `contentDescription` for images
- Test with TalkBack

## Anti-Patterns

### Don't

- ❌ Remove focus outlines without replacement
- ❌ Use color alone for meaning
- ❌ Create keyboard traps
- ❌ Auto-play media
- ❌ Use tiny touch targets

### Do

- ✅ Design with accessibility from the start
- ✅ Use semantic elements
- ✅ Provide visible focus states
- ✅ Test with real assistive technology
- ✅ Include accessibility in definition of done
