#include "printlib.h"

int main()
{
  float x, y;

  x = 15.48 - 9.09;
  println_float(x);

  y = 14.76 - 15.03;
  println_float(y);

  return 0;
}

// EXPECTED
// 6.39
// -0.27
