
#include "header.hpp"

class Solution {
public:
  static int numberOfSteps(int num) {
    auto dummy = num;
    int counter = 0;
    while (dummy != 0) {
      if (dummy % 2 == 0) {
        dummy = dummy >> 1;
      } else {
        dummy--;
      }
      counter++;
    }
    return counter;
  }
};

int main(int argc, char **argv) { std::cout << Solution::numberOfSteps(123); }
