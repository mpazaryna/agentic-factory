---
name: iOS Development Prompts Collection
description: Battle-tested prompts for Swift, SwiftUI, UIKit, Combine, async/await, architecture, and debugging
source: https://medium.com/@nimjerahul/20-chatgpt-prompts-every-senior-ios-developer-should-steal-in-2025-0b7a3e94e092
collected: 2025-02-05
tags: [ios, swift, swiftui, uikit, debugging, architecture, testing]
---

## Debug My Crash Log

```
You are my senior iOS debugging assistant.
Here is the crash log. Identify the root cause, the exact function causing it, and explain the fix.
Also rewrite the problematic code safely.

<PASTE CRASH LOG>
```

## Rewrite to async/await

```
Rewrite this function and all its call sites to async/await.
Keep the logic identical and simplify where possible.

<PASTE CODE>
```

## SwiftUI Redraw Debugger

```
This SwiftUI view is redrawing too much.
Explain why, identify the state causing it, and rewrite it to avoid unnecessary body updates.

<PASTE VIEW>
```

## Architecture Brainstorm

```
Give me 3 architecture options for implementing this feature.
Explain the pros/cons of each.
Recommend the best one for scalability + simplicity.

<DESCRIBE FEATURE>
```

## Combine Pipeline Fix

```
Here is my Combine pipeline.
Explain what's wrong, how to fix it, and rewrite a cleaner version using modern patterns.

<PASTE PIPELINE>
```

## Senior-Level Code Review

```
Review this code as a senior iOS engineer.
Point out architecture smells, potential crashes, naming issues, state issues, and any scalability concerns.
Suggest improvements and rewrite problematic parts.

<PASTE CODE>
```

## Generate Swift Models + Mock Data

```
Convert this JSON into Swift Codable models.
Also generate mock data and a simple decoding test.

<PASTE JSON>
```

## Debug Memory Leak

```
I have a memory leak.
Analyze this code and tell me where the retain cycle is happening, why, and how to fix it.

<PASTE CLASS OR VIEWMODEL>
```

## Simplify Massive ViewController

```
Break this large UIViewController into smaller, modular components.
Explain how to structure the files, and rewrite the key parts.

<PASTE VIEW CONTROLLER>
```

## Convert UIKit to SwiftUI

```
Rewrite this UIKit screen in SwiftUI with the same functionality.
Use MVVM and modern async patterns.

<PASTE UIKIT SCREEN>
```

## Test Case Generator

```
Write XCTest unit tests for this class.
Include edge cases, failure paths, and mock dependencies.

<PASTE CLASS>
```

## Performance Optimizer

```
Analyze this Swift code for performance issues.
Explain the bottlenecks and rewrite an optimized version.

<PASTE FUNCTION>
```

## Reusable Component Extractor

```
Turn this logic into a reusable Swift component with a clean API and configuration.

<PASTE LOGIC>
```

## Data Flow Explainer

```
Explain the full data flow of this feature:
- who owns the state
- what triggers updates
- what each layer is responsible for
- where bugs are likely to appear

<PASTE FEATURE FILES>
```

## Migrate Networking Layer

```
Rewrite this networking layer using:
- URLSession
- async/await
- error handling
- Result types
- reusable request builder

<PASTE NETWORK LAYER>
```

## Generate Module Documentation

```
Generate clean documentation for this module:
- purpose
- responsibilities
- inputs/outputs
- examples
- edge cases
- do's and don'ts

<PASTE CODE>
```

## Improve My Prompt

```
Improve this prompt to make it more detailed, context-aware, and effective for iOS development.

<PASTE PROMPT>
```
