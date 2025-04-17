#include "printlib.h"

int main()
{
    int a, b, c;
    a = 12;
    b = 3;
    c = -(a*b) + (a/b);

    println_int(c);
    return 0;
}

// EXPECTED
// -32