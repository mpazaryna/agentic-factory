# Component Patterns

Reusable component patterns with semantic HTML and consistent styling.

## Naming Convention (BEM-ish)

```css
/* Block */
.card { }

/* Element */
.card__header { }
.card__body { }
.card__footer { }

/* Modifier */
.card--featured { }
.card--compact { }

/* State */
.card.is-selected { }
.card.is-loading { }
```

## Button Component

```html
<button class="btn btn--primary">
  Primary Action
</button>

<button class="btn btn--secondary">
  Secondary Action
</button>

<button class="btn btn--ghost">
  Ghost Button
</button>
```

```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);

  padding: var(--space-2) var(--space-4);
  min-height: 44px;  /* Touch target */

  font-family: var(--font-sans);
  font-size: var(--text-sm);
  font-weight: 500;
  line-height: 1;

  border: 1px solid transparent;
  border-radius: var(--radius-md);

  cursor: pointer;
  transition: all var(--duration-fast) var(--ease-out);
}

.btn:focus-visible {
  outline: 2px solid var(--color-primary-500);
  outline-offset: 2px;
}

.btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Variants */
.btn--primary {
  background-color: var(--color-primary-500);
  color: white;
}

.btn--primary:hover:not(:disabled) {
  background-color: var(--color-primary-600);
}

.btn--secondary {
  background-color: var(--color-surface);
  border-color: var(--color-border);
  color: var(--color-text);
}

.btn--secondary:hover:not(:disabled) {
  background-color: var(--color-gray-100);
}

.btn--ghost {
  background-color: transparent;
  color: var(--color-primary-500);
}

.btn--ghost:hover:not(:disabled) {
  background-color: var(--color-primary-50);
}

/* Sizes */
.btn--sm {
  padding: var(--space-1) var(--space-3);
  min-height: 32px;
  font-size: var(--text-xs);
}

.btn--lg {
  padding: var(--space-3) var(--space-6);
  min-height: 52px;
  font-size: var(--text-base);
}
```

## Card Component

```html
<article class="card">
  <img class="card__image" src="..." alt="...">
  <div class="card__body">
    <h3 class="card__title">Card Title</h3>
    <p class="card__description">Description text goes here.</p>
  </div>
  <footer class="card__footer">
    <span class="card__meta">Metadata</span>
    <button class="btn btn--ghost btn--sm">Action</button>
  </footer>
</article>
```

```css
.card {
  display: flex;
  flex-direction: column;

  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);

  overflow: hidden;
  transition: box-shadow var(--duration-base) var(--ease-out),
              transform var(--duration-base) var(--ease-out);
}

.card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

.card__image {
  aspect-ratio: 16 / 9;
  object-fit: cover;
}

.card__body {
  flex: 1;
  padding: var(--space-4);
}

.card__title {
  font-size: var(--text-lg);
  font-weight: 600;
  margin-bottom: var(--space-2);
}

.card__description {
  color: var(--color-text-secondary);
  font-size: var(--text-sm);
  line-height: var(--leading-relaxed);
}

.card__footer {
  display: flex;
  align-items: center;
  justify-content: space-between;

  padding: var(--space-3) var(--space-4);
  border-top: 1px solid var(--color-border);
}

.card__meta {
  font-size: var(--text-xs);
  color: var(--color-text-muted);
}
```

## Input Component

```html
<div class="field">
  <label for="email" class="field__label">
    Email address
    <span class="field__required">*</span>
  </label>
  <input
    type="email"
    id="email"
    class="field__input"
    placeholder="you@example.com"
    required
    aria-describedby="email-help"
  >
  <p id="email-help" class="field__help">
    We'll never share your email.
  </p>
</div>

<!-- Error state -->
<div class="field field--error">
  <label for="email-error" class="field__label">Email</label>
  <input
    type="email"
    id="email-error"
    class="field__input"
    aria-invalid="true"
    aria-describedby="email-error-msg"
  >
  <p id="email-error-msg" class="field__error" role="alert">
    Please enter a valid email address.
  </p>
</div>
```

```css
.field {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.field__label {
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--color-text);
}

.field__required {
  color: var(--color-error);
}

.field__input {
  padding: var(--space-2) var(--space-3);
  min-height: 44px;

  font-size: var(--text-base);
  color: var(--color-text);

  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);

  transition: border-color var(--duration-fast) var(--ease-out),
              box-shadow var(--duration-fast) var(--ease-out);
}

.field__input::placeholder {
  color: var(--color-text-muted);
}

.field__input:focus {
  outline: none;
  border-color: var(--color-primary-500);
  box-shadow: 0 0 0 3px var(--color-primary-100);
}

.field__help {
  font-size: var(--text-xs);
  color: var(--color-text-muted);
}

/* Error state */
.field--error .field__input {
  border-color: var(--color-error);
}

.field--error .field__input:focus {
  box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.2);
}

.field__error {
  font-size: var(--text-xs);
  color: var(--color-error);
}
```

