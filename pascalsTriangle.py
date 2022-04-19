from typing import Optional, List
from inorderTraversal import TreeNode
from inorderTraversal import printTree

"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for numRow in range(1, numRows + 1):
            if numRow == 1:
                triangle.append([1])
            elif numRow == 2:
                triangle.append([1, 1])
            else:
                thisrow = [1]
                prev_row = triangle[numRow - 2]
                plist = zip(prev_row, prev_row[1:])
                for tmp in list(plist):
                    thisrow.append(tmp[0] + tmp[1])
                thisrow.append(1)
                triangle.append(thisrow)
        return triangle

Solution().generate(5)