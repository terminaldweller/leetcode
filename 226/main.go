package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func invertTree(root *TreeNode) *TreeNode {
	var invert func(root *TreeNode)
	invert = func(root *TreeNode) {
		if root == nil {
			return
		}

		root.Left, root.Right = root.Right, root.Left
		invert(root.Left)
		invert(root.Right)
	}
	invert(root)

	return root
}

// func invertTree(root *TreeNode) *TreeNode {
// 	if root == nil {
// 		return nil
// 	}

// 	right := invertTree(root.Right)
// 	left := invertTree(root.Left)
// 	root.Left = right
// 	root.Right = left

// 	return root
// }

func main() {
	fmt.Println("vim-go")
}
