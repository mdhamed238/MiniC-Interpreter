#include "printlib.h"

int main()
{
  float x;
  x = 11.34;

  if (x > 11.3)
  {
    println_string("x is greater than 11.3");
  }

  return 0;
}

// EXPECTED
// x is greater than 11.3