class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 0:
            return 0
        if len(s) == 1:
            return 1
        max_len = 1
        l_ptr = 0
        r_ptr = 1
        char_map = {s[0]: 0}
        for r_ptr in range(1, len(s)):
            v = s[r_ptr]
            if v in char_map and char_map[v] >= l_ptr:

                if r_ptr - l_ptr > max_len:
                    max_len = r_ptr - l_ptr
                l_ptr = char_map[v] + 1
                char_map[v] = r_ptr

            else:
                char_map[v] = r_ptr

        return max(max_len, r_ptr - l_ptr + 1)


print(Solution().lengthOfLongestSubstring("au"))