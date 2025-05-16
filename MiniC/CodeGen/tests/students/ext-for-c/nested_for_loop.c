#include "printlib.h"

int main()
{
    int i, j, result;
    result = 0;

    for (i = 1; i < 4; i = i + 1)
    {
        for (j = 1; j < 4; j = j + 1)
        {
            if (i % j == 0) continue;
            result = result + (i * j);
        }
    }
    println_int(result);
    return 0;
}

// EXPECTED
// 17
