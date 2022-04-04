#include "header.hpp"

class Solution {
public:
  static std::vector<std::string> fizzBuzz(int n) {
    std::vector<std::string> result;
    result.reserve(n);

    for (int i = 1; i <= n; ++i) {
      if (0 == i % 3) {
        if (0 == i % 5) [[unlikely]] {
          result.push_back("FizzBuzz");
        } else {
          result.push_back("Fizz");
        }
      } else if (0 == i % 5) {
        result.push_back("Buzz");
      } else [[likely]] {
        result.push_back(std::to_string(i));
      }
    }

    return result;
  }
};

int main(int argc, char **argv) {
  auto result = Solution::fizzBuzz(15);
  for (auto &iter : result) {
    std::cout << iter << ", ";
  }
  std::cout << "\n";
  return 0;
}
