#!/usr/bin/env python


class Solution:
    def minOperations(self, s: str) -> int:
        f_c = 0
        b_c = 0
        cond = 48
        for c in s:
            if ord(c) != cond:
                f_c += 1

            if cond == 48:
                cond = 49
            else:
                cond = 48

            if ord(c) != cond:
                b_c += 1

        print(f_c, b_c)
        return min(f_c, b_c)


def main():
    solution = Solution()
    print(solution.minOperations("0100"))
    print(solution.minOperations("10"))
    print(solution.minOperations("1111"))
    print(solution.minOperations("1100010111"))


if __name__ == "__main__":
    main()
