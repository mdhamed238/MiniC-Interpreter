#include "printlib.h"

int main()
{
  int x, y;

  x = 117 - 49;
  println_int(x);

  y = 14 - 47;
  println_int(y);

  return 0;
}

// EXPECTED
// 68
// -33
