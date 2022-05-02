#include "header.hpp"

class Solution {
public:
  static std::vector<int> sortArrayByParity(std::vector<int> &nums) {
    std::vector<int> result;
    int front = 0;
    int end = nums.size() - 1;
    result.resize(nums.size());
    for (auto &iter : nums) {
      if (iter % 2 == 0) {
        result[front] = iter;
        front++;
      } else {
        result[end] = iter;
        end--;
      }
    }
    for (int i = 0; i < result.size(); ++i) {
      std::cout << result[i] << "\n";
    }
    return result;
  }
};

int main(int argc, char **argv) {
  std::vector<int> nums = {3, 1, 2, 4};
  std::vector<int> nums2 = {0};
  auto result = Solution::sortArrayByParity(nums);
  auto result2 = Solution::sortArrayByParity(nums2);

  for (auto &iter : result) {
    std::cout << iter << "\n";
  }
  return 0;
}
