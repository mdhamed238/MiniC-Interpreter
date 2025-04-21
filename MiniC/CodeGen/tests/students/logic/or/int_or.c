#include "printlib.h"

int main() {
    int x, y;
    x = 0;
    y = 5;

    println_bool((x != 0) || (y != 0));

    return 0;
}

// EXPECTED
// 1
