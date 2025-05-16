#include "printlib.h"

int main()
{
    int i;

    for (; ;)
    {
        i = i+1;
        if(i > 666) {
            println_int(i % 0);
        }
    }

    return 0;
}

// SKIP TEST EXPECTED
// EXPECTED
// EXECCODE 1
// Division by 0
