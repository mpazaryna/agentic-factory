# How to Use swift-ui

## Basic Usage

Describe what you're building:

```
"Build me a card component"
"How do I pass data between views?"
"Create a grid layout"
"Add a spring animation to this button"
```

## Modes

### 1. View Composition
For building and structuring views:

```
"Build a profile card component"
"What's the right modifier order?"
"Create a custom view modifier"
```

### 2. State Management
For data flow and property wrappers:

```
"When do I use @State vs @Binding?"
"How do I share state across views with Environment?"
"Set up data flow for this feature"
```

### 3. Layout
For positioning and responsive design:

```
"Create a responsive grid"
"How do I use GeometryReader?"
"Build an adaptive layout for iPad"
```

### 4. Animation
For motion and transitions:

```
"Add a spring animation"
"Create a custom transition"
"Animate this list appearance"
```

### 5. Accessibility
For VoiceOver and Dynamic Type:

```
"Make this card accessible"
"Support Dynamic Type"
"Add custom VoiceOver actions"
```

### 6. Architecture
For app structure and data flow patterns:

```
"Do I need a ViewModel for this?"
"How do I inject dependencies?"
"Show me the .task(id:) pattern"
```

## Tips

- **Mention iOS version** - Some APIs are iOS 16+ or iOS 17+
- **Describe the context** - "For a settings screen" helps narrow recommendations
- **Ask about trade-offs** - "@State vs Environment" gets explanation of when to use each
- **Question ViewModels** - Often you don't need them; ask about alternatives

## Combined with swift-lang

For language-level features, use alongside `swift-lang`:

- `swift-ui` for view patterns, state management, architecture
- `swift-lang` for macros, concurrency, testing, generics
