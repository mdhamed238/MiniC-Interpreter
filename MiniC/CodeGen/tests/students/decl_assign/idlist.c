#include "printlib.h"

int main() {
    int i, j;
    bool m, n;
    
    i = 1;
    j = 2;

    m = true;
    n = false;
    
    println_int(i);
    println_int(j);
    
    println_bool(m);
    println_bool(n);
    
    return 0;
}


// EXPECTED
// 1
// 2
// 1
// 0