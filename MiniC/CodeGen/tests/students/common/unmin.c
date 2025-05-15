#include "printlib.h"
int main()
{

    println_int(2 * 3);
    println_int(-2 * 3);
    println_int(2 * -3);
    println_int(-2 * -3);

    println_int(2 * -3 - 3);
    println_int(-2 * -3 - 3);
    println_int(-2 * -3 - 3 * 2);

    return 0;
}

// EXPECTED
// 6
// -6
// -6
// 6
// -9
// 3
// 0