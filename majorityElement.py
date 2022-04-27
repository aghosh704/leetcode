"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

"""
import math


class Solution:
    from typing import List
    def majorityElement(self, nums: List[int]) -> int:
        mid = math.ceil(len(nums) / 2)
        num_cnts = {}
        for tmp in nums:
            num_cnts[tmp] = num_cnts.get(tmp, 0) + 1
            if num_cnts.get(tmp) >= mid:
                return tmp
