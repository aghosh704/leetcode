"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climbStairsHelper(n, {})

    def climbStairsHelper(self, n: int, memo) -> int:
        if n in memo:
            return memo[n]
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        a = self.climbStairsHelper(n-1, memo)
        b = self.climbStairsHelper(n-2, memo)
        memo[n-1] = a
        memo[n-2] = b
        return a + b

x = Solution().climbStairs(5)
print(x)
