#include "printlib.h"

int main() {
    int a, b, c;
    a = 5;
    b = 5;
    c = 10;

    if (a >= b) {
        println_string("a is greater than or equal to b");
    } else {
        println_string("a is not greater than or equal to b");
    }

    if (a >= c) {
        println_string("a is greater than or equal to c");
    } else {
        println_string("a is not greater than or equal to c");
    }

    return 0;
}

// EXPECTED
// a is greater than or equal to b
// a is not greater than or equal to c
