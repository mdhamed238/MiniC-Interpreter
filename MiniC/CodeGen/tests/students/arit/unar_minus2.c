#include "printlib.h"

int main()
{
    int a;

    a = -(-5);
    println_int(a);
    a = -(-4) * 9;
    println_int(a);
    a = -3;
    println_int(a);
    a = 3 - (-1);
    println_int(a);
    a = -0;
    println_int(a);

    return 0;
}

// EXPECTED
// 5
// 36
// -3
// 4
// 0