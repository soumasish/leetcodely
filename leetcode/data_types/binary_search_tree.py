
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, item):
        self.root = self.insert_helper(self.root, item)
        self.size += 1

    def insert_helper(self, root, item):
        if not root:
            root = TreeNode(item)
            return root
        if item > root.val:
            root.right = self.insert_helper(root.right, item)
        else:
            root.left = self.insert_helper(root.left, item)
        return root
    # def __init__(self):
    #     self.root = None
    #     self.size = 0
    #
    # def insert(self, item):
    #     self.root = self.insert_helper(item, self.root)
    #     self.size += 1
    #
    # def insert_helper(self, item, root):
    #     if root is None:
    #         return TreeNode(item)
    #     if item > root.val:
    #         root.right = self.insert_helper(item, root.right)
    #     else:
    #         root.left = self.insert_helper(item, root.left)
    #     return root


class TreeNode:
    def __init__(self, val ):
        self.val = val
        self.left = None
        self.right = None