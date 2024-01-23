#!/usr/bin/env python


import typing


class Solution:
    def maxLength(self, arr: typing.List[str]) -> int:
        result = [0]
        self.dfs(arr, "", 0, result)
        return result[0]

    def dfs(self, arr, path, idx, result):
        if self.isUniqueChars(path):
            result[0] = max(result[0], len(path))

        if idx == len(arr) or not self.isUniqueChars(path):
            return

        for i in range(idx, len(arr)):
            self.dfs(arr, path + arr[i], i + 1, result)

    def isUniqueChars(self, s):
        char_set = set()
        for c in s:
            if c in char_set:
                return False
            char_set.add(c)
        return True


def main():
    solution = Solution()
    print(solution.maxLength(["un", "iq", "ue"]))
    print(solution.maxLength(["cha", "r", "act", "ers"]))
    print(solution.maxLength(["abcdefghijklmnopqrstuvwxyz"]))


if __name__ == "__main__":
    main()
