#!/usr/bin/env python
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1
        mid = 0
        while begin <= end:
            mid = (end + begin) // 2
            if target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                begin = mid + 1
            else:
                return mid
        return begin


if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert([1, 3, 5, 6], 5))
    print(solution.searchInsert([1, 3, 5, 6], 2))
    print(solution.searchInsert([1, 3, 5, 6], 7))
