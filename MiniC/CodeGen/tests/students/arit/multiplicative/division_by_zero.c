#include "printlib.h"

int main()
{
    int x, result;
    x = 45;
    result = x / 0;

    return 0;
}

// SKIP TEST EXPECTED
// EXPECTED
// EXECCODE 1
// Division by 0