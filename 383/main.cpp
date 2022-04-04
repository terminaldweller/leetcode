
#include "header.hpp"
#include <unordered_map>

class Solution {
public:
  static bool canConstruct(std::string ransomNote, std::string magazine) {
    bool result;

    for (auto &iter : ransomNote) {
      std::cout << iter;
      auto pos = magazine.find(iter);
      if (pos == std::string::npos) {
        return false;
      } else {
        magazine[pos] = '\n';
      }
      std::cout << magazine << "\n";
    }

    return true;
  }
};

int main(int argc, char **argv) { Solution::canConstruct("maga", "magazine"); }
