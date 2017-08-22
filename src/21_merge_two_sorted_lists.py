"""Created by sgoswami on 8/8/17."""
"""Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the 
nodes of the first two lists."""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
        curr.next = l1 or l2
        print(dummy.next.val)
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(10)
    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)
    l2.next.next.next = ListNode(11)

    solution = Solution()
    l3 = solution.mergeTwoLists(l1, l2)

    while l3:
        print(l3.val, end=' ')
        l3 = l3.next
