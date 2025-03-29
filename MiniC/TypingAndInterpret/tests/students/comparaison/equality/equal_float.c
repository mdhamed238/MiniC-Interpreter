#include <printlib.h>

int main() {
    float a, b, c;
    a = 3.14;
    b = 3.14;
    c = 2.71;

    if (a == b) {
        println_string("a and b are equal");
    } else {
        println_string("a and b are not equal");
    }

    if (a == c) {
        println_string("a and c are equal");
    } else {
        println_string("a and c are not equal");
    }

    return 0;
}

// EXPECTED
// a and b are equal
// a and c are not equal
