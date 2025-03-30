#include "printlib.h"

int main() {
    bool a, b;
    a = false;
    b = true;
    if (a || b) {
        println_string("At least one is true");
    } else {
        println_string("Both false");
    }

    return 0;
}

// EXPECTED
// At least one is true
