#include "printlib.h"

int main() {
    bool a,b;
    int x,y;
    
    a = true;
    b = false;
    x = 3;
    y = 0;

    println_bool((a && !b) || (x != 0 && y == 0));

    return 0;
}

// EXPECTED
// 1
