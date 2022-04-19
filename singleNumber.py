"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


"""



from itertools import zip_longest
from typing import List


class Solution:
    def grouper(self, iterable, n, fillvalue=None):

        args = [iter(iterable)] * n
        return zip_longest(*args, fillvalue=fillvalue)

    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums_sorted = sorted(nums)
        for x, y in self.grouper(nums_sorted, 2, -1):
            if x != y:
                return x

print(Solution().singleNumber([1,1,2,2,3,4,4]))