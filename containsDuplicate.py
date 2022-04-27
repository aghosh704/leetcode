"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.


"""
class Solution:
    from typing import List
    def containsDuplicate(self, nums: List[int]) -> bool:
        #could use a set
        num_map = {}
        for tmp in nums:
            if tmp in num_map:
                return True
            else:
                num_map[tmp] = True
        return False