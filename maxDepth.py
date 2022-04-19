
"""
Given the root of a binary tree, find its max depth.
"""

from typing import Optional
from inorderTraversal import TreeNode
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))