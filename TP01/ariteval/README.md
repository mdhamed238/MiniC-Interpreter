# LAB1, Aithmetic expressions interpreter
MIF08, 2024-2025
Mohamed Hamed MOHAMED AHMED

## Code functionality
This directory contains an interpreter that can evaluate any "valid" arithmic expression (except for division) like: 5+3; 5-3; --3 * 4; 3*5; (2+3) *4; ...etc. The interpreter will evaluate the arithmetic exprssions and prints their value on the standard ouput (most likely your terminal).
## How to use the code
1. Compile the code, it will generate `AritParser.py` and `AritLexer.py`
```bash
make
```
2. Run the code
```bash
make run
```
3. Now, you can type any arithmetic expression in the terminal and the interpreter will evaluate it and print it.


> You can only imagine what you can do with software.


**NOTE:** 
- Every expression must end with a semicolon.
- If you want to type another expression , you can simply go to a new line.
- Once you have typed all your arithmetic expressions and you want to see the results,  you can simply type `^D` on you keyboard and the interpreter will evaluate them in a blink of an eye.
- `^C` will terminate the program.
- **^D and ^C mean respectively Control+D and Control+C**
## Design choices
Since every atom gets its value from the lexer as an integer, already handles parantheses, then this side is all good. 
On expression level, atoms get parsed as expressions. Expressions are hanled as follows:
* Unary Minus: "--" is priotized over all operators, any expression preceded by that is postive. Example: ```--5 = 5```.
* Binary Minus: the interpreter simply substracts the 2nd expression's value from 1st expression's value. Example: ```5 - 2 = 3```.
* Multiplication: the interpreter simply multiplies the values of expressions. Example: ```12 *  2 = 24```.
* Addition: the interpreter simply adds the values of expressions. Example: ```7 + 4 = 11```.

**Precedance and associativity**
- Precedance: in this order: 
    1. Parantheses
    2. Unary Minus
    3. Multiplication
    4. Substraction
    5. Addition.
- Associativity: 
    * Multiplication, addition and substraction are left-associative.
    * Unary Minus is right-associative.


With all that been said, it's your turn to try it!
## Known bugs

N/A
