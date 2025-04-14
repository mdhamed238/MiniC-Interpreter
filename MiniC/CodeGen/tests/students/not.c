#include "printlib.h"

int main()
{
    println_bool(!(2==3));
    println_bool(!(2 <= 2));
    return 0;
}

// EXPECTED
// 1
// 0