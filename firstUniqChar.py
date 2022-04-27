"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c_map = {}
        for tmp in s:
            c_map[tmp] = c_map.get(tmp, 0) + 1
        print(c_map)
        for tmp in range(len(s)):
            if c_map[s[tmp]] == 1:
                return tmp
        return -1


print(Solution().firstUniqChar("loveleetcode"))