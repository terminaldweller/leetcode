#!/usr/bin/env python

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)

        def feasible(weights, c, days):
            daysNeeded = 1
            currentLoad = 0
            for weight in weights:
                currentLoad += weight
                if currentLoad > c:
                    daysNeeded += 1
                    currentLoad = weight

            return daysNeeded <= days

        while start < end:
            mid = start + (end - start) // 2
            if feasible(weights, mid, days):
                end = mid
            else:
                start = mid + 1

        return start


if __name__ == "__main__":
    solution = Solution()
    print(solution.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    print(solution.shipWithinDays([3, 2, 2, 4, 1, 4], 3))
    print(solution.shipWithinDays([1, 2, 3, 1, 1], 4))
