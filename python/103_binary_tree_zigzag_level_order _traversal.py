"""Created by sgoswami on 8/8/17."""
"""Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then 
right to left for the next level and alternate between)."""

import collections


class BST:
    def __init__(self):
        self.root = None

    def add(self, item):
        self.root = self.insert_helper(self.root, item)
        return self.root

    def insert_helper(self, root, item):
        if root is None:
            root = TreeNode(item)
            return root
        if item < root.val:
            root.left = self.insert_helper(root.left, item)
        else:
            root.right = self.insert_helper(root.right, item)
        return root

    def inorder(self):
        self.inorder_helper(self.root)

    def inorder_helper(self, root):
        if root is None:
            return
        self.inorder_helper(root.left)
        print(root.val, end=', ')
        self.inorder_helper(root.right)


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        queue = collections.deque()
        delimiter = '#'
        trigger = False
        queue.appendleft(root)
        queue.appendleft(delimiter)
        level = collections.deque()
        while len(queue) > 0:
            curr = queue.pop()
            if curr == delimiter:
                res.append(list(level))
                level = collections.deque()
                if len(queue) > 0:
                    queue.appendleft(delimiter)
                trigger = not trigger
            else:
                level.append(curr.val)
                if trigger:
                    if curr.right:
                        queue.appendleft(curr.right)
                    if curr.left:
                        queue.appendleft(curr.left)
                else:
                    if curr.left:
                        queue.appendleft(curr.left)
                    if curr.right:
                        queue.appendleft(curr.right)
        return res


if __name__ == '__main__':
    bst = BST()
    bst.add(9)
    bst.add(3)
    bst.add(20)
    bst.add(15)
    bst.add(21)
    solution = Solution()
    print(solution.zigzagLevelOrder(bst.root))