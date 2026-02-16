# Responsive Design

Mobile-first responsive patterns for flexible, maintainable layouts.

## Breakpoint System

### Standard Breakpoints

```css
/* Mobile first - no media query needed for mobile */

/* Small (landscape phones) */
@media (min-width: 640px) { /* sm */ }

/* Medium (tablets) */
@media (min-width: 768px) { /* md */ }

/* Large (desktops) */
@media (min-width: 1024px) { /* lg */ }

/* Extra large (large desktops) */
@media (min-width: 1280px) { /* xl */ }

/* 2XL (wide screens) */
@media (min-width: 1536px) { /* 2xl */ }
```

### CSS Custom Properties for Breakpoints

```css
:root {
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;
  --breakpoint-2xl: 1536px;
}
```

## Fluid Typography

### Clamp-Based Scale

```css
:root {
  /* Fluid type scale */
  --text-base: clamp(1rem, 0.95rem + 0.25vw, 1.125rem);
  --text-lg: clamp(1.125rem, 1rem + 0.5vw, 1.25rem);
  --text-xl: clamp(1.25rem, 1rem + 1vw, 1.5rem);
  --text-2xl: clamp(1.5rem, 1rem + 1.5vw, 2rem);
  --text-3xl: clamp(1.875rem, 1rem + 2vw, 2.5rem);
  --text-4xl: clamp(2.25rem, 1rem + 3vw, 3.5rem);
  --text-display: clamp(2.5rem, 1rem + 5vw, 5rem);
}

/* Usage */
.hero__title {
  font-size: var(--text-display);
}
```

### Formula Breakdown

```
clamp(MIN, PREFERRED, MAX)

MIN: Minimum font size (mobile)
PREFERRED: Fluid calculation (grows with viewport)
MAX: Maximum font size (desktop)

Example: clamp(1rem, 0.5rem + 2vw, 2rem)
- At 320px viewport: ~1rem
- At 1200px viewport: ~2rem
- Smoothly scales between
```

## Fluid Spacing

```css
:root {
  /* Fluid spacing scale */
  --space-fluid-sm: clamp(0.5rem, 0.4rem + 0.5vw, 0.75rem);
  --space-fluid-md: clamp(1rem, 0.8rem + 1vw, 1.5rem);
  --space-fluid-lg: clamp(1.5rem, 1rem + 2vw, 3rem);
  --space-fluid-xl: clamp(2rem, 1rem + 4vw, 5rem);
  --space-fluid-2xl: clamp(3rem, 1rem + 6vw, 8rem);
}

/* Section padding */
.section {
  padding-block: var(--space-fluid-xl);
  padding-inline: var(--space-fluid-md);
}
```

## Container Patterns

### Max-Width Container

```css
.container {
  width: 100%;
  max-width: 1200px;
  margin-inline: auto;
  padding-inline: var(--space-4);
}

@media (min-width: 768px) {
  .container {
    padding-inline: var(--space-6);
  }
}

@media (min-width: 1024px) {
  .container {
    padding-inline: var(--space-8);
  }
}
```

### Fluid Container

```css
.container-fluid {
  width: min(100% - var(--space-8), 1400px);
  margin-inline: auto;
}
```

### Content Width Variants

```css
.container--narrow {
  max-width: 680px;  /* Reading width */
}

.container--wide {
  max-width: 1400px;
}

.container--full {
  max-width: none;
  padding-inline: var(--space-4);
}
```

## Layout Patterns

### Grid System

```css
/* Auto-fit responsive grid */
.grid {
  display: grid;
  gap: var(--space-6);
  grid-template-columns: repeat(
    auto-fit,
    minmax(min(300px, 100%), 1fr)
  );
}

/* Fixed column grid */
.grid-cols-2 {
  display: grid;
  gap: var(--space-6);
  grid-template-columns: 1fr;
}

@media (min-width: 768px) {
  .grid-cols-2 {
    grid-template-columns: repeat(2, 1fr);
  }
}

.grid-cols-3 {
  display: grid;
  gap: var(--space-6);
  grid-template-columns: 1fr;
}

@media (min-width: 640px) {
  .grid-cols-3 {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (min-width: 1024px) {
  .grid-cols-3 {
    grid-template-columns: repeat(3, 1fr);
  }
}
```

