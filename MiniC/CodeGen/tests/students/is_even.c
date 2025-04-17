#include "printlib.h"

int main()
{
    int a, b;
    bool is_even;
    a = 7;
    b = 12;

    is_even = (a%2) == 0;
    println_bool(is_even);

    is_even = (b%2) == 0;
    println_bool(is_even);

    return 0;
}

// EXPECTED
// 0
// 1