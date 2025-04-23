#include "printlib.h"

int main()
{
    int a, b;
    a = 5;
    b = 7;

    println_bool(a != b); 

    return 0;
}

// EXPECTED
// 1
