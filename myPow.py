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

    def myPow_v2(self, x: float, n: int) -> float:
        p = abs(n)
        if p == 0:
            return 1
        elif p % 2 == 0:
            y = self.myPow(x, p // 2)
            return y * y if n >= 0 else 1 / (y * y)
        else:
            y = self.myPow(x, p // 2)
            y = y * y * x
            return y if n >= 0 else 1 / y

print(Solution().myPow_v2(2, -2))
