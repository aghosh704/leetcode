"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order
of the non-zero elements.
"""
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        still_to_move = True
        while still_to_move:
            still_to_move = False
            for i in range(len(nums)):
                if nums[i] == 0 and i != len(nums)-1 and nums[i + 1] != 0:
                    still_to_move = True
                    nums[i] = nums[i + 1]
                    nums[i + 1] = 0

        print(nums)

    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nz_cnt = []
        for i in range(len(nums)):
            if nums[i] != 0:
                nz_cnt.append(nums[i])
        nums[0:len(nz_cnt)] = nz_cnt
        nums[len(nz_cnt):] = [0] * (len(nums) - len(nz_cnt))
        return nums

print(Solution().moveZeroes2([1, 0, 5, 8, 0, 12]))


