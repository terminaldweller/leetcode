
#include "header.hpp"
#include <functional>
#include <queue>

class KthLargest {
public:
  KthLargest(int k, std::vector<int> &nums) {
    this->k = k;
    for (auto &iter : nums) {
      pq.push(iter);
    }

    while (pq.size() > k) {
      pq.pop();
    }
  }

  int add(int val) {
    pq.push(val);
    if (pq.size() > k) {
      pq.pop();
    }
    return pq.top();
  }

private:
  std::priority_queue<int, std::vector<int>, std::greater<int>> pq;
  int k;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */

int main(int argc, char **argv) { return 0; }
