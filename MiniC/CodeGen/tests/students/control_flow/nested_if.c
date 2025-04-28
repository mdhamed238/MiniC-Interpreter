#include "printlib.h"

int main()
{
    int x;

    x = 9;

    if (x > 5)
    {
        if (x < 15)
        {
            println_int(1);
        }
        else
        {
            println_int(2);
        }
    }
    else
    {
        println_int(3);
    }

    return 0;
}

// EXPECTED
// 1