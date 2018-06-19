"""Created by sgoswami on 8/22/17."""
"""Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity."""
from .data_types.heap import MinHeap


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(item)


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None
