#include "printlib.h"

int main(){
  int x;
  x = 37;
  if(x > 40) {
    println_string("x is greater than 40");
  } else {
    println_string("x is less than 40");
  }

  return 0;
}

// EXPECTED
// x is greater than 40