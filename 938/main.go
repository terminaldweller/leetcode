package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func preOrder(node *TreeNode, sum *int, low, high int) {
	if node == nil {
		return
	}

	if node.Val >= low && node.Val <= high {
		*sum += node.Val
	}

	preOrder(node.Left, sum, low, high)
	preOrder(node.Right, sum, low, high)
}

func rangeSumBST(root *TreeNode, low int, high int) int {
	sum := 0

	preOrder(root, &sum, low, high)

	return sum
}

func main() {
	fmt.Println("vim-go")
}
