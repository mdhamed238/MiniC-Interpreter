#include "printlib.h"

int main()
{
  float x, y;

  x = 49.98 / 16.33;
  println_float(x);

  y = 13.22 / 0.15;
  println_float(y);

  return 0;
}

// EXPECTED
// 3.06
// 88.13
