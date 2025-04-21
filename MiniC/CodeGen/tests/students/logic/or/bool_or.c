#include "printlib.h"

int main() {
    bool a, b;
    a = false;
    b = true;
   
    println_bool(a || b);

    return 0;
}

// EXPECTED
// 1
