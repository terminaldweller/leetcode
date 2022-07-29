#!/usr/bin/env python3

from typing import List


class Solution:
    @staticmethod
    def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
        def match(w):
            m1, m2 = {}, {}
            return all(
                (m1.setdefault(i, j), m2.setdefault(j, i)) == (j, i)
                for i, j in zip(w, pattern)
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
