"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.


"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for tmp in s:
            s_map[tmp] = s_map.get(tmp, 0) + 1
        for tmp in t:
            t_map[tmp] = t_map.get(tmp, 0) + 1
        return s_map == t_map