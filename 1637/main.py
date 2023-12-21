#!/usr/bin/env python
import typing


class Solution:
    def maxWidthOfVerticalArea(self, points: typing.List[typing.List[int]]) -> int:
        p: typing.List[int] = []
        for point in points:
            p.append(point[0])
        p.sort()
        s = 0
        for i in range(1, len(p)):
            s = max(p[i] - p[i - 1], s)
        return s


def main():
    solution = Solution()
    points = [[8, 7], [9, 9], [7, 4], [9, 7]]
    print(solution.maxWidthOfVerticalArea(points))


if __name__ == "__main__":
    main()
