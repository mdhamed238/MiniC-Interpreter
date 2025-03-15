#include "printlib.h"

int main() {
    int a,b,c;
    a = 5;
    b = 7;
    c = 7;

    println_bool(a == b);
    println_bool(a != b);

    println_bool(a == c);
    println_bool(a != c);

    println_bool(b == c);
    println_bool(b != c);

    
    return 0;
}


// SKIP TEST EXPECTED
// EXPECTED
// 0
// 1
// 0
// 1
// 1
// 0
