#!/usr/bin/env python
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations: List[str] = []
        if digits is None or len(digits) == 0:
            return combinations

        def find_combinations(
            combinations,
            digits,
            previous,
            index,
            letters_numbers_mapping,
        ):
            if index == len(digits):
                combinations.append(previous)
                return
            letters = letters_numbers_mapping[int(digits[index])]
            for i in range(0, len(letters)):
                find_combinations(
                    combinations,
                    digits,
                    previous + letters[i],
                    index + 1,
                    letters_numbers_mapping,
                )

        letters_numbers_mapping = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz",
        ]
        find_combinations(combinations, digits, "", 0, letters_numbers_mapping)
        return combinations


def main():
    solution = Solution()
    print(solution.letterCombinations("23"))


if __name__ == "__main__":
    main()
