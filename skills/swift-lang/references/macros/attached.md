# Attached Macros

Attached macros modify declarations they're attached to using `@`. They can add properties, methods, accessors, conformances, and more.

## Types

| Macro Type | Purpose | Attaches To |
|------------|---------|-------------|
| PeerMacro | Add sibling declarations | Properties, functions |
| AccessorMacro | Add get/set accessors | Properties |
| MemberMacro | Add members to types | Classes, structs, enums, actors |
| MemberAttributeMacro | Add attributes to members | Classes, structs, enums, actors |
| ExtensionMacro | Add protocol conformance | Types |
| BodyMacro | Replace function body | Functions |
| PreambleMacro | Insert at function start | Functions (experimental) |

## PeerMacro

Adds new declarations alongside the declaration it's attached to.

### Expansion Function Signature

```swift
public static func expansion(
    of node: AttributeSyntax,
    providingPeersOf declaration: some DeclSyntaxProtocol,
    in context: some MacroExpansionContext
) throws -> [DeclSyntax]
```

### Understanding the Parameters

**`declaration: DeclSyntaxProtocol`** - The declaration the macro is attached to.

Example AST for `@MyMacro var someVariable: Int = 5`:
```
VariableDeclSyntax
├─attributes: AttributeListSyntax
│ ╰─[0]: AttributeSyntax (@MyMacro)
├─bindingSpecifier: keyword(var)
╰─bindings: PatternBindingListSyntax
  ╰─[0]: PatternBindingSyntax
    ├─pattern: IdentifierPatternSyntax
    │ ╰─identifier: identifier("someVariable")
    ├─typeAnnotation: TypeAnnotationSyntax
    │ ╰─type: IdentifierTypeSyntax (Int)
    ╰─initializer: InitializerClauseSyntax
      ╰─value: IntegerLiteralExprSyntax (5)
```

### Example: Add Setter Function

```swift
public struct AddSetterFunctionMacro: PeerMacro {
    public static func expansion(
        of node: AttributeSyntax,
        providingPeersOf declaration: some DeclSyntaxProtocol,
        in context: some MacroExpansionContext
    ) throws -> [DeclSyntax] {
        guard let declaration = declaration.as(VariableDeclSyntax.self) else {
            fatalError("Only works for properties")
        }

        guard declaration.bindingSpecifier.text == "var" else {
            fatalError("Only works for var")
        }

        guard let binding = declaration.bindings.first,
              let pattern = binding.pattern.as(IdentifierPatternSyntax.self),
              let typeAnnotation = binding.typeAnnotation else {
            fatalError("No binding syntax available")
        }

        return ["""
        func set\(raw: pattern.identifier.text.capitalized)(_ value: \(typeAnnotation.type)) {
            \(pattern.identifier) = value
        }
        """]
    }
}
```

### Endpoint Declaration

```swift
@attached(peer, names: arbitrary)
public macro AddSetter() = #externalMacro(
    module: "MyMacrosMacros",
    type: "AddSetterFunctionMacro"
)
```

## AccessorMacro

Adds accessors (get, set, willSet, didSet) to properties.

### Expansion Function Signature

```swift
public static func expansion(
    of node: AttributeSyntax,
    providingAccessorsOf declaration: some DeclSyntaxProtocol,
    in context: some MacroExpansionContext
) throws -> [AccessorDeclSyntax]
```

### Example: UserDefaults Property Wrapper Alternative

```swift
public struct AddUserDefaultsGetSetMacro: AccessorMacro {
    public static func expansion(
        of node: AttributeSyntax,
        providingAccessorsOf declaration: some DeclSyntaxProtocol,
        in context: some MacroExpansionContext
    ) throws -> [AccessorDeclSyntax] {
        // Extract the key argument
        guard case let .argumentList(arguments) = node.arguments,
              let argument = arguments.first else {
            fatalError("UserDefaults key not specified")
        }

        guard let declaration = declaration.as(VariableDeclSyntax.self),
              declaration.bindingSpecifier.text == "var" else {
            fatalError("Only works for var")
        }

        guard let binding = declaration.bindings.first,
              let typeAnnotation = binding.typeAnnotation,
              let optionalType = typeAnnotation.type.as(OptionalTypeSyntax.self) else {
            fatalError("Optional type required")
        }

        return [
            """
            get {
                UserDefaults.standard.value(forKey: \(argument.expression)) as? \(optionalType.wrappedType)
            }
            """,
            """
            set {
                UserDefaults.standard.set(newValue, forKey: \(argument.expression))
            }
            """
        ]
    }
}
```

