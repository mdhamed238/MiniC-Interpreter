#include "printlib.h"

int main()
{
    int i, MAX;
    i = 1;
    MAX = 100;

    while (i <= MAX)
    {
        if (i % 10 == 0)
        {
            println_int(i);
        }
        i = i + 1;
    }
    return 0;
}

// EXPECTED
// 10
// 20
// 30
// 40
// 50
// 60
// 70
// 80
// 90
// 100