#include "printlib.h"

int main(){
  int x;
  x = 23 % 5;
  println_int(x);
  
  return 0;
}

// EXPECTED
// 3