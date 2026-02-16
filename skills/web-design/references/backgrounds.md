# Backgrounds & Depth

Layered backgrounds add visual interest and create atmospheric depth.

## Gradient Techniques

### Linear Gradients

```css
/* Subtle brand gradient */
.hero {
  background: linear-gradient(
    135deg,
    var(--color-primary-500) 0%,
    var(--color-primary-700) 100%
  );
}

/* Dark atmospheric */
.dark-hero {
  background: linear-gradient(
    180deg,
    #0A0A0A 0%,
    #1A1A2E 50%,
    #16213E 100%
  );
}

/* Soft light mode */
.light-section {
  background: linear-gradient(
    180deg,
    var(--color-gray-50) 0%,
    #FFFFFF 100%
  );
}

/* Diagonal accent */
.accent-bg {
  background: linear-gradient(
    -45deg,
    var(--color-primary-100) 0%,
    var(--color-primary-50) 50%,
    #FFFFFF 100%
  );
}
```

### Radial Gradients

```css
/* Centered glow */
.glow-bg {
  background: radial-gradient(
    circle at 50% 50%,
    var(--color-primary-500) 0%,
    transparent 70%
  );
}

/* Corner accent */
.corner-glow {
  background:
    radial-gradient(
      circle at 0% 0%,
      rgba(59, 130, 246, 0.15) 0%,
      transparent 50%
    ),
    radial-gradient(
      circle at 100% 100%,
      rgba(139, 92, 246, 0.15) 0%,
      transparent 50%
    ),
    var(--color-bg);
}

/* Spotlight effect */
.spotlight {
  background: radial-gradient(
    ellipse 80% 50% at 50% 0%,
    rgba(59, 130, 246, 0.2) 0%,
    transparent 100%
  );
}
```

### Conic Gradients

```css
/* Color wheel effect */
.conic-bg {
  background: conic-gradient(
    from 180deg,
    var(--color-primary-500),
    var(--color-primary-300),
    var(--color-primary-500)
  );
}
```

## Pattern Overlays

### Dot Grid

```css
.dot-pattern {
  background-image: radial-gradient(
    circle,
    rgba(0, 0, 0, 0.1) 1px,
    transparent 1px
  );
  background-size: 20px 20px;
}

/* Dark mode version */
.dot-pattern-dark {
  background-image: radial-gradient(
    circle,
    rgba(255, 255, 255, 0.1) 1px,
    transparent 1px
  );
  background-size: 20px 20px;
}
```

### Line Grid

```css
.grid-pattern {
  background-image:
    linear-gradient(
      rgba(0, 0, 0, 0.05) 1px,
      transparent 1px
    ),
    linear-gradient(
      90deg,
      rgba(0, 0, 0, 0.05) 1px,
      transparent 1px
    );
  background-size: 40px 40px;
}
```

### Diagonal Lines

```css
.diagonal-pattern {
  background-image: repeating-linear-gradient(
    45deg,
    transparent,
    transparent 10px,
    rgba(0, 0, 0, 0.03) 10px,
    rgba(0, 0, 0, 0.03) 20px
  );
}
```

### SVG Patterns (Inline)

```css
/* Fine grid texture */
.svg-grid {
  background-image: url("data:image/svg+xml,%3Csvg width='20' height='20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M0 0h20v20H0z' fill='none'/%3E%3Cpath d='M20 0v20M0 20h20' stroke='rgba(0,0,0,0.05)' stroke-width='1'/%3E%3C/svg%3E");
}

/* Dots pattern */
.svg-dots {
  background-image: url("data:image/svg+xml,%3Csvg width='20' height='20' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='2' cy='2' r='1' fill='rgba(0,0,0,0.1)'/%3E%3C/svg%3E");
}
```

## Noise Texture

```css
/* Subtle noise overlay */
.noise {
  position: relative;
}

.noise::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  opacity: 0.03;
  pointer-events: none;
}
```

## Layered Compositions

### Hero Section

```css
.hero {
  position: relative;
  min-height: 80vh;

  /* Base gradient */
  background: linear-gradient(
    135deg,
    #0F172A 0%,
    #1E293B 100%
  );
}

/* Gradient orbs */
.hero::before {
  content: '';
  position: absolute;
  inset: 0;
  background:
    radial-gradient(
      circle at 20% 30%,
      rgba(59, 130, 246, 0.3) 0%,
      transparent 40%
    ),
    radial-gradient(
      circle at 80% 70%,
      rgba(139, 92, 246, 0.3) 0%,
      transparent 40%
    );
  pointer-events: none;
}

/* Grid overlay */
.hero::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: linear-gradient(
    rgba(255, 255, 255, 0.03) 1px,
    transparent 1px
  ),
  linear-gradient(
    90deg,
    rgba(255, 255, 255, 0.03) 1px,
    transparent 1px
  );
  background-size: 50px 50px;
  pointer-events: none;
}
```

### Feature Section

```css
.features {
  position: relative;
  background: var(--color-bg);
}

/* Subtle top gradient */
.features::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 200px;
  background: linear-gradient(
    180deg,
    var(--color-primary-50) 0%,
    transparent 100%
  );
  pointer-events: none;
}
```

## Glass Effect (Glassmorphism)

```css
.glass {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: var(--radius-lg);
}

/* Dark mode glass */
.glass-dark {
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}
```

## Mesh Gradients

```css
/* Complex mesh effect */
.mesh-bg {
  background-color: #f0f4f8;
  background-image:
    radial-gradient(at 40% 20%, #e0e7ff 0px, transparent 50%),
    radial-gradient(at 80% 0%, #ddd6fe 0px, transparent 50%),
    radial-gradient(at 0% 50%, #c7d2fe 0px, transparent 50%),
    radial-gradient(at 80% 50%, #fecdd3 0px, transparent 50%),
    radial-gradient(at 0% 100%, #dbeafe 0px, transparent 50%),
    radial-gradient(at 80% 100%, #e9d5ff 0px, transparent 50%);
}
```

## Animation

### Animated Gradient

```css
@keyframes gradient-shift {
  0%, 100% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
}

.animated-gradient {
  background: linear-gradient(
    -45deg,
    #ee7752,
    #e73c7e,
    #23a6d5,
    #23d5ab
  );
  background-size: 400% 400%;
  animation: gradient-shift 15s ease infinite;
}
```

### Subtle Floating Orbs

```css
@keyframes float {
  0%, 100% {
    transform: translateY(0) scale(1);
  }
  50% {
    transform: translateY(-20px) scale(1.05);
  }
}

.floating-orb {
  position: absolute;
  width: 300px;
  height: 300px;
  border-radius: 50%;
  background: radial-gradient(
    circle,
    rgba(59, 130, 246, 0.3) 0%,
    transparent 70%
  );
  animation: float 6s ease-in-out infinite;
  pointer-events: none;
}
```

## Best Practices

1. **Layer from back to front** - Base → Gradient → Pattern → Content
2. **Use pseudo-elements** - Keep backgrounds separate from content
3. **Respect reduced motion** - Disable animated backgrounds when requested
4. **Performance** - Prefer CSS over images when possible
5. **Contrast** - Ensure text remains readable over backgrounds
