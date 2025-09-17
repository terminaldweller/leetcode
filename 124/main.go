package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

func walk(node *TreeNode, sum *int) int {
	if node == nil {
		return 0
	}

	left := max(0, walk(node.Left, sum))
	right := max(0, walk(node.Right, sum))
	fmt.Println(left, right, sum)
	*sum = max(*sum, left+right+node.Val)

	return max(left, right) + node.Val
}

func maxPathSum(root *TreeNode) int {
	sum := math.MinInt

	walk(root, &sum)

	return sum
}

func main() {
	fmt.Println("vim-go")
}
