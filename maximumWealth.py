class Solution:
    def maximumWealth(self, accounts) -> int:
        max_wealth = float('-inf')
        for tmp in accounts:
            this_sum = sum(tmp)
            if this_sum > max_wealth:
                max_wealth = this_sum
        return max_wealth
