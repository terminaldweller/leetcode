#!/usr/bin/env python


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        result = -1
        for c in s:
            if s.count(c) > 1:
                result = max(result, s.rfind(c) - 1 - s.find(c))

        return result


def main():
    solution = Solution()
    print(solution.maxLengthBetweenEqualCharacters("aa"))
    print(solution.maxLengthBetweenEqualCharacters("abca"))
    print(solution.maxLengthBetweenEqualCharacters("cbzxy"))
    print(solution.maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv"))


if __name__ == "__main__":
    main()
