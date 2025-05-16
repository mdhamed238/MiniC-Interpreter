# Lab 5

## New language construct: C-like for loops

## Objective

- Implement the complete chain (syntax, typing, execution via compilation or interpretation) for a language
    construct.
Make sure you have read and understood REGLES-TPs.md on the course homepage.
**Warning:** this document is short, but the lenght of the document is _not_ proportional to the time you’ll need
to finish the lab.

## 5.1 Specification

#### We consider the MiniC language extended with a C-likeforloop. The informal specification of this construct is:

- The syntax is :for (A; B;C)D, where _A_ and _C_ are assignments, _B_ is an expression, and _D_ is a block or
    a single statement.
- _A_ , _B_ and _C_ are optional (i.e. can be left empty)
- If present, _B_ must be Boolean
- The behavior of theforloop for correct MiniC programs is the same as in the C language.

```
Example of correct MiniC for loops (assuming all variables are properly declared):
```
#### for (i=1;i<4;i=i+1) { println_int(i); }

#### for (;j<4.0;j=j+1.5) x = 42;

### EX E RCI S E#1Ï C-like for loops

Extend the language with C-like for loops. You need to support this construct in the interpreter and the compiler,
and to properly reject incorrect programs with the appropriate error. Test your code. This time, you need _nega-
tive tests_ , i.e. MiniC programs that are explicitly rejected by your compiler. You will need to modify files that you
already edited in previous labs, and files that you read but did not modify yet. You are not allowed to modify files

#### inLib/norMiniCC.py. Tests must be added to theMiniC/CodeGen/tests/students/ext-for-c/

#### and MiniC/TypingAndInterpret/tests/students/ext-for-c/ directories (under

#### TypingAndInterpret/CodeGenso that the Makefile targets of lab 2 and 4 still work for us). You may

#### use floats and strings inMiniC/TypingAndInterpret/tests/students/ext-for-c/but not inCodeGen

#### since your code generator cannot deal with them. You can copy tests fromTypingAndInterprettoCodeGen

or vice versa if needed, or use symbolic links.
Your compiler must support the naive and all-in-mem allocation. If you did not finish the all-in-mem or if
it’s broken for your lab 4, it’s time to finish/fix it now. You are not allowed to copy code from other students even
for this part.

### EX ERCI S E#2Ïcontinue statement

#### Add thecontinuestatement to the language. Accepted and rejected programs, and behavior, must be the same

#### as thecontinuestatement of the C language, with the following exception:continuestatements are only valid

#### forforloops (notwhile), and restart the most nestedforloop (ignoringwhileloops). It is OK, and advised,

#### not to use anywhileloops in your tests to focus on theforloop. Follow the same instructions as for thefor

loop for specification, testing and allowed modifications.
This exercice is “short” in the sense that it can be implemented with fewer lines of code (about 50 lines
including comments in our solution), but is also much trickier. The grading scale will give more weight to the

Laure Gonnord, Matthieu Moy, Gabriel Radanne et al. 1/


##### 5.1. SPECIFICATION LAB 5. NEW LANGUAGE CONSTRUCT: C-LIKE FOR LOOPS

#### first exercice (loop withoutcontinuestatement) so that students who did not finish this one can still get a good

grade.

### EX ERCI S E#3Ï Delivery

This lab is due on TOMUSS (deadline on the course’s homepage). Python code and C testcases will be graded.
We recall that your work is **personal** ; code and tests copy from any source or sharing is **strictly forbidden**. As

#### usual, upload an archive containing the wholeMiniCdirectory (make tardoes that for you).

#### It is good habit to document your work, you can do so by creating a fileREADME-for.md. It won’t be taken

into account in the grade, but may be useful to document your choice in case you disagree with the automatic
correction.

Laure Gonnord, Matthieu Moy, Gabriel Radanne et al. 2/


