
#include "header.hpp"
#include <unordered_map>
#include <utility>

class Solution {
public:
  static int lengthOfLongestSubstring(std::string s) {
    std::unordered_map<char, bool> dict;
    int max = 0;
    int cur = 0;
    int begin = 0;
    for (int i = 0; i < s.length(); ++i) {
      if (dict.find(s[i]) == dict.end()) {
        dict.emplace(std::make_pair(s[i], true));
        cur++;
      } else {
        auto culprit = s.rfind(s[i], i - 1);
        if (culprit < begin) {
          cur++;
          continue;
        }
        if (cur >= max) {
          max = cur;
        }
        cur = i - culprit;
        begin = culprit + 1;
        /* std::cout << s[culprit] << "\n"; */
      }
    }

    /* std::cout << max << ":" << cur << "\n"; */
    return std::max(max, cur);
  }
};

int main(int argc, char **argv) {
  std::cout << Solution::lengthOfLongestSubstring("abcabcbb") << "\n";
  std::cout << Solution::lengthOfLongestSubstring("bbbbb") << "\n";
  std::cout << Solution::lengthOfLongestSubstring("pwwkew") << "\n";
  std::cout << Solution::lengthOfLongestSubstring(" ") << "\n";
  std::cout << Solution::lengthOfLongestSubstring("au") << "\n";
  std::cout << Solution::lengthOfLongestSubstring("aab") << "\n";
  std::cout << Solution::lengthOfLongestSubstring("dvdf") << "\n";
  std::cout << Solution::lengthOfLongestSubstring("tmmzuxt") << "\n";
  return 0;
}
