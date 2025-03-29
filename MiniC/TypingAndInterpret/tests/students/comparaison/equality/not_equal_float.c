#include <printlib.h>

int main() {
    float a, b;
    a = 3.14;
    b = 2.71;

    if (a != b) {
        println_string("a and b are not equal");
    } else {
        println_string("a and b are equal");
    }


    return 0;
}

// EXPECTED
// a and b are not equal
