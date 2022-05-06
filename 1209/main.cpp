
#include "header.hpp"
#include <algorithm>
#include <stack>

class Solution {
public:
  static std::string removeDuplicates(std::string s, int k) {
    std::stack<std::pair<unsigned char, int>> dict;
    std::string result = "";

    for (auto &iter : s) {
      if (dict.empty()) {
        dict.push(std::make_pair(iter, 1));
        continue;
      }
      if (dict.top().first == iter) {
        dict.top().second++;
      } else {
        dict.push(std::make_pair(iter, 1));
      }
      if (dict.top().second == k) {
        dict.pop();
      }
    }

    while (dict.size() > 0) {
      result += dict.top().first;
      if (dict.top().second == 1)
        dict.pop();
      else
        dict.top().second--;
    }
    std::reverse(result.begin(), result.end());
    return result;
  }
};

int main(int argc, char **argv) {
  std::cout << Solution::removeDuplicates("abcd", 2) << std::endl;
  std::cout << Solution::removeDuplicates("deeedbbcccbdaa", 3) << std::endl;
  std::cout << Solution::removeDuplicates("pbbcggttciiippooaais", 2)
            << std::endl;
  return 0;
}
