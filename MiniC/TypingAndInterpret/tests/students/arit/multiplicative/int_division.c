#include "printlib.h"

int main()
{
  int x, y;

  x = 112 / 16;
  println_int(x);

  y = 12/25;
  println_int(y);

  return 0;
}

// EXPECTED
// 7
// 0
