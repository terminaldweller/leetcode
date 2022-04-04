
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
  static ListNode *middleNode(ListNode *head) {
    std::vector<ListNode *> heads;
    if (nullptr == head->next)
      return head;
    while (nullptr != head->next) {
      heads.push_back(head);
      head = head->next;
    }
    heads.push_back(head);

    int size = heads.size();
    std::cout << "size:" << size << "\n";
    return heads[int(size / 2)];
  }
};

int main(int argc, char **argv) {
  ListNode *l1 = new ListNode;
  ListNode *l2 = new ListNode;
  ListNode *l3 = new ListNode;
  ListNode *l4 = new ListNode;
  ListNode *l5 = new ListNode;
  ListNode *l6 = new ListNode;
  l1->val = 1;
  l2->val = 2;
  l3->val = 3;
  l4->val = 4;
  l5->val = 5;
  l6->val = 6;
  l1->next = l2;
  l2->next = l3;
  l3->next = l4;
  l4->next = l5;
  l5->next = l6;
  l6->next = nullptr;
  ListNode *head;
  head = Solution::middleNode(l1);
  while (head->next != nullptr) {
    std::cout << head->val << ",";
    head = head->next;
  }
  std::cout << std::endl;
  delete l1;
  delete l2;
  delete l3;
  delete l4;
  delete l5;
  delete l6;
}
