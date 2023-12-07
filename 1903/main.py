#!/usr/bin/env python

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""

def main():
    solution = Solution()
    print(solution.largestOddNumber("52"))
    print(solution.largestOddNumber("4206"))
    print(solution.largestOddNumber("35427"))

if __name__ == "__main__":
    main()
