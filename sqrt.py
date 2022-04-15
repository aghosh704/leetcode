"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        guess = 2
        while True:
            this_num = guess * guess
            if this_num == x:
                return guess
            elif this_num > x:
                return guess - 1
            else:
                guess += 1



print(Solution().mySqrt(4), pow(4, 0.5))