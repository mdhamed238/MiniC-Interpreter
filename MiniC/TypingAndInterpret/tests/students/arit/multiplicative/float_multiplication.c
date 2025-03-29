#include "printlib.h"

int main()
{
  float x, y;

  x = 2.33 * 5.09;
  println_float(x);

  y = 14.76 * 0.31;
  println_float(y);

  return 0;
}

// EXPECTED
// 11.86
// 4.58
