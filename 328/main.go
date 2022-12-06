package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func dumpList(head *ListNode) {
	for head.Next != nil {
		fmt.Println(head.Val)
		head = head.Next
	}
	fmt.Println(head.Val)
	fmt.Println()
}

func oddEvenList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	odd, even := head, head.Next
	evenHead := even
	for even != nil && even.Next != nil {
		odd.Next = even.Next
		odd = odd.Next
		even.Next = odd.Next
		even = even.Next
	}
	odd.Next = evenHead
	return head
}

func main() {
	node1 := &ListNode{1, nil}
	node2 := &ListNode{2, nil}
	node3 := &ListNode{3, nil}
	node4 := &ListNode{4, nil}
	node5 := &ListNode{5, nil}
	node1.Next = node2
	node2.Next = node3
	node3.Next = node4
	node4.Next = node5
	head := node1
	head = oddEvenList(node1)
	for head.Next != nil {
		fmt.Println(head.Val)
		head = head.Next
	}
	fmt.Println(head.Val)
}
