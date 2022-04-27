class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_pal = ""
        for tmp in range(len(s)):
            odd_result = self.expand_odd(s, tmp)
            even_result = self.expand_even(s, tmp)
            if odd_result[1] - odd_result[0] > len(max_pal):
                max_pal = s[odd_result[0]:odd_result[1] ]
            if even_result[1] - even_result[0] > len(max_pal):
                max_pal = s[even_result[0]:even_result[1] ]

        return max_pal

    def expand_odd(self, s, start):
        end = start
        while len(s) > 0 and start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return start + 1, end

    def expand_even(self, s, start):
        end = start + 1
        while len(s) > 0 and start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return start + 1, end
1