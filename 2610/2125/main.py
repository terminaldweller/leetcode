#!/usr/bin/env python

import typing


class Solution:
    def numberOfBeams(self, bank: typing.List[str]) -> int:
        row_count = 0
        result = 0
        for row in bank:
            count = row.count("1")
            if count != 0:
                result += row_count * count
                row_count = row.count("1")

        return result


def main():
    solution = Solution()
    print(solution.numberOfBeams(["011001", "000000", "010100", "00100"]))
    print(solution.numberOfBeams(["000", "111", "000"]))


if __name__ == "__main__":
    main()
