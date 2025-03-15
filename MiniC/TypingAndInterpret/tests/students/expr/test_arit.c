#include "printlib.h"

int main() {
    int a, b, res_i;
    float x, y, res_f;
    
    a = 10;
    b = 3;
    
    // Integer arithmetic
    res_i = a + b;
    println_int(res_i);
    
    res_i = a - b;
    println_int(res_i);
    
    res_i = a * b;
    println_int(res_i);
    
    res_i = a / b;
    println_int(res_i);
    
    res_i = a % b;
    println_int(res_i);
    
    // Float arithmetic
    x = 10.5;
    y = 2.5;
    
    res_f = x + y;
    println_float(res_f);
    
    res_f = x - y;
    println_float(res_f);
    
    res_f = x * y;
    println_float(res_f);
    
    res_f = x / y;
    println_float(res_f);
    
    return 0;
}


// SKIP TEST EXPECTED
// EXPECTED
// 13
// 7
// 30
// 3
// 1
// 13.00
// 8.00
// 26.25
// 4.20