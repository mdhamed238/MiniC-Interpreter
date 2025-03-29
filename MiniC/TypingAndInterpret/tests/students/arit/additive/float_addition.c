#include "printlib.h"

int main()
{
  float x, y;

  x = 42.98 + 8.33;
  println_float(x);

  y = 19.99 + 7.68;
  println_float(y);

  return 0;
}

// EXPECTED
// 51.31
// 27.67
