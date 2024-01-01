#!/usr/bin/env python

import typing


class Solution:
    def findContentChildren(self, g: typing.List[int], s: typing.List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        g_idx = 0
        s_idx = 0
        count = 0

        while s_idx < len(s) and g_idx < len(g):
            if s[s_idx] >= g[g_idx]:
                count += 1
                s_idx += 1
                g_idx += 1
            else:
                s_idx += 1

        return count


def main():
    solution = Solution()
    print(solution.findContentChildren([1, 2, 3], [1, 1]))
    print(solution.findContentChildren([1, 2], [1, 2, 3]))


if __name__ == "__main__":
    main()
