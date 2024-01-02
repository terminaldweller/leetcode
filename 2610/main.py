#!/usr/bin/env python
import typing


class Solution:
    def findMatrix(self, nums: typing.List[int]) -> typing.List[typing.List[int]]:
        dicts = {}
        for num in nums:
            if num in dicts:
                dicts[num] += 1
            else:
                dicts[num] = 1

        row = 0
        results = []
        for i in range(max(dicts.values())):
            results.append([])
        while max(dicts.values()) > 0:
            for k, v in dicts.items():
                if v >= 1:
                    results[row].append(k)
                    dicts[k] -= 1
            row += 1

        return results


def main():
    s = Solution()
    print(s.findMatrix([1, 3, 4, 1, 2, 3, 1]))
    print(s.findMatrix([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
