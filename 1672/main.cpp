#include "header.hpp"
#include <algorithm>

class Solution {
public:
  static int maximumWealth(std::vector<std::vector<int>> &accounts) {
    int i_max = 0;
    int sum_max = 0;
    int sum_cur = 0;
    for (int i = 0; i < accounts.size(); ++i) {
      for (int j = 0; j < accounts[i].size(); ++j) {
        sum_cur += accounts[i][j];
      }
      if (sum_cur > sum_max) {
        sum_max = sum_cur;
        i_max = i;
      }
      sum_cur = 0;
    }
    return sum_max;
  }
};

int main(int argc, char **argv) {
  std::vector<std::vector<int>> accounts = {{1, 2, 3}, {3, 2, 1}};
  std::cout << Solution::maximumWealth(accounts);
  return 0;
}
