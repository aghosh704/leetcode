"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


"""

class Solution:
    from typing import List
    def __init__(self):
        self.res = []
    letters_map = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'
    }

    def letterCombinations(self, digits: str) -> List[str]:
        self.back_track(0, digits, "")
        return self.res

    def back_track(self, idx, digits, ans):
        if len(ans) == len(digits):
            self.res.append(ans)
            #print(self.res)
            return

        for ch in self.letters_map[int(digits[idx])]:
            self.back_track(idx + 1, digits, ans + ch)



print(Solution().letterCombinations("23"))

