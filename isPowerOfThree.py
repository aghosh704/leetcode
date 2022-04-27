"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the
range that is missing from the array.
"""
class Solution:
        def isPowerOfThree(self, n: int) -> bool:
            while n > 1:
                n = n / 3
            return n == 1

print(Solution().isPowerOfThree(27))