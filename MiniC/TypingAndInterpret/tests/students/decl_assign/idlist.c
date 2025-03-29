#include "printlib.h"

int main() {
    int i, j;
    string a, b;
    float x, y;
    bool m, n;
    
    i = 1;
    j = 2;

    x = 1.1;
    y = 2.2;

    a = "Hello";
    b = "World";

    m = true;
    n = false;
    
    println_int(i);
    println_int(j);
    
    println_float(x);
    println_float(y);

    println_string(a);
    println_string(b);

    println_bool(m);
    println_bool(n);
    
    return 0;
}


// EXPECTED
// 1
// 2
// 1.10
// 2.20
// Hello
// World
// 1
// 0