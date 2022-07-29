#!/usr/bin/env python3

from typing import List


class Solution:
    @staticmethod
    def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
        def match(word):
            map1, map2 = {}, {}
            return all(
                (map1.setdefault(i, j), map2.setdefault(j, i)) == (j, i)
                for i, j in zip(word, pattern)
            )

        results = []
        for result in filter(match, words):
            results.append(result)
        return results


def main():
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"
    print(Solution.findAndReplacePattern(words, pattern))


if __name__ == "__main__":
    main()
