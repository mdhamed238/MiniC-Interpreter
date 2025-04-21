#include "printlib.h"

int main()
{
    int a, b, c;
    a = 5;
    b = 5;
    c = 10;

    println_int(a == b); 
    println_int(a == c); 

    return 0;
}

// EXPECTED
// 1
// 0
