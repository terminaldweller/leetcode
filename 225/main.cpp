#include "header.hpp"
#include <queue>

class MyStack {
public:
  MyStack() = default;

  void push(int x) { q1.push(x); }

  int pop() {
    while (q1.size() > 1) {
      q2.push(q1.front());
      q1.pop();
    }
    auto result = q1.back();
    q1.pop();
    while (q2.size() > 0) {
      q1.push(q2.front());
      q2.pop();
    }
    return result;
  }

  int top() { return q1.back(); }

  bool empty() { return q1.empty(); }

private:
  std::queue<int> q1;
  std::queue<int> q2;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */

int main(int argc, char **argv) {
  MyStack *obj = new MyStack();
  obj->push(10);
  int param_2 = obj->pop();
  int param_3 = obj->top();
  bool param_4 = obj->empty();
  return 0;
}
