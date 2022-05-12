"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        res = 0
        sign = 1
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

        s = s.lstrip()
        if len(s) == 0:
            return 0
        left = 0
        if s[0] == '+':
            left += 1
        elif s[0] == '-':
            sign = -1
            left += 1
        elif s[0] not in digits:
            return 0
        for idx in range(left, len(s)):
            if s[idx] in digits:
                res = res * 10 + int(s[idx])
            else:
                break
        res *= sign
        if res < 0:
            return max(res, MIN_INT)
        return min(res, MAX_INT)
    
print(Solution().myAtoi("     -12345"))

