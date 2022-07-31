#!/usr/bin/env python3
"""307"""

from typing import List


class NumArray_Naive:
    """Naive implementation. Useless."""

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        """Update."""
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        """sumRange."""
        return sum(self.nums[left : right + 1])


class NumArray:
    """Segment Tree implementation."""

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)
        self.segment_tree = [0] * (len(nums) * 2)
        self.build_segment_tree()

    def build_segment_tree(self):
        """build segment tree."""
        for i, j in zip(range(self.n, 2 * self.n), range(0, len(self.nums))):
            self.segment_tree[i] = self.nums[j]
        for i in reversed(range(1, self.n)):
            self.segment_tree[i] = (
                self.segment_tree[i * 2] + self.segment_tree[i * 2 + 1]
            )
        # print(self.segment_tree)

    def update_segment_tree(self, index: int, val: int):
        """update segment tree."""
        pos: int = index + self.n
        self.segment_tree[pos] = val
        while pos > 0:
            left = pos
            right = pos
            if pos % 2 == 0:
                right = pos + 1
            else:
                left = pos - 1
            self.segment_tree[int(pos / 2)] = (
                self.segment_tree[left] + self.segment_tree[right]
            )
            pos = int(pos / 2)

    def update(self, index: int, val: int) -> None:
        """Update."""
        self.update_segment_tree(index, val)

    def sumRange(self, left: int, right: int) -> int:
        """sumRange."""
        l = left + self.n
        r = right + self.n
        s: int = 0

        while l <= r:
            if (l % 2) == 1:
                s += self.segment_tree[l]
                l += 1
            if (r % 2) == 0:
                s += self.segment_tree[r]
                r -= 1
            l = int(l / 2)
            r = int(r / 2)

        return s


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


def main():
    """Main."""
    num_array = NumArray([1, 3, 5])
    print(num_array.sumRange(0, 2))
    num_array.update(1, 2)
    print(num_array.sumRange(0, 2))


if __name__ == "__main__":
    main()
