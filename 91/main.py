#!/usr/bin/env python


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, len(s) + 1):
            print(s[i - 1 : i])
            if 0 < int(s[i - 1 : i]) <= 9:
                dp[i] += dp[i - 1]
            print(s[i - 2 : i])
            if 10 <= int(s[i - 2 : i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]


def main():
    solution = Solution()
    print(solution.numDecodings("12"))
    print(solution.numDecodings("226"))
    print(solution.numDecodings("06"))


if __name__ == "__main__":
    main()
