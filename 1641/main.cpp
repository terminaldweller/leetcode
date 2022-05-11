#include "header.hpp"

class Solution {
public:
  static int countVowelStrings(int n) {
    std::vector<unsigned int> count = {1, 1, 1, 1, 1};
    while (--n > 0) {
      count[1] += count[0];
      count[2] += count[1];
      count[3] += count[2];
      count[4] += count[3];
    }

    return count[0] + count[1] + count[2] + count[3] + count[4];
  }
};

int main(int argc, char **argv) {
  std::cout << Solution::countVowelStrings(1) << std::endl;
  std::cout << Solution::countVowelStrings(2) << std::endl;
  std::cout << Solution::countVowelStrings(33) << std::endl;
  return 0;
}
