"""Given a linked list, swap every two adjacent nodes and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed."""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        trigger = True
        prev = curr = head
        while curr:
            curr = curr.next
            if curr and trigger:
                v = curr.val
                curr.val = prev.val
                prev.val = v
            trigger = not trigger
            prev = curr
        return head
