#include "printlib.h"

int main()
{
    int i, j, k, l;

    i = 59 % 3;
    println_int(i);
    j = -19 % 3;
    println_int(j);
    k = 27 % -4;
    println_int(k);
    l = -44 % -5;
    println_int(l);

    return 0;
}

// EXPECTED
// 2
// -1
// 3
// -4
