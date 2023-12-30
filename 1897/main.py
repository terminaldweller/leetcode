#!/usr/bin/env python
import typing


class Solution:
    def makeEqual(self, words: typing.List[str]) -> bool:
        dicts: typing.Dict = {}
        for word in words:
            for c in word:
                if c in dicts:
                    dicts[c] += 1
                else:
                    dicts[c] = 1

        for k, v in dicts.items():
            if v % len(words) != 0:
                return False

        return True


def main():
    solution = Solution()
    print(solution.makeEqual(["abc", "aabc", "bc"]))


if __name__ == "__main__":
    main()
