package main

import (
	"fmt"

	"github.com/emirpasic/gods/stacks/arraystack"
)

type MyQueue struct {
	s1 *arraystack.Stack
	s2 *arraystack.Stack
}

func Constructor() MyQueue {
	s1 := arraystack.New()
	s2 := arraystack.New()

	q := MyQueue{s1: s1, s2: s2}

	return q
}

func (this *MyQueue) Push(x int) {
	this.s1.Push(x)
}

func (this *MyQueue) Pop() int {
	for {
		if val, ok := this.s1.Pop(); ok {
			this.s2.Push(val)
		} else {
			break
		}
	}

	val, _ := this.s2.Pop()

	for {
		if val, ok := this.s2.Pop(); ok {
			this.s1.Push(val)
		} else {
			break
		}
	}

	return val.(int)
}

func (this *MyQueue) Peek() int {
	for {
		if val, ok := this.s1.Pop(); ok {
			this.s2.Push(val)
		} else {
			break
		}
	}

	val, _ := this.s2.Pop()
	this.s2.Push(val)

	for {
		if val, ok := this.s2.Pop(); ok {
			this.s1.Push(val)
		} else {
			break
		}
	}

	return val.(int)

}

func (this *MyQueue) Empty() bool {
	return this.s1.Empty()
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Peek();
 * param_4 := obj.Empty();
 */

func main() {
	obj := Constructor()
	obj.Push(1)
	obj.Push(2)
	fmt.Println(obj.Peek())
	fmt.Println(obj.Pop())
	fmt.Println(obj.Empty())
}
