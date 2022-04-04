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
  static ListNode *swapNodes(ListNode *head, int k) {
    auto iter = head;
    int counter = 1;
    std::vector<ListNode *> dummy;
    while (iter->next != nullptr) {
      dummy.push_back(iter);
      iter = iter->next;
      counter++;
    }
    dummy.push_back(iter);

    std::cout << "counter: " << counter << "\n";

    std::swap(static_cast<ListNode *>(dummy[k - 1])->val,
              static_cast<ListNode *>(dummy[counter - k])->val);

    return head;
  }
};

int main(int argc, char **argv) {
  ListNode *l1 = new ListNode;
  ListNode *l2 = new ListNode;
  ListNode *l3 = new ListNode;
  ListNode *l4 = new ListNode;
  ListNode *l5 = new ListNode;
  l1->val = 1;
  l2->val = 2;
  l3->val = 3;
  l4->val = 4;
  l5->val = 5;
  l1->next = l2;
  l2->next = l3;
  l3->next = l4;
  l4->next = l5;
  l5->next = nullptr;

  auto head = Solution::swapNodes(l1, 2);

  while (head->next != nullptr) {
    std::cout << head->val << ",";
    head = head->next;
  }
  std::cout << "\n";
}
