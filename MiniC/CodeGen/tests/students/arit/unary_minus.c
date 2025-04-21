#include "printlib.h"

int main() {
    int pos, neg, zero, result;
    pos = 10;
    neg = -5;
    zero = 0;

    result = -pos;
    println_int(result); 

    result = -neg;
    println_int(result); 

    result = -zero;
    println_int(result);
    return 0;
}

// EXPECTED
// -10
// 5
// 0