#include "printlib.h"

int main() {
    int i, j, k;
    float x, y, z;
    
    i = 1;
    j = 2;
    k = 3;
    
    x = 1.1;
    y = 2.2;
    z = 3.3;
    
    println_int(i);
    println_int(j);
    println_int(k);
    
    println_float(x);
    println_float(y);
    println_float(z);
    
    return 0;
}


// SKIP TEST EXPECTED
// EXPECTED
// 1
// 2
// 3
// 1.10
// 2.20
// 3.30