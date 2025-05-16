#include <printlib.h>

int main()

{
    int i;

    for (i = 1; i <= 10; i = i + 1) println_int(i);

    return 0;
}

// EXPECTED
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
// 10