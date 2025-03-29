#include "printlib.h"

int main() {
    int a, b, c;
    a = 5;
    b = 3;
    c = 10;

    if (a < b) {
        println_string("a is less than b");
    } else {
        println_string("a is not less than b");
    }

    if (a < c) {
        println_string("a is less than c");
    } else {
        println_string("a is not less than c");
    }

    return 0;
}

// EXPECTED
// a is not less than b
// a is less than c
