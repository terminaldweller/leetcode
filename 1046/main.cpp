
#include "header.hpp"
#include <algorithm>

class Solution {
public:
  static int lastStoneWeight(std::vector<int> &stones) {
    if (stones.size() == 1) {
      return stones[0];
    }
    std::sort(stones.begin(), stones.end());
    while (stones[stones.size() - 2] > 0) {
      stones[stones.size() - 2] =
          std::abs(stones[stones.size() - 1] - stones[stones.size() - 2]);
      stones[stones.size() - 1] = 0;
      std::sort(stones.begin(), stones.end());
      for (auto &iter : stones) {
        std::cout << iter << " " << std::endl;
      }
      std::cout << "\n";
    }
    return stones[stones.size() - 1];
  }
};

int main(int argc, char **argv) {
  std::vector<int> stones = {2, 7, 4, 1, 8, 1};
  std::cout << Solution::lastStoneWeight(stones);
  return 0;
}