### Endpoint Declaration

```swift
@attached(accessor)
public macro AddUserDefaults(_ key: String) = #externalMacro(
    module: "MyMacrosMacros",
    type: "AddUserDefaultsGetSetMacro"
)
```

### Accessor Names Requirement

For `get` and `set`: No names needed (`@attached(accessor)`)

For observers: Must specify names:
```swift
@attached(accessor, names: named(willSet), named(didSet))
@attached(accessor, names: named(init), named(get), named(set))
```

Empty array return: Use `willSet` to avoid compiler error.

## MemberMacro

Adds members (properties, methods, types) to type declarations.

### Expansion Function Signature

```swift
public static func expansion(
    of node: AttributeSyntax,
    providingMembersOf declaration: some DeclGroupSyntax,
    conformingTo protocols: [TypeSyntax],
    in context: some MacroExpansionContext
) throws -> [DeclSyntax]
```

### Understanding DeclGroupSyntax

`declaration.memberBlock.members` contains all members of the type:

```
ClassDeclSyntax
├─name: identifier("MyClass")
╰─memberBlock: MemberBlockSyntax
  ├─members: MemberBlockItemListSyntax
  │ ├─[0]: MemberBlockItemSyntax
  │ │ ╰─decl: VariableDeclSyntax (someProperty)
  │ ╰─[1]: MemberBlockItemSyntax
  │   ╰─decl: EnumDeclSyntax (CustomError)
```

### Example: Add Debug Description

```swift
public struct AddDebugDescriptionMacro: MemberMacro {
    public static func expansion(
        of node: AttributeSyntax,
        providingMembersOf declaration: some DeclGroupSyntax,
        conformingTo protocols: [TypeSyntax],
        in context: some MacroExpansionContext
    ) throws -> [DeclSyntax] {
        // Extract property names
        let propertyNames = declaration.memberBlock.members.compactMap { member -> String? in
            guard let varDecl = member.decl.as(VariableDeclSyntax.self),
                  let binding = varDecl.bindings.first,
                  let pattern = binding.pattern.as(IdentifierPatternSyntax.self) else {
                return nil
            }
            return pattern.identifier.text
        }

        let description = propertyNames.map { "\($0): \\(\($0))" }.joined(separator: ", ")

        return ["""
        var debugDescription: String {
            "\(raw: description)"
        }
        """]
    }
}
```

## MemberAttributeMacro

Adds attributes to members of a type (like applying macros to all properties).

### Expansion Function Signature

```swift
public static func expansion(
    of node: AttributeSyntax,
    attachedTo declaration: some DeclGroupSyntax,
    providingAttributesFor member: some DeclSyntaxProtocol,
    in context: some MacroExpansionContext
) throws -> [AttributeSyntax]
```

### Example: Apply UserDefaults to All Properties

```swift
public struct AddUserDefaultsToAllVarMacro: MemberAttributeMacro {
    public static func expansion(
        of node: AttributeSyntax,
        attachedTo declaration: some DeclGroupSyntax,
        providingAttributesFor member: some DeclSyntaxProtocol,
        in context: some MacroExpansionContext
    ) throws -> [AttributeSyntax] {
        // Only apply to variables
        guard let member = member.as(VariableDeclSyntax.self) else {
            return []
        }

        // Extract prefix from macro arguments
        guard case let .argumentList(arguments) = node.arguments,
              let argument = arguments.first,
              let expression = argument.expression.as(StringLiteralExprSyntax.self),
              let segment = expression.segments.first?.as(StringSegmentSyntax.self) else {
            fatalError("Prefix key not specified")
        }
        let prefixKey = segment.content.text

        // Get property name
        guard let binding = member.bindings.first,
              let pattern = binding.pattern.as(IdentifierPatternSyntax.self) else {
            return []
        }

        return ["""
        @AddUserDefaults("\(raw: prefixKey)-\(pattern.identifier)")
        """]
    }
}
```

### Endpoint Declaration

```swift
@attached(memberAttribute)
public macro AddUserDefaultsToAllVariable(keyPrefix: String) = #externalMacro(
    module: "MyMacrosMacros",
    type: "AddUserDefaultsToAllVarMacro"
)
```

## ExtensionMacro

Adds protocol conformance via extensions.

### Expansion Function Signature

```swift
public static func expansion(
    of node: AttributeSyntax,
    attachedTo declaration: some DeclGroupSyntax,
    providingExtensionsOf type: some TypeSyntaxProtocol,
    conformingTo protocols: [TypeSyntax],
    in context: some MacroExpansionContext
) throws -> [ExtensionDeclSyntax]
```

