#!/usr/bin/env python3
# https://scribe.rip/codex/leetcode-300-longest-increasing-subsequence-b5eaba41e407


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = 1

        maximum: int = 1

        for i in range(0, len(dp)):
            dp[i] = 1
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1

            if dp[i] > maximum:
                maximum = dp[i]

        return maximum


def main():
    solution = Solution()
    print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(solution.lengthOfLIS([0, 1, 0, 3, 2, 3]))
    print(solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))


if __name__ == "__main__":
    main()
