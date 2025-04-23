#include "printlib.h"

int main()
{
    bool a, b, c;
    a = true;
    b = false;
    c = true;

    println_bool(a == b); 
    println_bool(a == c); 

    return 0;
}

// EXPECTED
// 0
// 1
