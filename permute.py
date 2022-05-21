"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""
from typing import List


class Solution:
   
    def permute(self, lst: List[int]):
        if len(lst) == 1:
            return [lst]

        first = lst[0]
        rest = lst[1:]
        output = []
        for perm in self.permute(rest):
            for i in range(len(perm) + 1):
                new = perm[:i] + [first] + perm[i:]
                output.append(new)
        return output