#include "printlib.h"

int main() {
    bool a,b;
    int x,y;
    
    a = true;
    b = false;
    x = 3;
    y = 0;

    if ((a && !b) || (x != 0 && y == 0)) {
        println_string("Logical expression is true");
    } else {
        println_string("Logical expression is false");
    }

    return 0;
}

// EXPECTED
// Logical expression is true
