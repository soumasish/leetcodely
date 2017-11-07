"""Created by sgoswami on 8/9/17."""
"""Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center)."""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return root is None or self.is_symmetric_helper(root.left, root.right)

    def is_symmetric_helper(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        return self.is_symmetric_helper(left.left, right.right) and self.is_symmetric_helper(left.right, right.left)