"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

"""
import math


class Solution:

    def mypow_helper(self, x: float, n: int) ->float:
        if x == 0: return 0
        if n == 0: return 1

        res = self.mypow_helper(x, n // 2)
        return res * res if n % 2 == 0 else x * res * res

    def myPow(self, x: float, n: int) -> float:
        return 1/self.mypow_helper(x, abs(n)) if n < 0 else self.mypow_helper(x, n)

print(Solution().myPow(2, 2))
