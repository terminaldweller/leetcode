#!/usr/bin/env python


class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def fact(n, memo):
            if n <= 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = fact(n - 1, memo) + fact(n - 2, memo)
            return memo[n]

        return fact(n, memo)


def main():
    solution = Solution()
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
    print(solution.climbStairs(44))


if __name__ == "__main__":
    main()
