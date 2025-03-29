#include "printlib.h"

int main() {

    int i ;
    i = 1;

    while (i <= 15) {
        if (i % 3 == 0 && i % 5 == 0) {
            println_string("FizzBuzz");
        } else if (i % 3 == 0) {
            println_string("Fizz");
        } else if (i % 5 == 0) {
            println_string("Buzz");
        } else {
            println_int(i);
        }

        i = i + 1;
    }

    return 0;
}

// EXPECTED
// 1
// 2
// Fizz
// 4
// Buzz
// Fizz
// 7
// 8
// Fizz
// Buzz
// 11
// Fizz
// 13
// 14
// FizzBuzz
