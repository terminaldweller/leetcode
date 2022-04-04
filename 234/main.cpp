#include "header.hpp"

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  Solution() = default;
  bool isPalindrome(ListNode *head) {
    auto iter = head;
    std::vector<int> pal;

    while (iter->next != nullptr) {
      pal.push_back(iter->val);
      iter = iter->next;
    }
    pal.push_back(iter->val);
    for (int i = pal.size(); i >= 0; i--) {
      if (head->val != pal[i]) {
        return false;
      }
      head = head->next;
    }
    return true;
  }
};

int main(int argc, char **argv) { return 0; }
