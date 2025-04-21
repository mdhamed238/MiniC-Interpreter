#include "printlib.h"

int main()
{
    bool a;
    int x;
    a = true;
    x = 0;

   println_bool(a && (x != 0));

    return 0;
}

// EXPECTED
// 0
