"""Created by sgoswami on 7/16/17."""
"""Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
Note: If the given node has no in-order successor in the tree, return null."""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # if root is None:
        #     return None
        # if root.val <= p.val:
        #     return self.inorderSuccessor(root.right, p)
        # else:
        #     left = self.inorderSuccessor(root.left, p)
        #     if left is not None:
        #         return left
        #     else:
        #         return root

        if root is None:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            if left:
                return left
            else:
                return root