#include "printlib.h"

int main() {
    int i;
    i = 1;

    while (i <= 5) {
        println_int(i);
        i = i + 1;
    }

    return 0;
}

// EXPECTED
// 1
// 2
// 3
// 4
// 5