#include "printlib.h"

int main()
{
    bool a;
    int x;
    a = true;
    x = 0;

    if (a && (x != 0))
    {
        println_string("a is true and x is not zero");
    }
    else
    {
        println_string("Either a is false or x is zero");
    }

    return 0;
}

// EXPECTED
// Either a is false or x is zero
