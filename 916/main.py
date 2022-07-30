#!/usr/bin/env python3

import copy
from typing import List, Dict


class Solution:
    def wordSubsets_v2(
        self, words1: List[str], words2: List[str]
    ) -> List[str]:
        """Way too slow.Way too stupid."""
        words2_maps: List[Dict] = []
        result: List[str] = []

        def get_map(word):
            word_map: Dict[str, int] = {}
            for char in word:
                if char in word_map:
                    word_map[char] = word_map[char] + 1
                else:
                    word_map[char] = 1

            return word_map

        for word in words2:
            words2_maps.append(get_map(word))
        word_map: Dict[str, int] = {}
        for word in words1:
            for char in word:
                if char in word_map:
                    word_map[char] = word_map[char] + 1
                else:
                    word_map[char] = 1
            is_matching = True
            for word2_map in words2_maps:
                for k, v in word2_map.items():
                    if k in word_map:
                        if v <= word_map[k]:
                            pass
                        else:
                            is_matching = False
                            break
                    else:
                        is_matching = False
                        break
                if is_matching:
                    pass
                else:
                    break
            if is_matching:
                result.append(word)
            # words1_maps.append(copy.deepcopy(word_map))
            word_map = {}
            is_matching = False

        return result

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def count(word):
            ans = [0] * 26
            for c in word:
                ans[ord(c) - ord("a")] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            ls = count(b)
            for i in range(26):
                bmax[i] = max(bmax[i], ls[i])

        ans = []
        for a in A:
            ls = count(a)
            for i in range(26):
                if ls[i] < bmax[i]:
                    break
            else:
                ans.append(a)
        return ans


def main():
    words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words2 = ["e", "o"]
    words3 = ["amazon", "apple", "facebook", "google", "leetcode"]
    words4 = ["l", "e"]
    solution = Solution()
    print(solution.wordSubsets(words1, words2))
    print(solution.wordSubsets(words3, words4))


if __name__ == "__main__":
    main()
