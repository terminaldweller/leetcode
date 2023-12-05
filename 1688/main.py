#!/usr/bin/env python

class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            if n % 2 == 0:
                matches += n // 2
                n = n // 2
            else:
                matches += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return matches

def main():
    solution = Solution()
    print(solution.numberOfMatches(7))

if __name__ == "__main__":
    main()