### Understanding the protocols Parameter

`protocols` contains **only protocols the type doesn't already conform to** from those declared in the endpoint.

### Example: Auto-Identifiable

```swift
public struct IdentifiableMacro: ExtensionMacro {
    public static func expansion(
        of node: AttributeSyntax,
        attachedTo declaration: some DeclGroupSyntax,
        providingExtensionsOf type: some TypeSyntaxProtocol,
        conformingTo protocols: [TypeSyntax],
        in context: some MacroExpansionContext
    ) throws -> [ExtensionDeclSyntax] {
        // Check if Identifiable conformance is needed
        let needsIdentifiable = protocols.contains { proto in
            guard let proto = proto.as(IdentifierTypeSyntax.self) else { return false }
            return proto.name.text == "Identifiable"
        }

        guard needsIdentifiable else { return [] }

        return [try ExtensionDeclSyntax(
            """
            extension \(type): Identifiable {
                var id: UUID { UUID() }
            }
            """
        )]
    }
}
```

### Endpoint Declaration

```swift
@attached(extension, conformances: Identifiable, names: named(id))
public macro ConformIdentifiable() = #externalMacro(
    module: "MyMacrosMacros",
    type: "IdentifiableMacro"
)
```

## BodyMacro

Replaces (or creates) the body of a function.

### Expansion Function Signature

```swift
public static func expansion(
    of node: AttributeSyntax,
    providingBodyFor declaration: some DeclSyntaxProtocol & WithOptionalCodeBlockSyntax,
    in context: some MacroExpansionContext
) throws -> [CodeBlockItemSyntax]
```

### Understanding WithOptionalCodeBlockSyntax

Provides `declaration.body: CodeBlockSyntax?` with:
- `body.statements` - The code inside the function

### Example: Throw if Not Implemented

```swift
public struct EmptyFunctionThrowMacro: BodyMacro {
    public static func expansion(
        of node: AttributeSyntax,
        providingBodyFor declaration: some DeclSyntaxProtocol & WithOptionalCodeBlockSyntax,
        in context: some MacroExpansionContext
    ) throws -> [CodeBlockItemSyntax] {
        // Don't replace if body has content
        if let body = declaration.body, !body.statements.isEmpty {
            return []
        }

        return [
            """
            print(#function, "not implemented")
            fatalError("Not implemented")
            """
        ]
    }
}
```

### Endpoint Declaration

```swift
@attached(body)
public macro ErrorIfNotImplemented() = #externalMacro(
    module: "MyMacrosMacros",
    type: "EmptyFunctionThrowMacro"
)
```

## Combining Multiple Roles

A macro can conform to multiple protocols:

```swift
public struct ObservableMacro: MemberMacro, MemberAttributeMacro, ExtensionMacro {
    // Implement all three expansion functions
}
```

Endpoint with multiple roles:
```swift
@attached(member, names: ...)
@attached(memberAttribute)
@attached(extension, conformances: Observable)
public macro Observable() = #externalMacro(...)
```

## Common Patterns

### Extracting String from Arguments

```swift
guard case let .argumentList(arguments) = node.arguments,
      let argument = arguments.first,
      let expression = argument.expression.as(StringLiteralExprSyntax.self),
      let segment = expression.segments.first?.as(StringSegmentSyntax.self) else {
    fatalError("String argument required")
}
let stringValue = segment.content.text
```

### Processing Members

```swift
for member in declaration.memberBlock.members {
    switch member.decl.kind {
    case .variableDecl:
        let varDecl = member.decl.as(VariableDeclSyntax.self)!
        // Process property

    case .functionDecl:
        let funcDecl = member.decl.as(FunctionDeclSyntax.self)!
        // Process method

    case .enumCaseDecl:
        let caseDecl = member.decl.as(EnumCaseDeclSyntax.self)!
        // Process enum case

    default:
        break
    }
}
```

### Getting Property Info

```swift
guard let binding = varDecl.bindings.first,
      let pattern = binding.pattern.as(IdentifierPatternSyntax.self),
      let typeAnnotation = binding.typeAnnotation else {
    continue
}

let propertyName = pattern.identifier.text
let propertyType = typeAnnotation.type
```

## Resources

- [ComplexMacros Examples](https://github.com/apple/swift-syntax/tree/main/Examples/Sources/MacroExamples/Implementation/ComplexMacros)
- [ObservableMacro Implementation](https://github.com/apple/swift-syntax/blob/main/Examples/Sources/MacroExamples/Implementation/ComplexMacros/ObservableMacro.swift)
