#include "printlib.h"

int main() {
    bool a, b;
    a = true; 
    b = false;

    if (a && b) {
        println_string("true AND false is true");
    } else {
        println_string("true AND false is false");
    }

    if (a && a) {
        println_string("true AND true is true");
    } else {
        println_string("true AND true is false");
    }

    return 0;
}

// EXPECTED
// true AND false is false
// true AND true is true
