
#include "header.hpp"
#include <unordered_map>

class Solution {
public:
  static int maxOperations(std::vector<int> &nums, int k) {
    int result = 0;
    std::unordered_map<int, int> dict;
    for (auto &iter : nums) {
      if (dict.find(iter) != dict.end()) {
        dict[iter]++;
      } else {
        dict.insert(std::make_pair(iter, 1));
      }
    }
    for (auto &iter : dict) {
      if (k > iter.first) {
        if (dict.find(k - iter.first) != dict.end()) {
          if (k - iter.first == iter.first) {
            result = result + int(iter.second / 2);
          } else {
            auto dec = std::min(dict[iter.first], dict[k - iter.first]);
            result = result + dec;
            dict[iter.first] -= dec;
            dict[k - iter.first] -= dec;
          }
        }
      }
    }
    return result;
  }
};

int main(int argc, char **argv) {
  std::vector<int> num1 = {1, 2, 3, 4};
  std::vector<int> num2 = {3, 1, 3, 4, 3};
  std::vector<int> num3 = {2, 2, 2, 3, 1, 1, 4, 1};
  std::vector<int> num4 = {3, 5, 1, 5};
  std::vector<int> num5 = {2, 5, 4, 4, 1, 3, 4, 4, 1, 4,
                           4, 1, 2, 1, 2, 2, 3, 2, 4, 2};

  std::cout << Solution::maxOperations(num1, 5) << std::endl; // 2
  std::cout << Solution::maxOperations(num2, 6) << std::endl; // 1
  std::cout << Solution::maxOperations(num3, 4) << std::endl; // 2
  std::cout << Solution::maxOperations(num4, 2) << std::endl; // 0
  std::cout << Solution::maxOperations(num5, 3) << std::endl; // 4

  return 0;
}
