#include "printlib.h"

int main() {
    int a, b, c;
    a = 5;
    b = 10;
    c = 5;

    if (a < b && b > c) {
        println_int(1);
    } else {
        println_int(0);
    }

    if (a > b || b >= c) {
        println_int(1);
    } else {
        println_int(0);
    }

    if (a > b && b > c) {
        println_int(1);
    } else {
        println_int(0);
    }

    if (a > b || c > b) {
        println_int(1);
    } else {
        println_int(0);
    }

    if (a < b && b < c && a == c) {
        println_int(1);
    } else {
        println_int(0);
    }

    if (a > b || b < c || c > a) {
        println_int(1);
    } else {
        println_int(0);
    }

    return 0;
}

// EXPECTED
// 1
// 1
// 0
// 0
// 0
// 0