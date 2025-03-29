#include "printlib.h"

int main()
{
    string x, y, result;
    x = "Hello";
    y = "World";
    result = x + " " + y;

    println_string(result);

    return 0;
}

// SKIP TEST EXPECTED
// EXPECTED
// Hello World
