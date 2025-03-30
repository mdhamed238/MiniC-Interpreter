#include "printlib.h"

int main()
{
    string str1, str2, result;
    str1 = "Hello, ";
    str2 = "World!";

    result = str1 + str2;

    println_string(result); // Expected output: "Hello, World!"

    return 0;
}

// SKIP TEST EXPECTED
// EXPECTED
// Hello, World!
