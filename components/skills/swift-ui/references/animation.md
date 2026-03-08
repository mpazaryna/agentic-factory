# Animation

SwiftUI animation patterns: implicit, explicit, transitions, and springs.

## Implicit Animation

Automatically animates when value changes.

```swift
struct ImplicitExample: View {
    @State private var scale: CGFloat = 1.0

    var body: some View {
        Circle()
            .fill(.blue)
            .frame(width: 100, height: 100)
            .scaleEffect(scale)
            .animation(.easeInOut(duration: 0.3), value: scale)
            .onTapGesture {
                scale = scale == 1.0 ? 1.5 : 1.0
            }
    }
}
```

### Animation Types

```swift
.animation(.linear(duration: 0.3), value: someValue)
.animation(.easeIn(duration: 0.3), value: someValue)
.animation(.easeOut(duration: 0.3), value: someValue)
.animation(.easeInOut(duration: 0.3), value: someValue)

// Spring
.animation(.spring(response: 0.3, dampingFraction: 0.6), value: someValue)
.animation(.spring(response: 0.5, dampingFraction: 0.8, blendDuration: 0), value: someValue)

// Bouncy (iOS 17+)
.animation(.bouncy, value: someValue)
.animation(.bouncy(duration: 0.4, extraBounce: 0.2), value: someValue)

// Snappy (iOS 17+)
.animation(.snappy, value: someValue)
```

## Explicit Animation

Wrap state changes in `withAnimation`.

```swift
struct ExplicitExample: View {
    @State private var isExpanded = false

    var body: some View {
        VStack {
            Button("Toggle") {
                withAnimation(.spring(response: 0.3, dampingFraction: 0.7)) {
                    isExpanded.toggle()
                }
            }

            if isExpanded {
                Text("Expanded content")
                    .padding()
                    .background(.blue.opacity(0.2))
            }
        }
    }
}
```

### Animation Completion (iOS 17+)

```swift
withAnimation(.easeOut(duration: 0.3)) {
    isVisible = false
} completion: {
    // Called when animation completes
    removeItem()
}
```

## Transitions

Control how views appear and disappear.

```swift
struct TransitionExample: View {
    @State private var showDetail = false

    var body: some View {
        VStack {
            Button("Show") {
                withAnimation {
                    showDetail.toggle()
                }
            }

            if showDetail {
                DetailView()
                    .transition(.move(edge: .bottom))
            }
        }
    }
}
```

### Built-in Transitions

```swift
.transition(.opacity)                    // Fade
.transition(.scale)                      // Scale from center
.transition(.scale(scale: 0.5))         // Custom scale
.transition(.slide)                      // Slide from leading
.transition(.move(edge: .bottom))       // Move from edge
.transition(.push(from: .trailing))     // Push (iOS 16+)

// Combined
.transition(.opacity.combined(with: .scale))
.transition(.move(edge: .bottom).combined(with: .opacity))
```

### Asymmetric Transitions

Different animations for insert/remove.

```swift
.transition(.asymmetric(
    insertion: .move(edge: .trailing).combined(with: .opacity),
    removal: .move(edge: .leading).combined(with: .opacity)
))
```

### Custom Transitions

```swift
extension AnyTransition {
    static var slideAndFade: AnyTransition {
        .asymmetric(
            insertion: .move(edge: .trailing).combined(with: .opacity),
            removal: .scale.combined(with: .opacity)
        )
    }
}

// Usage
DetailView()
    .transition(.slideAndFade)
```

## Spring Animation

Natural, physics-based motion.

```swift
// Response: Duration to reach target (lower = faster)
// Damping: Bounciness (0 = endless, 1 = no bounce)
.spring(response: 0.3, dampingFraction: 0.6)

// Presets
.spring()                                    // Default spring
.interactiveSpring()                        // For gestures
.interpolatingSpring(stiffness: 200, damping: 15)  // Physics-based
```

### Spring Recommendations

| Feel | Response | Damping |
|------|----------|---------|
| Snappy | 0.2–0.3 | 0.7–0.8 |
| Natural | 0.3–0.5 | 0.6–0.7 |
| Bouncy | 0.4–0.6 | 0.4–0.6 |
| Gentle | 0.5–0.8 | 0.8–1.0 |

## Gesture-Driven Animation

```swift
struct DragExample: View {
    @State private var offset = CGSize.zero
    @State private var isDragging = false

    var body: some View {
        Circle()
            .fill(.blue)
            .frame(width: 100, height: 100)
            .scaleEffect(isDragging ? 1.2 : 1.0)
            .offset(offset)
            .gesture(
                DragGesture()
                    .onChanged { value in
                        offset = value.translation
                        withAnimation(.interactiveSpring()) {
                            isDragging = true
                        }
                    }
                    .onEnded { _ in
                        withAnimation(.spring(response: 0.3, dampingFraction: 0.6)) {
                            offset = .zero
                            isDragging = false
                        }
                    }
            )
    }
}
```

## Phase Animator (iOS 17+)

Multi-step animations.

```swift
struct PulseView: View {
    @State private var isAnimating = false

    var body: some View {
        Circle()
            .fill(.blue)
            .frame(width: 100, height: 100)
            .phaseAnimator([false, true]) { content, phase in
                content
                    .scaleEffect(phase ? 1.2 : 1.0)
                    .opacity(phase ? 0.7 : 1.0)
            } animation: { phase in
                .easeInOut(duration: 0.8)
            }
    }
}
```

## Keyframe Animation (iOS 17+)

```swift
struct BounceView: View {
    @State private var trigger = false

    var body: some View {
        Circle()
            .fill(.blue)
            .frame(width: 100, height: 100)
            .keyframeAnimator(initialValue: AnimationValues(), trigger: trigger) { content, value in
                content
                    .scaleEffect(value.scale)
                    .offset(y: value.verticalOffset)
            } keyframes: { _ in
                KeyframeTrack(\.scale) {
                    SpringKeyframe(1.2, duration: 0.2)
                    SpringKeyframe(1.0, duration: 0.2)
                }
                KeyframeTrack(\.verticalOffset) {
                    SpringKeyframe(-20, duration: 0.2)
                    SpringKeyframe(0, duration: 0.2)
                }
            }
            .onTapGesture {
                trigger.toggle()
            }
    }
}

struct AnimationValues {
    var scale: CGFloat = 1.0
    var verticalOffset: CGFloat = 0
}
```

## Reduced Motion

Respect user's accessibility setting.

```swift
struct AccessibleAnimation: View {
    @Environment(\.accessibilityReduceMotion) var reduceMotion
    @State private var isExpanded = false

    var body: some View {
        VStack {
            content
        }
        .onChange(of: isExpanded) { _, newValue in
            // Skip animation if reduced motion is on
        }
    }

    func toggle() {
        if reduceMotion {
            isExpanded.toggle()
        } else {
            withAnimation(.spring()) {
                isExpanded.toggle()
            }
        }
    }
}
```

## Best Practices

1. **Keep It Fast** - Most UI animations should be 200-300ms
2. **Use Springs** - More natural than linear/ease curves
3. **Respect Reduce Motion** - Check `accessibilityReduceMotion`
4. **Animate Transforms** - scale, rotation, offset are GPU-accelerated
5. **Avoid Animating Layout** - Prefer transform over frame changes
6. **Match Purpose** - Entrance = ease-out, exit = ease-in
