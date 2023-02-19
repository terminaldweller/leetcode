#!/usr/bin/env python

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = [root]
        left_to_right = True

        while q:
            level_size = len(q)
            level = []

            for i in range(level_size):
                node = q.pop(0)

                if left_to_right:
                    level.append(node.val)
                else:
                    level = [node.val] + level

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
            left_to_right = not left_to_right
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.zigzagLevelOrder())
