#!/usr/bin/env python

import typing


class Solution:
    def minCost(self, colors: str, neededTime: typing.List[int]) -> int:
        time = 0
        n = len(colors)
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                time += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        return time


def main():
    solution = Solution()
    print(solution.minCost("abaa", [1, 2, 3, 4]))


if __name__ == "__main__":
    main()
