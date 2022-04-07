
#include "header.hpp"
#include <algorithm>

struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  static ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    int carry = 0;
    int sum = 0;
    ListNode *head = new ListNode;
    ListNode *result = head;
    bool l1_last = false;
    bool l2_last = false;
    while (l1->next != nullptr || l2->next != nullptr) {

      if (l1->next != nullptr) {
        sum += l1->val;
        l1 = l1->next;
      } else {
        if (!l1_last) {
          sum += l1->val;
          l1_last = true;
        }
      }

      if (l2->next != nullptr) {
        sum += l2->val;
        l2 = l2->next;
      } else {
        if (!l2_last) {
          sum += l2->val;
          l2_last = true;
        }
      }

      sum += carry;
      if (sum >= 10) {
        sum -= 10;
        carry = 1;
      } else {
        carry = 0;
      }
      head->val = sum;
      head->next = new ListNode;
      head = head->next;
      sum = 0;
    }

    sum = 0;
    if (l1 != nullptr && !l1_last) {
      sum += l1->val;
    }
    if (l2 != nullptr && !l2_last) {
      sum += l2->val;
    }
    sum += carry;
    if (sum >= 10) {
      sum -= 10;
      carry = 1;
    } else {
      carry = 0;
    }
    head->val = sum;
    if (carry != 0) {
      head->next = new ListNode;
      head = head->next;
      head->val = carry;
    }

    return result;
  }
};

int main(int argc, char **argv) {
  ListNode *l11 = new ListNode;
  ListNode *l12 = new ListNode;
  ListNode *l13 = new ListNode;
  ListNode *l14 = new ListNode;
  ListNode *l15 = new ListNode;
  ListNode *l16 = new ListNode;
  ListNode *l17 = new ListNode;
  ListNode *l21 = new ListNode;
  ListNode *l22 = new ListNode;
  ListNode *l23 = new ListNode;
  ListNode *l24 = new ListNode;
  l11->val = 9;
  l12->val = 9;
  l13->val = 9;
  l14->val = 9;
  l15->val = 9;
  l16->val = 9;
  l17->val = 9;
  l21->val = 9;
  l22->val = 9;
  l23->val = 9;
  l24->val = 9;
  l11->next = l12;
  l12->next = l13;
  l13->next = l14;
  l14->next = l15;
  l15->next = l16;
  l16->next = l17;
  l17->next = nullptr;
  l21->next = l22;
  l22->next = l23;
  l23->next = l24;
  l24->next = nullptr;

  auto result = Solution::addTwoNumbers(l11, l21);
  while (result->next != nullptr) {
    std::cout << result->val;
    result = result->next;
  }
  std::cout << result->val << "\n";

  return 0;
}
