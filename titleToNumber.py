"""
Given a string columnTitle that represents the column title as appear in an Excel sheet,
return its corresponding column number.
A -> 1
B -> 2
C -> 3
"""
class Solution:

    def titleToNumber(self, columnTitle: str) -> int:
        alpha_map = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
            'E': 5,
            'F': 6,
            'G': 7,
            'H': 8,
            'I': 9,
            'J': 10,
            'K': 11,
            'L': 12,
            'M': 13,
            'N': 14,
            'O': 15,
            'P': 16,
            'Q': 17,
            'R': 18,
            'S': 19,
            'T': 20,
            'U': 21,
            'V': 22,
            'W': 23,
            'X': 24,
            'Y': 25,
            'Z': 26
        }
        final_sum = 0
        idx = 0
        for num in columnTitle[::-1]:
            if idx > 0:
                final_sum += (pow(26, idx) * alpha_map[num])
            else:
                final_sum += alpha_map[columnTitle[-1]]
            idx += 1
        return final_sum


print(Solution().titleToNumber("FXSHRXW"))
print(ord('C')-64)