#include "printlib.h"

int main() {
    int x;
    x = 9;

    if(x > 10) {
        println_string("x is greater than 5");
    } else {
        println_string("x is less than 10");
    }
    return 0;
}

// EXPECTED
// x is less than 10