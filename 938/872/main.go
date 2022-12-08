package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func preorderVisit(node *TreeNode, leafSequence *[]int) {
	if node == nil {
		return
	}
	if node.Left == nil && node.Right == nil {
		*leafSequence = append(*leafSequence, node.Val)
		return
	}

	preorderVisit(node.Left, leafSequence)
	preorderVisit(node.Right, leafSequence)
}

func leafSimilar(root1, root2 *TreeNode) bool {
	var leafSequence1 []int
	var leafSequence2 []int

	preorderVisit(root1, &leafSequence1)
	preorderVisit(root2, &leafSequence2)

	// for i := 0; i < len(leafSequence1); i++ {
	// 	fmt.Println((leafSequence1)[i])
	// }
	// for i := 0; i < len(leafSequence2); i++ {
	// 	fmt.Println((leafSequence2)[i])
	// }

	if len(leafSequence1) != len(leafSequence2) {
		return false
	}

	for i := 0; i < len(leafSequence1); i++ {
		if (leafSequence1)[i] != (leafSequence2)[i] {
			return false
		}
	}

	return true
}

func main() {
	var node1 TreeNode
	var node2 TreeNode
	var node3 TreeNode
	node1.Val = 1
	node2.Val = 2
	node3.Val = 3

	node1.Left = &node2
	node1.Right = &node3

	var node4 TreeNode
	var node5 TreeNode
	var node6 TreeNode
	node4.Val = 1
	node5.Val = 2
	node6.Val = 3

	node4.Left = &node6
	node4.Right = &node5

	fmt.Println(leafSimilar(&node1, &node4))

}
