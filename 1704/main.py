#!/usr/bin/env python


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        length = len(s) // 2
        first = 0
        second = 0
        for i in range(0, length):
            if s[i] in vowels:
                first += 1

            if s[length + i] in vowels:
                second += 1

        if first == second:
            return True
        return False


def main():
    solution = Solution()
    print(solution.halvesAreAlike("book"))
    print(solution.halvesAreAlike("textbook"))
    print(solution.halvesAreAlike("AbCdEfGh"))


if __name__ == "__main__":
    main()
