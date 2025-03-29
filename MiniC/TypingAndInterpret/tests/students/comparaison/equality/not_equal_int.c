#include "printlib.h"

int main()
{
    int a, b;
    a = 5;
    b = 7;

    if (a != b)
    {
        println_string("a and b are not equal");
    }
    else
    {
        println_string("a and b are equal");
    }

    return 0;
}

// EXPECTED
// a and b are not equal

