#include "printlib.h"

int main() {
    int a, b, c;
    a = 5;
    b = 10;
    c = 5;

    // Testing relational operators combined with AND (&&)
    if (a < b && b > c) {
        println_string("a is less than b and b is greater than c");
    } else {
        println_string("a is not less than b and b is greater than c");
    }

    // Testing relational operators combined with OR (||)
    if (a > b || b >= c) {
        println_string("a is greater than b or b is greater than or equal to c");
    } else {
        println_string("a is not greater than b or b is not greater than or equal to c");
    }

    // More complex condition using AND (&&)
    if (a < b && b > c && c <= a) {
        println_string("a is less than b, b is greater than c, and c is less than or equal to a");
    } else {
        println_string("The complex condition with AND is not satisfied");
    }

    // More complex condition using OR (||)
    if (a > b || b <= c || a >= c) {
        println_string("Either a is greater than b, b is less than or equal to c, or a is greater than or equal to c");
    } else {
        println_string("None of the OR conditions are satisfied");
    }


    return 0;
}

// EXPECTED
// a is less than b and b is greater than c
// a is not greater than b or b is not greater than or equal to c
// a is less than b, b is greater than c, and c is less than or equal to a
// Either a is greater than b, b is less than or equal to c, or a is greater than or equal to c