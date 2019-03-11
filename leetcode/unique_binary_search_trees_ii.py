# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        if n == 0:
            return []

        def _generated_trees(i, j):
            if i == j + 1:
                return [None]
            ans = []
            for k in range(i, j + 1):
                left = _generated_trees(i, k - 1)
                right = _generated_trees(k + 1, j)

                for left_sub_tree in left:
                    for right_sub_tree in right:
                        root = TreeNode(k)
                        root.left = left_sub_tree
                        root.right = right_sub_tree
                        ans.append(root)
            return ans

        return _generated_trees(1, n)
