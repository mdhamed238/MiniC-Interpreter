#include "printlib.h"

int main()
{
  int x, y;

  x = 121 + 16;
  println_int(x);

  y =  97 + 221;
  println_int(y);

  return 0;
}

// EXPECTED
// 137
// 318
