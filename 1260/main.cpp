#include "header.hpp"
#include <cmath>

class Solution {
public:
  static std::vector<std::vector<int>>
  shiftGrid(std::vector<std::vector<int>> &grid, int k) {
    if (k == 0) {
      return grid;
    }

    auto row_count = grid.size();
    auto col_count = grid[0].size();
    std::vector<std::vector<int>> result;
    result.resize(row_count);
    for (auto &iter : result) {
      iter.resize(col_count);
    }

    /* if (k % grid.size() == 0) { */
    /*   for (auto &iter : grid) { */
    /*     std::copy(iter.begin(), iter.end(), */
    /*               result[((k % grid[0].size()) - 1) % grid.size()].begin());
     */
    /*   } */
    /* } */

    for (int i = 0; i < row_count; ++i) {
      for (int j = 0; j < col_count; ++j) {
        auto index = ((col_count * i + j + k)) % (col_count * row_count) + 1;
        auto new_row = std::ceil(static_cast<double>(index) /
                                 static_cast<double>(col_count));
        auto new_col = index - ((new_row - 1) * col_count);
        result[new_row - 1][new_col - 1] = grid[i][j];
        std::cout << "index:" << index << " new:" << new_row << "," << new_col
                  << "\n";
      }
    }
    return result;
  }
};

void pprint(std::vector<std::vector<int>> &&grid) {
  for (auto &iter : grid) {
    for (auto &ya_iter : iter) {
      std::cout << ya_iter << " ";
    }
    std::cout << "\n";
  }
  std::cout << "\n";
}

int main(int argc, char **argv) {
  std::vector<std::vector<int>> grid1 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
  std::vector<std::vector<int>> grid2 = {
      {3, 8, 1, 9}, {19, 7, 2, 5}, {4, 6, 11, 10}, {12, 0, 21, 13}};
  std::vector<std::vector<int>> grid3 = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};

  pprint(Solution::shiftGrid(grid1, 1));
  pprint(Solution::shiftGrid(grid2, 4));
  pprint(Solution::shiftGrid(grid3, 9));

  return 0;
}
