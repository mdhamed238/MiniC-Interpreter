#include "printlib.h"

int main() {
    int a, b, c;
    a = 5;
    b = 3;
    c = 10;

    if (a > b) {
        println_string("a is greater than b");
    } else {
        println_string("a is not greater than b");
    }

    if (a > c) {
        println_string("a is greater than c");
    } else {
        println_string("a is not greater than c");
    }

    return 0;
}

// EXPECTED
// a is greater than b
// a is not greater than c
