#!/usr/bin/env python


import typing


class Solution:
    def minFallingPathSum(self, matrix: typing.List[typing.List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = (
                    min(
                        matrix[i - 1][j],
                        matrix[i - 1][max(0, j - 1)],
                        matrix[i - 1][min(len(matrix[i]) - 1, j + 1)],
                    )
                    + matrix[i][j]
                )

        return min(matrix[-1])


def main():
    solution = Solution()
    print(solution.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))


if __name__ == "__main__":
    main()
