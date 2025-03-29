#include <printlib.h>

int main() {
    string a, b, c;
    a = "Hello";
    b = "Hello";
    c = "World";

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
