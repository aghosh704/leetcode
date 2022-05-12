"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
class Solution:
    from typing import List


    def threeSum(self, nums: List[int]) -> List[List[int]]:

        arr = []
        if len(nums) < 3:
            return []
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l< r:
                if nums[i] + nums[l] + nums[r] == 0:
                    x = [nums[i], nums[l], nums[r]]
                    x.sort()
                    arr.append(x)
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
        return [list(x) for x in set(tuple(x) for x in arr)]

a = [-1,0,1,2,-1,-4]
a = [1, 2, -2, -1]
#a = [0, 0]
print(Solution().threeSum(a))
#[[-1, 0, 1], [-1, -1, 2], [1, -1, 0], [2, -4, 2]]
