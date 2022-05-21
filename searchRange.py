"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

class Solution:

    def binarySearch_first(self, nums: List[int], target: int, low, high) -> int:

        if high >= low:

            mid = low + (high - low) // 2
            if target > nums[mid]:
                return self.binarySearch_first(nums, target, mid + 1, high)
            elif (mid == 0 or nums[mid - 1] < target) and nums[mid] == target:
                return mid
            else:
                return self.binarySearch_first(nums, target, low, mid-1)
        else:
            return -1

    def binarySearch_last(self, nums: List[int], target: int, low, high) -> int:

        if high >= low:

            mid = low + (high - low) // 2
            if nums[mid] > target:
                return self.binarySearch_last(nums, target, low, mid-1)
            elif nums[mid] == target and (mid == high or nums[mid + 1] > target):
                return mid
            else:
                return self.binarySearch_last(nums, target, mid + 1, high)
        else:
            return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        i1 = self.binarySearch_first(nums, target, 0, len(nums)-1)
        i2 = self.binarySearch_last(nums, target, 0, len(nums)-1)
        print(i1, i2)




print(Solution().searchRange([3, 3, 3], 3))
