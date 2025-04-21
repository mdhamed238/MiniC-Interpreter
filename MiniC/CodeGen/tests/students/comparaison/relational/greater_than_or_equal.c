#include "printlib.h"

int main() {
    int a, b, c;
    a = 5;
    b = 5;
    c = 10;

    if (a >= b) {
        println_int(a);
    } else {
        println_int(b);
    }

    if (a >= c) {
        println_int(a);
    } else {
        println_int(c);
    }

    return 0;
}

// EXPECTED
// 5
// 10
