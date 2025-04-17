#include "printlib.h"

int main()
{
    int a;
    a = 15;

    if (a % 3 == 0 && a % 5 == 0)
    {
        println_int(35);
    }
    else if (a % 3 == 0)
    {
        println_int(3);
    }
    else if (a % 5 == 0)
    {
        println_int(5);
    }
    return 0;
}

// EXPECTED
// 35