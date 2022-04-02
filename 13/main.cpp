
#include "header.hpp"
#include <map>

class Solution {
public:
  Solution() = default;
  static int romanToInt(std::string s) {
    std::map<unsigned char, int32_t> romanNumber = {
        {'I', 1},   {'V', 5},   {'X', 10},  {'L', 50},
        {'C', 100}, {'D', 500}, {'M', 1000}};
    int result = 0;
    int val = 0;
    unsigned char prev;

    for (int i = 0; i < s.length() - 1; ++i) {
      val = romanNumber[s[i]];
      if (romanNumber[s[i]] < romanNumber[s[i + 1]]) {
        result = result - val;
      } else {
        result = result + val;
      }
    }

    return result + romanNumber[s[s.length() - 1]];
  }
};

int main(int argc, char **argv) {
  std::string s;
  std::cin >> s;
  std::cout << Solution::romanToInt(s) << "\n";
  return 0;
}
