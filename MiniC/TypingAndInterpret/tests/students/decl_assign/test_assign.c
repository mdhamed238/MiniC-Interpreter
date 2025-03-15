#include "printlib.h"

int main() {
    int x;
    float y;
    bool b;
    string s;
    
    x = 42;
    y = 3.14;
    b = true;
    s = "Hello";
    
    println_int(x);
    println_float(y);
    println_bool(b);
    println_string(s);
    
    return 0;
}


// SKIP TEST EXPECTED
// EXPECTED
// 42
// 3.14
// 1
// Hello