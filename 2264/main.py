#!/usr/bin/env python

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        if '999' in num:
            return '999'
        if '888' in num:
            return '888'
        if '777' in num:
            return '777'
        if '666' in num:
            return '666'
        if '555' in num:
            return '555'
        if '444' in num:
            return '444'
        if '333' in num:
            return '333'
        if '222' in num:
            return '222'
        if '111' in num:
            return '111'
        if '000' in num:
            return '000'
        return ""

def main():
    solution = Solution()
    print(solution.largestGoodInteger("6777133339"))

if __name__ == "__main__":
    main()
