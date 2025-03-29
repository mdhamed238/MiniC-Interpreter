#include "printlib.h"

int main(){
  int x;
  
  x = 10;
  
  if (x > 5) {
    if (x < 15) {
      println_string("X is between 5 and 15");
    } else {
      println_string("X is greater than or equal to 15");
    }
  } else {
    println_string("X is less than or equal to 5");
  }
  
  return 0;
}


// SKIP TEST EXPECTED
// EXPECTED
// X is between 5 and 15