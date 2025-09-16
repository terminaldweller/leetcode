#!/usr/bin/env python


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(":
                stack.append("(")
            elif char == "[":
                stack.append("[")
            elif char == "{":
                stack.append("{")
            elif char == ")":
                if len(stack) == 0:
                    return False
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif char == "]":
                if len(stack) == 0:
                    return False
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif char == "}":
                if len(stack) == 0:
                    return False
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False

        if len(stack) != 0:
            return False

        return True


def main() -> None:
    solution = Solution()


if __name__ == "__main__":
    main()
