#include "printlib.h"

int main()
{
    int i;

    for (i = 1; i < 4; i = i + 1)
    {
        if (i == 2)
        {
            continue;
        }
        println_int(i);
    }

    return 0;
}

// EXPECTED
// 1
// 3
