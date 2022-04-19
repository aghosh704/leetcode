"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing
all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters
include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        f_ptr = 0
        s_ptr = len(s) - 1
        while f_ptr < s_ptr:
            while not s[f_ptr].isalnum():
                f_ptr += 1
                if f_ptr >= len(s):
                    return True
            while not s[s_ptr].isalnum():
                s_ptr -= 1
                if s_ptr < 0:
                    return True
            if s[s_ptr].lower() == s[f_ptr].lower():
                s_ptr -= 1
                f_ptr += 1
            else:
                break
        if f_ptr >= s_ptr:
            return True
        else:
            return False

str = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(str))