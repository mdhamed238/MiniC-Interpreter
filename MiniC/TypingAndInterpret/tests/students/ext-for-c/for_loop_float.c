#include "printlib.h"

int main()
{
    float i;
    float result;

    for (i = 0.75; i < 15.0; i = i + 1.5)
    {
        result = result + i;
    }

    println_float(result);

    return 0;
}

// EXPECTED
// 75.00
