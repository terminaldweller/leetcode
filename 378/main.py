#!/usr/bin/env python3
# https://leetcode.com/problems/k-th-smallest-prime-fraction/discuss/115819/Summary-of-solutions-for-problems-%22reducible%22-to-LeetCode-378

from typing import List
import math


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n: int = len(matrix)
        l: int = matrix[0][0]
        r: int = matrix[n - 1][n - 1]

        cnt: int = 0
        m: int = 0
        while l < r:
            cnt = 0
            if (l + (r - l) / 2) < 0:
                m = math.floor(l + ((r - l) / 2))
            else:
                m = math.floor(l + ((r - l) / 2))

            for i in range(0, n):
                j: int = n - 1
                while j >= 0 and matrix[i][j] > m:
                    j -= 1
                cnt += j + 1

            print(cnt, m)
            if cnt < k:
                l = m + 1
            else:
                r = m

        return l


def main():
    solution = Solution()
    print(solution.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
    print(solution.kthSmallest([[-5]], 1))
    print(solution.kthSmallest([[1, 2], [1, 3]], 2))
    print(solution.kthSmallest([[1, 2], [1, 3]], 3))
    print(solution.kthSmallest([[-5, -4], [-5, -4]], 1))


if __name__ == "__main__":
    main()
