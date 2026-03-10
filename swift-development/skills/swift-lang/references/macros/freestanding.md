# Freestanding Macros

Freestanding macros appear on their own, starting with `#`. They generate code at compile time without being attached to existing declarations.

## Types

| Macro Type | Purpose | Returns |
|------------|---------|---------|
| ExpressionMacro | Return an expression (like a global function) | `ExprSyntax` |
| DeclarationMacro | Declare variables, structs, functions | `[DeclSyntax]` |
| CodeItemMacro | Create code items in function/closure body | Experimental |

## ExpressionMacro

Returns an expression that can be used anywhere an expression is valid.

### Expansion Function Signature

```swift
public static func expansion(
    of node: some FreestandingMacroExpansionSyntax,
    in context: some MacroExpansionContext
) -> ExprSyntax
```

### Understanding the Parameters

**`node: FreestandingMacroExpansionSyntax`** - The syntax tree for the macro call including arguments.

Example AST for `#myMacro("argument", String.self, someVar)`:
```
MacroExpansionExprSyntax
├─pound: pound
├─macroName: identifier("myMacro")
├─leftParen: leftParen
├─arguments: LabeledExprListSyntax
│ ├─[0]: LabeledExprSyntax
│ │ ├─expression: StringLiteralExprSyntax
│ │ │ ├─segments: StringLiteralSegmentListSyntax
│ │ │ │ ╰─[0]: StringSegmentSyntax
│ │ │ │   ╰─content: stringSegment("argument")
│ ├─[1]: LabeledExprSyntax
│ │ ├─expression: MemberAccessExprSyntax (String.self)
│ ├─[2]: LabeledExprSyntax
│ │ ├─expression: DeclReferenceExprSyntax (someVar)
├─rightParen: rightParen
```

**`context: MacroExpansionContext`** - Information about where the macro is expanded.
- `lexicalContext` - Array of enclosing contexts (functions, closures, types, etc.)

### Example: Container Name Macro

Returns the name of the enclosing type (class, struct, enum, etc.):

```swift
public struct ContainerNameMacro: ExpressionMacro {
    public static func expansion(
        of node: some FreestandingMacroExpansionSyntax,
        in context: some MacroExpansionContext
    ) -> ExprSyntax {
        let lexicalContext = context.lexicalContext
        if lexicalContext.isEmpty {
            fatalError("Cannot be used at file scope.")
        }

        var containerName: String?
        for ctx in lexicalContext {
            if let name = extractContainerName(ctx) {
                containerName = name
                break
            }
        }

        guard let containerName else {
            fatalError("Must be used inside a type declaration.")
        }

        return "\(literal: containerName)"
    }
}

private func extractContainerName(_ syntax: Syntax) -> String? {
    switch syntax.kind {
    case .classDecl:
        return syntax.as(ClassDeclSyntax.self)?.name.text
    case .structDecl:
        return syntax.as(StructDeclSyntax.self)?.name.text
    case .enumDecl:
        return syntax.as(EnumDeclSyntax.self)?.name.text
    case .actorDecl:
        return syntax.as(ActorDeclSyntax.self)?.name.text
    case .extensionDecl:
        if let ext = syntax.as(ExtensionDeclSyntax.self),
           let type = ext.extendedType.as(IdentifierTypeSyntax.self) {
            return type.name.text
        }
        return nil
    case .protocolDecl:
        return syntax.as(ProtocolDeclSyntax.self)?.name.text
    default:
        return nil
    }
}
```

### Endpoint Declaration

```swift
@freestanding(expression)
public macro containerName() -> String = #externalMacro(
    module: "MyMacrosMacros",
    type: "ContainerNameMacro"
)
```

### Usage

```swift
class MyClass {
    func printName() {
        print(#containerName) // "MyClass"
    }
}
```

## DeclarationMacro

Declares global or block variables, structures, functions, etc.

### Expansion Function Signature

```swift
public static func expansion(
    of node: some FreestandingMacroExpansionSyntax,
    in context: some MacroExpansionContext
) throws -> [DeclSyntax]
```

### Example: ID Generator Macro

```swift
public struct ItsukiIdMacro: DeclarationMacro {
    public static func expansion(
        of node: some FreestandingMacroExpansionSyntax,
        in context: some MacroExpansionContext
    ) throws -> [DeclSyntax] {
        return [
            """
            var id = "itsuki.enjoy-\(raw: UUID().uuidString)"
            """
        ]
    }
}
```

### Endpoint Declaration with Names

Declaration macros must specify what names they introduce:

```swift
@freestanding(declaration, names: named(id))
public macro itsukiId() = #externalMacro(
    module: "MyMacrosMacros",
    type: "ItsukiIdMacro"
)
```

### Name Specifications

| Specification | Meaning |
|--------------|---------|
| `named(name)` | Fixed name |
| `prefixed(prefix)` | Adds prefix to original name |
| `suffixed(suffix)` | Adds suffix to original name |
| `overloaded` | Same name as original (for peer functions) |
| `arbitrary` | Any name |

Multiple names: `names: named(id), named(ID)`

### Usage

```swift
class ClassWithID {
    #itsukiId

    init() {
        print(id) // "itsuki.enjoy-233AA46A-..."
    }
}
```

## Processing Syntax Trees

### Common Pattern: Switch on Kind, Cast to Type

```swift
switch syntax.kind {
case .classDecl:
    let decl = syntax.as(ClassDeclSyntax.self)!
    // Process class declaration

case .functionDecl:
    let decl = syntax.as(FunctionDeclSyntax.self)!
    // Process function declaration

case .variableDecl:
    let decl = syntax.as(VariableDeclSyntax.self)!
    // Process variable declaration

default:
    break
}
```

### Extracting Argument Values

```swift
// Get first argument expression
guard let argument = node.arguments.first?.expression else {
    fatalError("No arguments provided")
}

// For string literal arguments
if let stringLiteral = argument.as(StringLiteralExprSyntax.self),
   let segment = stringLiteral.segments.first?.as(StringSegmentSyntax.self) {
    let stringValue = segment.content.text
}
```

### Building Return Syntax

```swift
// Using literal interpolation (escapes special characters)
return "\(literal: someString)"

// Using raw interpolation (direct insertion)
return "var name = \(raw: variableName)"

// Using token syntax directly (for identifiers, types)
return "func set\(pattern.identifier)(_ value: \(typeAnnotation.type))"
```

## Debugging Macros

Since macros run at compile time, `print` statements don't work. Create a debug macro:

```swift
public struct DebugNodeContextMacro: ExpressionMacro {
    public static func expansion(
        of node: some FreestandingMacroExpansionSyntax,
        in context: some MacroExpansionContext
    ) -> ExprSyntax {
        return "\(literal: """
        Node: \(node.debugDescription)
        Context: \(context.lexicalContext.map(\.debugDescription).joined(separator: "\n"))
        """)"
    }
}
```

In Xcode: Select macro usage > Right-click > Expand Macro to see generated code.

## Resources

- [SwiftSyntax Documentation](https://swiftpackageindex.com/apple/swift-syntax/documentation)
- [Swift AST Explorer](https://swift-ast-explorer.com) - Visualize syntax trees
- [MacroExamples](https://github.com/apple/swift-syntax/tree/main/Examples/Sources/MacroExamples)
