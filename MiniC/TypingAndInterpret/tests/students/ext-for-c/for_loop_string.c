#include "printlib.h"

int main()
{
    int i;
    string name;
    name = "Med";

    for (i = 1; i < 4; i = i + 1)
    {
        println_string("Hello " + name + "!");
    }

    return 0;
}

// SKIP TEST EXPECTED
// EXPECTED
// Hello Med! 
// Hello Med! 
// Hello Med! 
