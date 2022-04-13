#include "header.hpp"

class Solution {
public:
  static int floorMod(int x, int y) { return ((x % y) + y) % y; }

  static std::vector<std::vector<int>> generateMatrix(int n) {
    std::vector<std::vector<int>> result(n, std::vector<int>(n));
    int cnt = 1;
    int dir[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    int d = 0;
    int row = 0;
    int col = 0;
    while (cnt <= n * n) {
      result[row][col] = cnt++;
      int r = floorMod(row + dir[d][0], n);
      int c = floorMod(col + dir[d][1], n);

      if (result[r][c] != 0)
        d = (d + 1) % 4;
      row += dir[d][0];
      col += dir[d][1];
    }
    return result;
  }
};

void pprint(std::vector<std::vector<int>> matrix) {
  for (auto &iter : matrix) {
    for (auto &ya_iter : iter) {
      std::cout << ya_iter << " ";
    }
    std::cout << "\n";
  }
}

int main(int argc, char **argv) {
  pprint(Solution::generateMatrix(3));
  pprint(Solution::generateMatrix(4));
  pprint(Solution::generateMatrix(5));
  pprint(Solution::generateMatrix(33));
  return 0;
}
