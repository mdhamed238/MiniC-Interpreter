#include "printlib.h"

int main() {
    bool a;
    int x;
    
    a = false;
    x = 10;

    if (a || (x != 0)) {
        println_string("Either true or nonzero");
    } else {
        println_string("False and zero");
    }

    return 0;
}

// EXPECTED
// Either true or nonzero

