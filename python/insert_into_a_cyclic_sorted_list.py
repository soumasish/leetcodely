"""Given a node from a cyclic linked list which is sorted in ascending order, write a function to insert a value into
the list such that it remains a cyclic sorted list. The given node can be a reference to any single node in the list,
and may not be necessarily the smallest value in the cyclic list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value.
After the insertion, the cyclic list should remain sorted.

If the list is empty (i.e., given node is null), you should create a new single cyclic list and return the reference to
that single node. Otherwise, you should return the original given node."""
from typing import Optional


# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next


class Solution(object):
    def insert(self, head: Optional[Node], insertVal:int) -> Node:
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        n = Node(insertVal, None)
        if not head:
            n.next = n
            return n
        curr = head
        while True:
            if curr.val <= insertVal <= curr.next.val:
                break
            if curr.val > curr.next.val:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    break
            curr = curr.next
            if curr == head:
                break
        n.next = curr.next
        curr.next = n
        return head
