"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    from typing import List

    def __init__(self):
        self.res = []
    def generateParenthesis(self, n: int) -> List[str]:
        self.generateParenthesisHelper(n)
        return self.res


    def generateParenthesisHelper(self, n, open_cnt=0, closed_cnt=0, s="", cnt_so_far=0):

        if open_cnt == closed_cnt == n:
            self.res.append(s)
            return
        if open_cnt > closed_cnt:
            self.generateParenthesisHelper(n, open_cnt, closed_cnt + 1, s + ")", cnt_so_far)
        if open_cnt < n:
            self.generateParenthesisHelper(n, open_cnt + 1, closed_cnt, s + "(", cnt_so_far + 1)

print(Solution().generateParenthesis(3))