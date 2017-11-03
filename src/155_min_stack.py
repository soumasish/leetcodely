"""Created by sgoswami on 10/7/17."""
"""Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack."""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
        self.min_head = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        p = Node(x)
        q = Node(x)
        p.next = self.head
        p = self.head
        if not self.min_head:
            self.min_head = q
        else:
            curr = self.min_head
            previous = None
            while q.val > curr.val:
                previous = curr
                curr = curr.next
            previous.next = q
            q.next = curr

    def pop(self):
        """
        :rtype: void
        """
        v = self.head.val
        prev, curr = None, self.min_head
        while curr.val != v:
            prev = curr
            curr = curr.next
        prev.next = curr.next
        self.head = self.head.next

    def top(self):
        """
        :rtype: int
        """
        return self.head.val

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_head.val

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None




