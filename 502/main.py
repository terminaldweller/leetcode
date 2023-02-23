#!/usr/bin/env python
from typing import List
import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        print(projects)
        projects.sort()
        print(projects)

        q = []
        ptr = 0

        for _ in range(k):
            while ptr < n and projects[ptr][0] <= w:
                heapq.heappush(q, -projects[ptr][1])
                ptr += 1
            if not q:
                break
            w += -heapq.heappop(q)

        return w


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
