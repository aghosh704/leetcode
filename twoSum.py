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

print(Solution().twoSum([1,2,3], 4))