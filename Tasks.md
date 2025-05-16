# Extension for MiniC

## Implement these features

- C-like _for_ loop
  - [x] Add syntax in `MiniC.g4`
  - [x] Typing visitor in `MiniCTypingVisitor`
  - [x] Interpreter visitor in `MiniCInterpretVisitor`
  - [x] Simple For loop counter
  - [x] Infinite loop test, with a statement that stops the loop, e.g Division by 0
  - [x] Tests pass with Lab 2 interpreter, make test-test-interpret
  - [x] 3@ code generation: `MiniCCodeGen3AVisitor`
  - [x] All-in-mem allocator, `AllInMemAllocator`

* _Continue_ statement
  - [x] Add syntax in `MiniC.g4`
  - [x] Typing visitor in `MiniCTypingVisitor`
  - [x] Interpreter visitor in `MiniCInterpretVisitor`
  - [x] Simple For loop counter
  - [x] Infinite loop test, with a statement that stops the loop, e.g Division by 0
  - [x] Tests pass with Lab 2 interpreter, make test-test-interpret
  - [x] 3@ code generation: `MiniCCodeGen3AVisitor`
  - [x] All-in-mem allocator, `AllInMemAllocator`

## Steps, for each feature

- Add syntax in `MiniC.g4`
- Typing visitor in `MiniCTypingVisitor`
- Interpreter visitor in `MiniCInterpretVisitor`
- 3@ code generation
- All-in-mem allocator
- Write tests, should work with both interpreter (Lab 2) and Compiler (Lab 4)
