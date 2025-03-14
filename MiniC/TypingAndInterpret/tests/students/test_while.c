#include "printlib.h"

int main(){
  int x;
  x = 5;

  while(x > 0) {
    println_int(x);
    x = x - 1;
  }

  return 0;
}

// EXPECTED
// 5
// 4
// 3
// 2
// 1