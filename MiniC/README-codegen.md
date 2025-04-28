# MiniC Compiler 
LAB4 (simple code generation), MIF08 / CAP 2022-23

# Authors

Mohamed Hamed MOHAMED AHMED

# Contents

This is a naive MiniC interpreter that supports primitive data types(_Intergers_ and _Booleans_), conditional blocks, logic, relational comparaisons and arithmetic operations. From a C file, it generate an AST(Abstract Syntax Tree) using ANTLR Lexing and Parsing. Later on, the interpreter visits this AST to generate the 3 address code which will be treated differently depending on the interpreter. First,  the  __Naive__ interpreter converts the temporaries to RiscV registers which can be really fast at compile time. Nevertheless, this interpreter fails when the temporaries are more than the registers. The __All-in-mem__ interpreter, on the other hand,  stores everything on the memory(stack). Lastly, the __Hybrid__ Allocator is a combination the __Naive__ and __All-in-mem__ allocators, it allocates on RiscV registers, when there are no more registers it uses the memory. Last but not least, this remains a very basic implementation of what real world compilers/interpreters look like.

# Test design 

The main objective was to cover as many test cases as possible to make sure that the interpreter is working as expected.

# Design choices

I attentively followed the instructions of the Labwork and i was able to quickly understand what must be done and how it should be.
My implementation is an abstract representation of the ANTLR grammar for MiniC language. Thus, there are no known limitations since the test coverage is 100% with 100% success.

# Known bugs

There are no limitations or bugs by the time you are reading this document. Any suggestions are highly welcome :D

# Checklists

A check ([X]) means that the feature is implemented 
and *tested* with appropriate test cases.

## Code generation

- [x] Number Atom
- [x] Boolean Atom
- [x] Id Atom
- [x] Additive expression
- [x] Multiplicative expression
- [x] UnaryMinus expression
- [x] Or expression
- [x] And expression
- [x] Equality expression
- [x] Relational expression (! many cases -> many tests)
- [x] Not expression

## Statements

- [x] Prog, assignements
- [x ] While
- [x] Cond Block
- [x] If
- [x] Nested ifs
- [x] Nested whiles

## Allocation

- [x] Naive allocation
- [x] All in memory allocation
- [x] Massive tests of memory allocation

