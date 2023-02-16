package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	ldepth := maxDepth(root.Left)
	rdepth := maxDepth(root.Right)

	return max(ldepth, rdepth) + 1
}

func main() {
	fmt.Println("vim-go")
}
