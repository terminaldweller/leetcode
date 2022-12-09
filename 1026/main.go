package main

import (
	"fmt"
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

func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func abs(a int) int {
	if a < 0 {
		return -a
	} else {
		return a
	}
}

func maxAncestorDiff(root *TreeNode) int {
	result := -(1 << 30)

	var walkTree func(*TreeNode, int, int)
	walkTree = func(node *TreeNode, mav, miv int) {
		if node == nil {
			return
		}

		if node != root {
			result = max(result, max(abs(miv-node.Val), abs(mav-node.Val)))
		}

		walkTree(node.Left, max(mav, node.Val), min(miv, node.Val))
		walkTree(node.Right, max(mav, node.Val), min(miv, node.Val))
	}
	walkTree(root, result, -result)

	return result
}

func main() {
	fmt.Println("vim-go")
}
