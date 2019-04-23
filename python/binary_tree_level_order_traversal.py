"""Created by sgoswami on 7/19/17."""
"""Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right,
 level by level)."""
from collections import deque
from python.ds.binary_search_tree import BinarySearchTree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res, level = [], []
        queue = deque()
        queue.appendleft(root)
        queue.appendleft('#')
        while len(queue) > 0:
            curr = queue.pop()
            if curr == '#':
                if len(queue) > 0:
                    queue.appendleft('#')
                res.append(level[:])
                level = []
                continue
            else:
                level.append(curr.val)
            if curr.left:
                queue.appendleft(curr.left)
            if curr.right:
                queue.appendleft(curr.right)
        return res


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(3)
    bst.insert(9)
    bst.insert(15)
    bst.insert(7)
    solution = Solution()
    print(solution.levelOrder(bst.root))
