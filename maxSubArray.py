"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
"""
class Solution:
    from typing import List
    def maxSubArray(self, nums: List[int]) -> int:
        new_nums = []
        sum_so_far = float('-inf')
        for tmp in nums:
            if tmp > sum_so_far + tmp:
                new_nums.append(tmp)
                sum_so_far = tmp
            else:
                sum_so_far += tmp
                new_nums.append(sum_so_far)
        return max(new_nums)

a = [-2, -1, -3, 4, -1, 2, 1, -5, 4]

print(Solution().maxSubArray(a))