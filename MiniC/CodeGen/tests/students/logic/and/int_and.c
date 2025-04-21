#include "printlib.h"

int main()
{
    int x, y;
    x = 1;
    y = 2;

    println_bool((x != 0) && (y != 0));

    return 0;
}

// EXPECTED
// 1
