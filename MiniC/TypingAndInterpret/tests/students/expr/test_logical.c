#include "printlib.h"

int main()
{
    bool a, b;
    b = true;

    if (a && b)
    {
        println_string("Both are True");
    }
    else {
        if(a) {
            println_string("a is True");
        } else if(b) {
            println_string("b is True");
        } else {
            println_string("Both are False");
        }
    }
    return 0;
}


// EXPECTED
// b is True