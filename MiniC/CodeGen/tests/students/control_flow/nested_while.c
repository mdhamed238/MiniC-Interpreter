#include "printlib.h"

int main() {
  int i, MAX, curr, j, sum;

  i = 0;
  j = 3;
  MAX = 7;
  sum = 0;

  while (i < MAX) {
    curr = 0;
    while (curr < j) {
      curr = curr + 1;
    }
    sum = sum + curr;
    i = i + 1;
  }
  
  println_int(sum);
  
  return 0;
}

// EXPECTED
// 21
