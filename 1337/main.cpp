#include "header.hpp"

class Solution {
public:
  std::vector<int> kWeakestRows(std::vector<std::vector<int>> &mat, int k) {
    std::pair<std::vector<int>, std::vector<int>> sums;
    sums.first.reserve(mat.size());
    sums.second.reserve(mat.size());
    int row = 0;
    int sum = 0;

    for (auto &iter : mat) {
      for (auto &ya_iter : iter) {
        sum += ya_iter;
        if (0 == ya_iter) {
          break;
        }
      }
      sums.first[row] = row;
      sums.second[row] = sum;
      row++;
      sum = 0;
    }

    for (int i = 0; i < row - 1; ++i) {
      for (int j = 0; j < row - 1; ++j) {
        if (sums.second[j] > sums.second[j + 1]) {
          std::swap(sums.first[j], sums.first[j + 1]);
          std::swap(sums.second[j], sums.second[j + 1]);
        }
      }
    }

    /* for (int i = 0; i < row; ++i) { */
    /*   std::cout << sums.first[i] << ":" << sums.second[i] << "\n"; */
    /* } */

    std::vector<int> result(k);
    std::copy(sums.first.begin(), sums.first.begin() + k, result.begin());
    return result;
  }
};

int main(int argc, char **argv) {
  Solution solution;
  std::vector<std::vector<int>> mat = {{1, 1, 0, 0, 0},
                                       {1, 1, 1, 1, 0},
                                       {1, 0, 0, 0, 0},
                                       {1, 1, 0, 0, 0},
                                       {1, 1, 1, 1, 1}};
  auto result = solution.kWeakestRows(mat, 3);
  for (int i = 0; i < 3; ++i) {
    std::cout << result[i] << "\n";
  }
  return 0;
}
