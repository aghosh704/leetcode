"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

"""
class Solution:
    def strstr_i(self, str1, str2):
        return True if str1 == str2 else False

    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            haystack_c = haystack[i:i+len(needle)]
            if len(haystack_c) == len(needle):
                if self.strstr_i(haystack_c, needle):
                    return i
                else:
                    continue
            else:
                break
        return -1

a = "hello"
b = "llx"
x = Solution().strStr(a, b)
print(x)