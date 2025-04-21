#include "printlib.h"

int main()
{
    bool a, b, c;
    a = true;
    b = false;
    c = true;

    println_int(a == b); 
    println_int(a == c); 

    return 0;
}

// EXPECTED
// 0
// 1
