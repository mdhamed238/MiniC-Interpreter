#include "printlib.h"

int main() {
    int i, j;
    i = 1;

    // Outer loop: counts from 1 to 3
    while (i <= 3) {
        println_int(i);
        j = 1;
        
        // Inner loop counts from 1 to 2
        while(j <= 2) {
            println_int(j);
           j = j+1;
        }

        i = i + 1;
    }

    return 0;
}

// EXPECTED
// 1
// 1
// 2
// 2
// 1
// 2
// 3
// 1
// 2
