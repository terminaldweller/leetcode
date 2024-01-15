#!/usr/bin/env python
import typing


class Solution:
    def findWinners(
        self, matches: typing.List[typing.List[int]]
    ) -> typing.List[typing.List[int]]:
        record: typing.Dict[int, int] = {}
        zeroes = []
        ones = []

        for match in matches:
            if match[0] not in record:
                record[match[0]] = 0

            if match[1] not in record:
                record[match[1]] = 1
            else:
                record[match[1]] += 1

        for k, v in record.items():
            if v == 0:
                zeroes.append(k)
            elif v == 1:
                ones.append(k)

        return [sorted(zeroes), sorted(ones)]


def main():
    solution = Solution()
    print(
        solution.findWinners(
            [
                [1, 3],
                [2, 3],
                [3, 6],
                [5, 6],
                [5, 7],
                [4, 5],
                [4, 8],
                [4, 9],
                [10, 4],
                [10, 9],
            ]
        )
    )


if __name__ == "__main__":
    main()
