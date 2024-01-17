#!/usr/bin/env python


import typing


class Solution:
    def uniqueOccurrences(self, arr: typing.List[int]) -> bool:
        dici = {}
        for val in arr:
            if val in dici:
                dici[val] += 1
            else:
                dici[val] = 1

        return len(dici.values()) == len(set(dici.values()))


def main():
    solution = Solution()
    print(solution.uniqueOccurences([1, 2, 2, 1, 1, 3]))


if __name__ == "__main__":
    main()
