#include "printlib.h"

int main()
{
    bool a, b, c;
    a = true;
    b = false;
    c = true;

    if (a == b)
    {
        println_string("a and b are equal");
    }
    else
    {
        println_string("a and b are not equal");
    }

    if (a == c)
    {
        println_string("a and c are equal");
    }
    else
    {
        println_string("a and c are not equal");
    }

    return 0;
}

// EXPECTED
// a and b are not equal
// a and c are equal
