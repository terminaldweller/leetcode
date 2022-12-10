package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func max(a, b int64) int64 {
	if a > b {
		return int64(a)
	} else {
		return int64(b)
	}
}

func maxProduct(root *TreeNode) int {
	var total int64
	var result int64

	var sumUnder func(*TreeNode) int64
	sumUnder = func(node *TreeNode) int64 {
		var sum int64
		if node == nil {
			return 0
		}

		sum = sumUnder(node.Left) + sumUnder(node.Right) + int64(node.Val)
		result = max(int64(result), sum*(total-sum))

		return sum
	}

	total = sumUnder(root)
	sumUnder(root)

	return int(result % (1_000_000_000 + 7))
}

func main() {
	fmt.Println("vim-go")
}
