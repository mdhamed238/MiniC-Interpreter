# Extension for MiniC

## Implement these features
* C-like *for* loop
    - [X] Add syntax in `MiniC.g4`
    - [X] Typing visitor in `MiniCTypingVisitor`
    - [X] Interpreter visitor in `MiniCInterpretVisitor`
    - [X] Simple For loop counter
    - [X] Infinite loop test, with a statement that stops the loop, e.g Division by 0
    - [X] Tests pass with Lab 2 interpreter, make test-test-interpret
    - [ ] 3@ code generation: `MiniCCodeGen3AVisitor`
    - [ ] All-in-mem allocator, `AllInMemAllocator`

-  *Continue* statement


## Steps, for each feature
* Add syntax in `MiniC.g4`
* Typing visitor in `MiniCTypingVisitor`
* Interpreter visitor in `MiniCInterpretVisitor`
* 3@ code generation
* All-in-mem allocator
* Write tests, should work with both interpreter (Lab 2) and Compiler (Lab 4)