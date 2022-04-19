
"""
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never
differs by more than one.
"""

from typing import Optional
from inorderTraversal import TreeNode
from inorderTraversal import printTree


class Solution:
    from typing import List
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 2:
            n = TreeNode(nums[1])
            n.left = TreeNode(nums[0])
            return n
        else:
            mid = len(nums) // 2
            n = TreeNode(nums[mid])
            n.left = self.sortedArrayToBST(nums[0:mid])

            n.right = self.sortedArrayToBST(nums[mid+1:])
            return n

nums = [-10,-3,0,5,9]
t = Solution().sortedArrayToBST(nums)

printTree(t)