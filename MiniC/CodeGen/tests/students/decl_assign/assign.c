#include "printlib.h"

int main() {
    int x;
    bool b;
    
    x = 42;
    b = true;
    
    println_int(x);
    println_bool(b);
    
    return 0;
}


// EXPECTED
// 42
// 1
