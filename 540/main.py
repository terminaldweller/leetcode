#!/usr/bin/env python
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        mid = 0

        if len(nums) == 1:
            return nums[0]

        while start < end:
            mid = (start + end) // 2
            if nums[mid] == nums[mid + 1]:
                if (end - mid + 1) % 2 == 0:
                    end = mid - 1
                else:
                    start = mid
            elif nums[mid] == nums[mid - 1]:
                if (mid - start + 1) % 2 == 0:
                    start = mid + 1
                else:
                    end = mid
            else:
                return nums[mid]

        return nums[end]


if __name__ == "__main__":
    solution = Solution()
    assert solution.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2
    assert solution.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10
    assert solution.singleNonDuplicate([1, 2, 2, 3, 3, 4, 4, 8, 8]) == 1
    assert solution.singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 4, 8]) == 8
    assert solution.singleNonDuplicate([1, 1, 2]) == 2
    assert solution.singleNonDuplicate([0, 1, 1, 2, 2, 5, 5]) == 0
