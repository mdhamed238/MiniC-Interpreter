#include "printlib.h"

int main()
{
    int a, b, c;
    a = 5;
    b = 5;
    c = 10;

    println_bool(a == b); 
    println_bool(a == c); 

    return 0;
}

// EXPECTED
// 1
// 0