## Badge Component

```html
<span class="badge">Default</span>
<span class="badge badge--primary">Primary</span>
<span class="badge badge--success">Success</span>
<span class="badge badge--warning">Warning</span>
<span class="badge badge--error">Error</span>
```

```css
.badge {
  display: inline-flex;
  align-items: center;

  padding: var(--space-1) var(--space-2);

  font-size: var(--text-xs);
  font-weight: 500;
  line-height: 1;

  background-color: var(--color-gray-100);
  color: var(--color-gray-700);
  border-radius: var(--radius-full);
}

.badge--primary {
  background-color: var(--color-primary-100);
  color: var(--color-primary-700);
}

.badge--success {
  background-color: #D1FAE5;
  color: #065F46;
}

.badge--warning {
  background-color: #FEF3C7;
  color: #92400E;
}

.badge--error {
  background-color: #FEE2E2;
  color: #991B1B;
}
```

## Modal Component

```html
<div class="modal-backdrop" aria-hidden="true"></div>
<dialog class="modal" aria-labelledby="modal-title">
  <header class="modal__header">
    <h2 id="modal-title" class="modal__title">Modal Title</h2>
    <button class="modal__close" aria-label="Close modal">
      <svg><!-- X icon --></svg>
    </button>
  </header>
  <div class="modal__body">
    <p>Modal content goes here.</p>
  </div>
  <footer class="modal__footer">
    <button class="btn btn--secondary">Cancel</button>
    <button class="btn btn--primary">Confirm</button>
  </footer>
</dialog>
```

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: var(--z-modal-backdrop);

  opacity: 0;
  transition: opacity var(--duration-base) var(--ease-out);
}

.modal-backdrop.is-visible {
  opacity: 1;
}

.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);

  width: min(90vw, 500px);
  max-height: 85vh;

  background-color: var(--color-surface);
  border: none;
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-xl);

  z-index: var(--z-modal);

  opacity: 0;
  transform: translate(-50%, -50%) scale(0.95);
  transition: opacity var(--duration-base) var(--ease-out),
              transform var(--duration-base) var(--ease-out);
}

.modal[open] {
  opacity: 1;
  transform: translate(-50%, -50%) scale(1);
}

.modal__header {
  display: flex;
  align-items: center;
  justify-content: space-between;

  padding: var(--space-4) var(--space-6);
  border-bottom: 1px solid var(--color-border);
}

.modal__title {
  font-size: var(--text-lg);
  font-weight: 600;
}

.modal__close {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 32px;
  height: 32px;

  color: var(--color-text-muted);
  border-radius: var(--radius-md);
  transition: background-color var(--duration-fast) var(--ease-out);
}

.modal__close:hover {
  background-color: var(--color-gray-100);
}

.modal__body {
  padding: var(--space-6);
  overflow-y: auto;
}

.modal__footer {
  display: flex;
  justify-content: flex-end;
  gap: var(--space-3);

  padding: var(--space-4) var(--space-6);
  border-top: 1px solid var(--color-border);
}
```

## Navigation Component

```html
<nav class="nav" aria-label="Main navigation">
  <a href="/" class="nav__logo">
    <img src="logo.svg" alt="Brand">
  </a>

  <ul class="nav__menu">
    <li><a href="#" class="nav__link is-active">Home</a></li>
    <li><a href="#" class="nav__link">Features</a></li>
    <li><a href="#" class="nav__link">Pricing</a></li>
  </ul>

  <div class="nav__actions">
    <button class="btn btn--ghost">Sign In</button>
    <button class="btn btn--primary">Get Started</button>
  </div>
</nav>
```

```css
.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;

  padding: var(--space-4) var(--space-6);

  background-color: var(--color-surface);
  border-bottom: 1px solid var(--color-border);
}

.nav__logo img {
  height: 32px;
}

.nav__menu {
  display: flex;
  gap: var(--space-1);
  list-style: none;
}

.nav__link {
  padding: var(--space-2) var(--space-3);

  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--color-text-secondary);

  border-radius: var(--radius-md);
  transition: color var(--duration-fast) var(--ease-out),
              background-color var(--duration-fast) var(--ease-out);
}

.nav__link:hover {
  color: var(--color-text);
  background-color: var(--color-gray-100);
}

.nav__link.is-active {
  color: var(--color-primary-500);
  background-color: var(--color-primary-50);
}

.nav__actions {
  display: flex;
  gap: var(--space-2);
}
```

## Accessibility Checklist

For every component:

- [ ] Semantic HTML elements
- [ ] Visible focus states (`:focus-visible`)
- [ ] ARIA labels where needed
- [ ] Color contrast meets WCAG AA (4.5:1)
- [ ] Touch targets minimum 44x44px
- [ ] Works with keyboard navigation
- [ ] Respects `prefers-reduced-motion`
