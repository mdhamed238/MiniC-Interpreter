#include "printlib.h"

int main() {
    bool a;
    int x;
    
    a = false;
    x = 10;

    println_bool(a || (x != 0));

    return 0;
}

// EXPECTED
// 1
