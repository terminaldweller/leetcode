#!/usr/bin/env python3
# not mine

from typing import List


class Solution:
    def __init__(self):
        self.memo = {}
        self.num_list = {}

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        modulo: int = 10**9 + 7
        N: int = len(arr)
        arr.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(arr)}

        for i, x in enumerate(arr):
            for j in range(i):
                if x % arr[j] == 0:
                    right = x / arr[j]
                    if right in index:
                        dp[i] += dp[j] * dp[int(index[int(right)])]
                        dp[i] %= modulo

        return sum(dp) % modulo


def main():
    solution = Solution()
    assert solution.numFactoredBinaryTrees([2, 4]), 3
    assert solution.numFactoredBinaryTrees([2, 4, 5, 10]), 7


if __name__ == "__main__":
    main()
