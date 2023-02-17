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

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func walk(node *TreeNode, vals *[]int) {
	if node == nil {
		return
	}

	walk(node.Left, vals)
	*vals = append(*vals, node.Val)
	walk(node.Right, vals)
}

func minDiffInBST(root *TreeNode) int {
	var vals []int

	walk(root, &vals)

	minDist := math.MaxInt32

	for i := 1; i < len(vals); i++ {
		minDist = min(minDist, vals[i]-vals[i-1])
	}

	return minDist
}

func main() {
	fmt.Println("vim-go")
}
