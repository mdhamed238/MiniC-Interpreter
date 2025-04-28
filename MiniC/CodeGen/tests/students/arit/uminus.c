#include "printlib.h"

int main()
{
    int m, n;
    m = 17;
    n = -m;
    println_int(m);
    println_int(n);
    return 0;
}

// EXPECTED
// 17
// -17
