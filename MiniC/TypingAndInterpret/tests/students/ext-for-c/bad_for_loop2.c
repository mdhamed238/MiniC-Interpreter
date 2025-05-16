#include "printlib.h"

int main()
{
    int i;

    if (i < 10)
    {
        continue;
    }

    return 0;
}

// SKIP TEST EXPECTED
// EXPECTED
// EXITCODE 2
// 'continue' statement not in loop statement
