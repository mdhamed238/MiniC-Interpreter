#include "printlib.h"

int main()
{
    bool a, b;
    a = true;
    b = false;

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
