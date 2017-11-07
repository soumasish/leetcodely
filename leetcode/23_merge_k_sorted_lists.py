"""Created by sgoswami on 8/22/17."""
"""Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity."""
import heapq

# Definition for singly-linked list.
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
        queue = []
        for node in lists:
            while node:
                heapq.heappush(queue, node.val)
                node = node.next
        if len(queue) == 0:
            return None
        val = heapq.heappop(queue)
        head = previous = ListNode(val)
        while True:
            try:
                v = heapq.heappop(queue)
            except IndexError:
                break
            curr = ListNode(v)
            previous.next = curr
            previous = curr
        return head

