#include "printlib.h"

int main()
{
    int a, b;
    a = 1;
    b = 3;

    if(a < 0 || a < b) {
        println_int(1);
    }
    return 0;
}

// EXPECTED
// 1