#!/usr/bin/env python
import typing


class Solution:
    def getAverage(self, M, i, j):
        sum = 0
        count = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if x >= 0 and x < len(M) and y >= 0 and y < len(M[x]):
                    sum += M[x][y]
                    count += 1
        return sum // count

    def imageSmoother(
        self, M: typing.List[typing.List[int]]
    ) -> typing.List[typing.List[int]]:
        result: typing.List[typing.List[int]] = [
            [0 for _ in range(len(M[0]))] for _ in range(len(M))
        ]
        for i in range(len(M)):
            for j in range(len(M[i])):
                result[i][j] = self.getAverage(M, i, j)

        return result


def main():
    img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    img2 = [[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13]]
    img3 = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
    solution = Solution()
    print(solution.imageSmoother(img))
    print(solution.imageSmoother(img2))
    print(solution.imageSmoother(img3))


if __name__ == "__main__":
    main()
