#include "printlib.h"

int main()
{
    int x;
    int y;

    x = 5;
    y = 10;

    println_bool(x < y);  
    println_bool(x <= y); 
    println_bool(x > y);  
    println_bool(x >= y); 
    println_bool(x == y); 
    println_bool(x != y); 

    return 0;
}


// SKIP TEST EXPECTED
// EXPECTED
// 1
// 1
// 0
// 0
// 0
// 1