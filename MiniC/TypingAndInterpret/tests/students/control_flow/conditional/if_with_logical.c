#include "printlib.h"

int main() {
    int a, b, c;
    a = 5;
    b = 10;
    c = 0;

    // Using AND logical operator
    if (a < b && b > 5) {
        println_string("Condition with AND is true: a < b AND b > 5");
    } else {
        println_string("Condition with AND is false");
    }

    // Using OR logical operator
     if (a > b || b > 5) {
        println_string("Condition OR is true: a > b OR b > 5");
    } else {
        println_string("Condition with OR is false");
    }

    if (a > 10 && c == 0) {
        println_string("This condition should be false");
    } else {
        println_string("Condition with AND and false comparison is false");
    }

    return 0;
}

// EXPECTED
// Condition with AND is true: a < b AND b > 5
// Condition OR is true: a > b OR b > 5
// Condition with AND and false comparison is false
