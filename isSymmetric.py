
"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

from typing import Optional
from inorderTraversal import TreeNode
class Solution:
        def isSymmetricHelper(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if left is None and right is None:
                return True

            if right is not None and left is None:
                return False

            if right is None and left is not None:
                return False

            if left.val != right.val:
                return False

            return self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)

        def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            return self.isSymmetricHelper(root.left, root.right)