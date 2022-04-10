
#include "header.hpp"
#include <string>

class Solution {
public:
  static int calPoints(std::vector<std::string> &ops) {
    std::vector<int> result;
    result.reserve(1000);
    int sum = 0;
    for (auto &iter : ops) {
      if (iter == "+") {
        auto dummy = result[result.size() - 1] + result[result.size() - 2];
        result.push_back(dummy);
        sum += dummy;
      } else if (iter == "D") {
        auto dummy = result[result.size() - 1] * 2;
        result.push_back(dummy);
        sum += dummy;
      } else if (iter == "C") {
        sum -= result[result.size() - 1];
        result.pop_back();
      } else {
        auto dummy = std::stoi(iter);
        result.push_back(dummy);
        sum += dummy;
      }
    }

    return sum;
  }
};

int main(int argc, char **argv) {
  std::vector<std::string> ops1 = {"5", "2", "C", "D", "+"};
  std::vector<std::string> ops2 = {"5", "-2", "4", "C", "D", "9", "+", "+"};
  std::cout << Solution::calPoints(ops1) << "\n";
  std::cout << Solution::calPoints(ops2) << "\n";
  return 0;
}
