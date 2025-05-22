# MiniC Compiler and Interpreter

A modular toolchain for the MiniC language, a simplified subset of C. This project includes an interpreter, a 3-address code generator, and several allocation strategies (Naive, All-in-Memory, Hybrid). Developed as part of a Computer Science MSc lab at Université Claude Bernard Lyon 1.

## Author
Mohamed Hamed MOHAMED AHMED

## Setup with Docker
Ensure a consistent environment using Docker:

```bash
# Pull the Docker image
docker pull mmoy/riscv-latex-python:dev

# Run the container
docker run --rm -ti -v "$PWD":/home/compil --user $(id -u):$(id -g) -w /home/compil mmoy/riscv-latex-python:dev
```

## Running Tests
Execute tests inside the development environment:

```bash
# Run all tests
make test

# Run a specific test
make test-interpret FILTER='TypingAndInterpret/tests/arit/multiplicative/modulo.c'

# Test specific patterns
make test FILTER='TypingAndInterpret/tests/**/*division*.c'
```

Run the toolchain manually:
```bash
python3 MiniCC.py --mode eval TypingAndInterpret/tests/arit/multiplicative/modulo.c
```

## Test Infrastructure
Each test file is validated in two ways:
- **Interpreter Check (`test_eval`)**: Runs the interpreter and verifies its output matches the expected result.
- **GCC Execution (`test_expect`)**: Compiles and runs the file using GCC to ensure the annotations in the source file are correct.

If GCC and the interpreter behave differently (e.g., division by zero), the test can be skipped using `// SKIP TEST EXPECTED` in the source file. While some tests may be skipped, all `test_eval` checks should pass.

## Project Overview
This project implements a full MiniC toolchain, including parsing, type checking, interpretation, intermediate code generation (3-address code), and multiple register/memory allocation strategies.

### Key Components
- **Lexer and Parser**: ANTLR4 for syntax analysis.
- **Type Checker**: Ensures type correctness.
- **Interpreter**: Executes MiniC code.
- **3-Address Code Generator**: Produces intermediate code.
- **Allocators**: Naive, All-in-Memory, and Hybrid strategies for register/memory assignment.
- **Test Suite**: High coverage for all components.

## Target Architecture
The toolchain targets **RISC-V**, an open-source instruction set architecture (ISA) designed for efficiency and scalability. MiniC code is compiled to RISC-V assembly for execution on simulators or hardware.

## Reference
Based on [Lab 2: Interpreters and Types](https://matthieu-moy.fr/cours/mif08/tp2.pdf).

## Feedback
Suggestions and improvements are welcome!
