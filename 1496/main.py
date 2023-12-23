#!/usr/bin/env python


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        visited = set()
        visited.add((x, y))
        for i in path:
            if i == "N":
                y += 1
            elif i == "S":
                y -= 1
            elif i == "E":
                x += 1
            else:
                x -= 1
            if (x, y) in visited:
                return True
            visited.add((x, y))
        return False


def main():
    solution = Solution()
    print(solution.isPathCrossing("NES"))


if __name__ == "__main__":
    main()
