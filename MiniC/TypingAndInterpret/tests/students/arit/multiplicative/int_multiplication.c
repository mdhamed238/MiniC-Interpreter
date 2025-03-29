#include "printlib.h"

int main()
{
  int x, y;

  x = 9 *  27;
  println_int(x);

  y = 14 * 7;
  println_int(y);

  return 0;
}

// EXPECTED
// 243
// 98
