#!/usr/bin/env python3
# not mine

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """dog-slow"""

        def isValid(root, node_min, node_max):
            if root is None:
                return True

            if node_min is not None and root.val <= node_min:
                return False
            if node_max is not None and root.val >= node_max:
                return False

            return isValid(root.left, node_min, root.val) and isValid(
                root.right, root.val, node_max
            )

        return isValid(root, None, None)


def main():
    node11 = TreeNode(2)
    node12 = TreeNode(1)
    node13 = TreeNode(3)
    node11.left = node12
    node11.right = node13

    node21 = TreeNode(5)
    node22 = TreeNode(1)
    node23 = TreeNode(4)
    node24 = TreeNode(3)
    node25 = TreeNode(6)
    node21.left = node22
    node21.right = node23
    node23.left = node24
    node23.right = node25

    node31 = TreeNode(5)
    node32 = TreeNode(4)
    node33 = TreeNode(6)
    node34 = TreeNode(3)
    node35 = TreeNode(7)
    node31.left = node32
    node31.right = node33
    node33.left = node34
    node33.right = node35

    solution = Solution()
    print(solution.isValidBST(node11))
    print(solution.isValidBST(node21))
    print(solution.isValidBST(node31))


if __name__ == "__main__":
    main()
