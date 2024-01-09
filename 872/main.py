#!/usr/bin/env python
import typing


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverse(self, node: typing.Optional[TreeNode], leafSeq):
        if node is None:
            return

        if node.left is None and node.right is None:
            leafSeq.append(node.val)
            return

        self.traverse(node.left, leafSeq)
        self.traverse(node.right, leafSeq)

    def leafSimilar(
        self, root1: typing.Optional[TreeNode], root2: typing.Optional[TreeNode]
    ) -> bool:
        leafSeq1: typing.List[int] = []
        leafSeq2: typing.List[int] = []

        self.traverse(root1, leafSeq1)
        self.traverse(root2, leafSeq2)

        if len(leafSeq1) != len(leafSeq2):
            return False

        for e1, e2 in zip(leafSeq1, leafSeq2):
            if e1 != e2:
                return False

        return True


def main():
    solution = Solution()
    # print(solution.leafSimilar())


if __name__ == "__main__":
    main()
