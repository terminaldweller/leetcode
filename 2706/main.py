#!/usr/bin/env python
import typing


class Solution:
    def buyChoco(self, prices: typing.List[int], money: int) -> int:
        price_dict: typing.Dict = {}
        for i in range(len(prices)):
            price_dict[prices[i]] = (
                price_dict[prices[i]] + 1 if prices[i] in price_dict else 1
            )

        mini = min(prices)
        if price_dict[mini] >= 2:
            if mini * 2 <= money:
                return money - mini * 2
            else:
                return money

        slider = mini + 1
        maxi = max(prices)
        while slider <= maxi:
            if slider in price_dict:
                if mini + slider <= money:
                    return money - mini - slider
            slider += 1

        return money


def main():
    solution = Solution()
    print(solution.buyChoco([1, 2, 1, 3, 2], 4))
    print(solution.buyChoco([10, 10, 10, 10], 20))
    print(solution.buyChoco([1, 2, 2], 3))
    print(solution.buyChoco([3, 2, 3], 3))


if __name__ == "__main__":
    main()
