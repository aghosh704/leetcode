class Solution:

    def romanToInt(self, s: str) -> int:
        roman_symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        idx = 0
        while True:
            if idx >= len(s):
                break
            tmp = s[idx]
            if tmp == "I":
                if idx + 1 < len(s) and s[idx + 1] == 'V':
                    num += 4
                    idx += 1
                elif idx + 1 < len(s) and s[idx + 1] == 'X':
                    num += 9
                    idx += 1
                else:
                    num += roman_symbols[tmp]
            elif tmp == "X":
                if idx + 1 < len(s) and s[idx + 1] == 'L':
                    num += 40
                    idx += 1
                elif idx + 1 < len(s) and s[idx + 1] == 'C':
                    num += 90
                    idx += 1
                else:
                    num += roman_symbols[tmp]
            elif tmp == "C":
                if idx + 1 < len(s) and s[idx + 1] == 'D':
                    num += 400
                    idx += 1
                elif idx + 1 < len(s) and s[idx + 1] == 'M':
                    num += 900
                    idx += 1
                else:
                    num += roman_symbols[tmp]
            else:
                num += roman_symbols[tmp]

            idx += 1

        return num

print(Solution().romanToInt("III"))