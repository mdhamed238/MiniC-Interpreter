#include "printlib.h"

int main() {
    int a, b, c;
    
    a = 10;
    b = 6;
    c = 4;

    println_bool(a > b);
    println_bool(a > c);
    println_bool(b < c);

    println_bool(a > b+c);
    
    println_bool(a >= b+c);
    println_bool(b <= c);
    
    return 0;
}


// SKIP TEST EXPECTED
// EXPECTED
// 1
// 1
// 0
// 0
// 1
// 0
