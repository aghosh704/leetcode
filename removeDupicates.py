"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that
each unique element appears only once. The relative order of the elements should be kept the same.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for idx, num in enumerate(nums):
            if nums[idx] > nums[i]:
                nums[i+1] = nums[idx]
                i += 1
        #
        print(nums)
        return i+1
x = Solution().removeDuplicates([1,2,3,3])
print("val=", x)