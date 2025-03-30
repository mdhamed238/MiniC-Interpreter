#include "printlib.h"

int main()
{
    int x, y;
    x = 1;
    y = 2;

    if ((x != 0) && (y != 0))
    {
        println_string("Both are not equal to zero");
    }
    else
    {
        println_string("At least one is equal to zero");
    }

    return 0;
}

// EXPECTED
// Both are not equal to zero
