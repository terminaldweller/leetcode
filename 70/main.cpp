
#include "header.hpp"

class Solution {
public:
  int climbStairs(int n) { return this->lookup[n]; }
  /* static int climbStairs(int n) { */
  /*   if (n == 1) */
  /*     return 1; */
  /*   if (n == 2) */
  /*     return 2; */
  /*   int prev_1 = 2; */
  /*   int prev_2 = 1; */
  /*   int neu = 0; */
  /*   for (int i = 3; i <= n; ++i) { */
  /*     neu = prev_1 + prev_2; */
  /*     prev_2 = prev_1; */
  /*     prev_1 = neu; */
  /*   } */

  /*   return prev_1; */
  /* } */
  std::vector<int64_t> lookup = {
      0,         1,         2,          3,          5,          8,
      13,        21,        34,         55,         89,         144,
      233,       377,       610,        987,        1597,       2584,
      4181,      6765,      10946,      17711,      28657,      46368,
      75025,     121393,    196418,     317811,     514229,     832040,
      1346269,   2178309,   3524578,    5702887,    9227465,    14930352,
      24157817,  39088169,  63245986,   102334155,  165580141,  267914296,
      433494437, 701408733, 1134903170, 1836311903, 2971215073, 4807526976};

private:
};

int main(int argc, char **argv) {
  Solution *solution = new Solution;
  std::cout << solution->climbStairs(2) << "\n";
  std::cout << solution->climbStairs(3) << "\n";
  std::cout << solution->climbStairs(4) << "\n";
  std::cout << solution->climbStairs(5) << "\n";
  return 0;
}
