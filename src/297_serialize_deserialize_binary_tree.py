"""Created by sgoswami on 8/13/17."""
"""Serialization is the process of converting a data structure or object into a sequence of bits so that it can be 
stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the 
same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your 
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a 
string and this string can be deserialized to the original tree structure."""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        curr_str = ''
        self.serialize_helper(root, curr_str)
        return curr_str

    def serialize_helper(self, root, curr_str):
        if not root:
            curr_str += '#'
            return
        curr_str += str(root.val)
        self.serialize_helper(root.left, curr_str)
        self.serialize_helper(root.right, curr_str)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        itr = iter(data)
        return self.deserialize_helper(data, itr)


    def deserialize_helper(self, data, itr):
        item = next(itr)
        if not item or item == '#':
            return None
        p = TreeNode(int(item))
        p.left = self.deserialize_helper(data, itr)
        p.right = self.deserialize_helper(data, itr)
        return p

