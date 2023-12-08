#!/usr/bin/env python

import typing


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: typing.Optional[TreeNode]) -> str:
        if not root:
            return ""
        if not root.left and not root.right:
            return str(root.val)
        if not root.right:
            return str(root.val) + "(" + self.tree2str(root.left) + ")"
        return (
            str(root.val)
            + "("
            + self.tree2str(root.left)
            + ")("
            + self.tree2str(root.right)
            + ")"
        )


def main():
    solution = Solution()
    print(solution.tree2str())


if __name__ == "__main__":
    main()
