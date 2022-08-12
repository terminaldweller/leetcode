#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None:
            return None

        cur = root

        while cur:
            if cur.val > p.val and cur.val > q.val:
                cur = cur.left
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            else:
                return cur


def main():
    node11 = TreeNode(6)
    node12 = TreeNode(2)
    node13 = TreeNode(8)
    node14 = TreeNode(0)
    node15 = TreeNode(4)
    node16 = TreeNode(7)
    node17 = TreeNode(9)
    node18 = TreeNode(3)
    node19 = TreeNode(5)

    node11.left = node12
    node11.right = node13
    node12.left = node14
    node12.right = node15
    node13.left = node16
    node13.right = node17
    node15.left = node18
    node15.right = node19

    solution = Solution()
    print(solution.lowestCommonAncestor(node11, node12, node15).val)
    print(solution.lowestCommonAncestor(node11, node17, node19).val)
    print(solution.lowestCommonAncestor(node11, node19, node17).val)
    print(solution.lowestCommonAncestor(node11, node19, node14).val)


if __name__ == "__main__":
    main()