### Sidebar Layout

```css
.sidebar-layout {
  display: grid;
  gap: var(--space-6);
}

@media (min-width: 1024px) {
  .sidebar-layout {
    grid-template-columns: 280px 1fr;
  }
}

/* Sidebar on right */
.sidebar-layout--right {
  grid-template-columns: 1fr;
}

@media (min-width: 1024px) {
  .sidebar-layout--right {
    grid-template-columns: 1fr 280px;
  }
}
```

### Stack Pattern

```css
.stack {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.stack--lg {
  gap: var(--space-6);
}

/* Horizontal on larger screens */
.stack-to-row {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

@media (min-width: 768px) {
  .stack-to-row {
    flex-direction: row;
    align-items: center;
  }
}
```

## Container Queries

```css
/* Define container */
.card-container {
  container-type: inline-size;
  container-name: card;
}

/* Query the container */
@container card (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
  }
}

@container card (min-width: 600px) {
  .card__title {
    font-size: var(--text-xl);
  }
}
```

## Responsive Navigation

```css
.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-4);
}

.nav__menu {
  display: none;
}

.nav__toggle {
  display: flex;
}

@media (min-width: 768px) {
  .nav__menu {
    display: flex;
    gap: var(--space-4);
  }

  .nav__toggle {
    display: none;
  }
}
```

## Responsive Images

```css
/* Responsive by default */
img {
  max-width: 100%;
  height: auto;
}

/* Art direction with picture */
.hero-image {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

@media (min-width: 768px) {
  .hero-image {
    aspect-ratio: 21 / 9;
  }
}
```

```html
<!-- Responsive image with srcset -->
<img
  src="image-800.jpg"
  srcset="
    image-400.jpg 400w,
    image-800.jpg 800w,
    image-1200.jpg 1200w
  "
  sizes="(max-width: 600px) 100vw, 50vw"
  alt="Description"
>

<!-- Art direction with picture -->
<picture>
  <source media="(min-width: 1024px)" srcset="hero-wide.jpg">
  <source media="(min-width: 640px)" srcset="hero-medium.jpg">
  <img src="hero-mobile.jpg" alt="Hero image">
</picture>
```

## Responsive Tables

```css
/* Horizontal scroll on mobile */
.table-container {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

/* Or stack on mobile */
@media (max-width: 639px) {
  .table-stack thead {
    display: none;
  }

  .table-stack tr {
    display: block;
    margin-bottom: var(--space-4);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
  }

  .table-stack td {
    display: flex;
    justify-content: space-between;
    padding: var(--space-3);
    border-bottom: 1px solid var(--color-border);
  }

  .table-stack td::before {
    content: attr(data-label);
    font-weight: 600;
  }
}
```

## Responsive Utilities

```css
/* Show/hide based on breakpoint */
.hide-mobile {
  display: none;
}

@media (min-width: 768px) {
  .hide-mobile {
    display: block;
  }

  .hide-desktop {
    display: none;
  }
}

/* Responsive text alignment */
.text-center-mobile {
  text-align: center;
}

@media (min-width: 768px) {
  .text-center-mobile {
    text-align: left;
  }
}
```

## Testing Checklist

- [ ] Test at 320px (small phones)
- [ ] Test at 375px (standard phones)
- [ ] Test at 768px (tablets)
- [ ] Test at 1024px (small laptops)
- [ ] Test at 1440px (desktops)
- [ ] Test with zoom (200%)
- [ ] Test with reduced motion enabled
- [ ] Test touch targets (44px minimum)
