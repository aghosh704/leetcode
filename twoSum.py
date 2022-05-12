from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for tmp in range(len(nums)):
            num_map[nums[tmp]] = tmp
        for tmp in range(len(nums)):
            curr_target = target - nums[tmp]
            pair_idx = num_map.get(curr_target, -1)
            if pair_idx != -1 and pair_idx != tmp:
                return [tmp, pair_idx]
        return [-1, -1]

    def twoSum_v2(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        left_idx = 0
        right_idx = len(nums) - 1
        while left_idx < right_idx:
            s = nums_sorted[left_idx] + nums_sorted[right_idx]
            if s < target:
                left_idx += 1
            elif s > target:
                right_idx -= 1
            else:
                return [left_idx, right_idx]

        return [-1, -1]

print(Solution().twoSum_v2([1,2,4], 6))