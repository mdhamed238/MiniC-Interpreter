#include "printlib.h"

int main()
{
    println_bool(1 == 1);
    println_bool(1 != 1);
    return 0;
}

// EXPECTED
// 1
// 0