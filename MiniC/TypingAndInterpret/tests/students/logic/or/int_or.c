#include "printlib.h"

int main() {
    int x, y;
    x = 0;
    y = 5;

    if ((x != 0) || (y != 0)) {
        println_string("At least one nonzero");
    } else {
        println_string("Both zero");
    }

    return 0;
}

// EXPECTED
// At least one nonzero
