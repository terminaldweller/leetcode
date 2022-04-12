
#include "header.hpp"

class Solution {
public:
  void gameOfLife(std::vector<std::vector<int>> &board) {
    std::vector<std::vector<int>> shadow;
    shadow.resize(board.size());
    /* std::cout << board.size() << "\n"; */
    /* std::cout << board[0].size() << "\n"; */
    auto M = board.size();
    auto N = board[0].size();
    for (auto &iter : shadow) {
      iter.resize(N);
    }
    int pop = 0;
    for (int i = 0; i < M; ++i) {
      for (int j = 0; j < N; ++j) {
        std::cout << "(i,j):" << i << "," << j << "\t";
        // Neighbour
        if (i >= 1) {
          pop += board[i - 1][j];
          if (j >= 1)
            pop += board[i - 1][j - 1];
          if (j < N - 1)
            pop += board[i - 1][j + 1];
        }
        if (i < M - 1) {
          pop += board[i + 1][j];
          if (j >= 1)
            pop += board[i + 1][j - 1];
          if (j < N - 1)
            pop += board[i + 1][j + 1];
        }
        if (j < N - 1) {
          pop += board[i][j + 1];
        }
        if (j >= 1) {
          pop += board[i][j - 1];
        }
        std::cout << "pop: " << pop << "\n";
        /* std::cout << shadow[0][0] << "\n"; */
        /* std::cout << shadow[3][2] << "\n"; */
        /* std::cout << "fuck\n"; */

        // Decision
        if (board[i][j] == 0) {
          if (pop == 3)
            shadow[i][j] = 1;
          else
            shadow[i][j] = 0;
        } else {
          if (pop == 2 || pop == 3)
            shadow[i][j] = 1;
          else
            shadow[i][j] = 0;
        }
        pop = 0;
      }
    }
    /* std::cout << "fuck\n"; */

    for (int i = 0; i < board.size(); ++i) {
      for (int j = 0; j < board[0].size(); ++j) {
        board[i][j] = shadow[i][j];
      }
    }
  }
};

int main(int argc, char **argv) {
  std::vector<std::vector<int>> b1 = {
      {0, 1, 0}, {0, 0, 1}, {1, 1, 1}, {0, 0, 0}};
  std::vector<std::vector<int>> b2 = {{1, 1}, {1, 0}};

  Solution solution;
  solution.gameOfLife(b1);
  solution.gameOfLife(b2);

  return 0;
}
