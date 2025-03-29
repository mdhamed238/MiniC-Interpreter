#include "printlib.h"

int main() {
    int i;
    i = 1;

    while (i <= 7) {
        if(i % 2 == 0) {
            println_string("Even number");
        } else {
            println_string("Odd number");
        }

        i = i + 1;
    }

    return 0;
}

// EXPECTED
// Odd number
// Even number
// Odd number
// Even number
// Odd number
// Even number
// Odd number