#!/usr/bin/env python3
# used the hints

import math


class Solution:
    def poorPigs_v2(
        self, buckets: int, minutesToDie: int, minutesToTest: int
    ) -> int:
        number_of_tries: int = math.floor(minutesToTest / minutesToDie)
        if number_of_tries == 1:
            boundary = math.log(buckets, 10) / math.log(2, 10)
            return math.ceil(boundary)
        else:
            boundary = math.log(buckets, 10) / math.log(number_of_tries, 10)
            return math.ceil(boundary)

    def poorPigs(
        self, buckets: int, minutesToDie: int, minutesToTest: int
    ) -> int:
        result: int = 0
        number_of_tries: int = math.floor(minutesToTest / minutesToDie)
        while pow(number_of_tries + 1, result) < buckets:
            result += 1
        return result


def main():
    solution = Solution()
    print(solution.poorPigs(1000, 15, 60))
    print(solution.poorPigs(4, 15, 15))
    print(solution.poorPigs(4, 15, 30))
    print(solution.poorPigs(8, 15, 40))


if __name__ == "__main__":
    main()
