#!/usr/bin/env python
import typing


class Solution:
    def minOperations(self, nums: typing.List[int]) -> int:
        dicts: typing.Dict = {}
        for num in nums:
            if num in dicts:
                dicts[num] += 1
            else:
                dicts[num] = 1

        sum = 0
        print(dicts)
        for k, v in dicts.items():
            if v == 1:
                return -1
            sum += v // 3
            if v % 3:
                sum += 1

        return sum


def main():
    solution = Solution()
    print(solution.minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]))
    print(solution.minOperations([2, 1, 2, 2, 3, 3]))
    print(
        solution.minOperations(
            [14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12]
        )
    )
    print(solution.minOperations([19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19, 19]))


if __name__ == "__main__":
    main()
