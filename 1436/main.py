#!/usr/bin/env python
import typing


class Solution:
    def destCity(self, paths: typing.List[typing.List[str]]) -> str:
        one = {}
        for path in paths:
            one[path[0]] = path[1]

        dest = one[paths[0][0]]
        while dest in one:
            dest = one[dest]

        return dest


def main():
    solution = Solution()
    paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    print(solution.destCity(paths))


if __name__ == "__main__":
    main()
