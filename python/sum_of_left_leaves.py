# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def preorder(node, left):
            if not root:
                return
            if left and not root.left and not root.right:
                cache[0] += root.val



