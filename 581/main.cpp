
#include "header.hpp"
#include <algorithm>

class Solution {
public:
  static int findUnsortedSubarray(std::vector<int> &nums) {
    std::vector<int> nums_copy;
    nums_copy.resize(nums.size());
    std::copy(nums.begin(), nums.end(), nums_copy.begin());
    std::sort(nums_copy.begin(), nums_copy.end());
    int l = 0;
    int n = nums.size() - 1;
    bool begin = 0;
    bool end = 0;
    while (n > l) {
      if (nums_copy[l] == nums[l]) {
        l++;
      } else {
        begin = true;
        break;
      }
    }
    while (n > l) {
      if (nums_copy[n] == nums[n]) {
        n--;
      } else {
        end = true;
        break;
      }
    }
    if (end || begin)
      return n - l + 1;
    else
      return 0;
  }
};

int main(int argc, char **argv) {
  std::vector<int> nums1 = {2, 6, 4, 8, 10, 9, 15};
  std::vector<int> nums2 = {1, 2, 3, 4};
  std::cout << Solution::findUnsortedSubarray(nums1) << std::endl;
  std::cout << Solution::findUnsortedSubarray(nums2) << std::endl;
  return 0;
}
