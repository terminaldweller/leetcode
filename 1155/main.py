#!/usr/bin/env python


from functools import lru_cache


class Solution:
    @lru_cache(None)
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d == 1:
            if 0 < target <= f:
                return 1
            return 0
        if target < d or target > f * d:
            return 0
        res = 0
        for i in range(1, f + 1):
            res += self.numRollsToTarget(d - 1, f, target - i) % (10**9 + 7)
        return res % (10**9 + 7)


def main():
    solution = Solution()
    print(solution.numRollsToTarget(1, 6, 3))
    print(solution.numRollsToTarget(2, 6, 7))
    print(solution.numRollsToTarget(2, 5, 10))
    print(solution.numRollsToTarget(30, 30, 500))


if __name__ == "__main__":
    main()
