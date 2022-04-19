"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.val))
        printTree(node.right, level + 1)

class Solution:
    from typing import Optional, List

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversalHelper(root, [])

    def inorderTraversalHelper(self, root: Optional[TreeNode], traversal) -> List[int]:
        if root is not None:
            self.inorderTraversalHelper(root.left, traversal)
            traversal.append(root.val)
            self.inorderTraversalHelper(root.right, traversal)
        return traversal
