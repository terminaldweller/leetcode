#!/usr/bin/env python3
# not my solution


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        kMod = int(1e9) + 7
        dp = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}

        for _ in range(n - 1):
            newDp = {
                "a": dp["e"] + dp["i"] + dp["u"],
                "e": dp["a"] + dp["i"],
                "i": dp["e"] + dp["o"],
                "o": dp["i"],
                "u": dp["i"] + dp["o"],
            }
            dp = newDp

        return sum(dp.values()) % kMod


def main():
    solution = Solution()
    print(solution.countVowelPermutation(1))
    print(solution.countVowelPermutation(2))
    print(solution.countVowelPermutation(5))


if __name__ == "__main__":
    main()
