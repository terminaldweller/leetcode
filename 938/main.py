#!/usr/bin/env python


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    import typing

    def rangeSumBST(self, root: typing.Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        if root.val < low or root.val > high:
            return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(
                root.right, low, high
            )
        return (
            root.val
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )


def main() -> None:
    solution = Solution()
    print(solution.rangeSumBST())


if __name__ == "__main__":
    main()
