#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def findErrorNums(self, nums):
        counts = {}
        one = 0
        for num in nums:
            if num in counts:
                counts[num] += 1
                one = num
            else:
                counts[num] = 1

        total = len(nums) * (len(nums) + 1) // 2

        return [one, total - sum(nums) + one]


def main():
    solution = Solution()
    print(solution.findErrorNums([1, 2, 2, 4]))
    print(solution.findErrorNums([1, 1]))


if __name__ == "__main__":
    main()
