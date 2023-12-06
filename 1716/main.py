#!/usr/bin/env python

class Solution:
    def totalMoney(self, n:int)->int:
        week = n // 7
        day = n % 7
        total = 0
        for i in range(week):
            total += 28 + 7 * i
        for i in range(day):
            total += week + i + 1
        return total

def main():
    solution = Solution()
    print(solution.totalMoney(4))
    print(solution.totalMoney(10))
    print(solution.totalMoney(20))

if __name__ == '__main__':
    main()
