#!/usr/bin/env python3
# https://yellowcoding.com/leetcode-108-convert-sorted-array-to-binary-search-tree/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def fun(nums: List[int], low: int, high: int):
            if low > high:
                return None

            mid: int = int((low + high) / 2)
            node = TreeNode(val=nums[mid])
            node.left = fun(nums, low, mid - 1)
            node.right = fun(nums, mid + 1, high)
            return node

        return fun(nums, 0, len(nums) - 1)


def main():
    solution = Solution()
    print(solution.sortedArrayToBST([-10, -3, 0, 5, 9]))
    print(solution.sortedArrayToBST([1, 3]))


if __name__ == "__main__":
    main()
