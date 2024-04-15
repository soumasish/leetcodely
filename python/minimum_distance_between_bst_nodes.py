"""Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any
two different nodes in the tree."""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def minDiffInBST(self, root: Optional[TreeNode]):
        """
        :type root: TreeNode
        :rtype: int
        """

        min_diff = float('inf')
        prev = float('-inf')

        def inorder(node):
            nonlocal min_diff, prev
            if not node:
                return
            inorder(node.left)
            if prev != float('-inf'):
                min_diff = min(min_diff, node.val - prev)
            prev = node.val
            inorder(node.right)

        inorder(root)
        return min_diff

