# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        store, seen = [], set()
        curr = head
        while curr:
            store.append(curr)
            curr = curr.next
        if len(store) == 1:
            return store[0]
        curr = store[0]
        first, last = 1, -1
        trigger = False
        while True:
            if not trigger:
                if store[last] in seen:
                    break
                seen.add(store[last])
                curr.next = store[last]
                last -= 1
                trigger = True
            else:
                if store[first] in seen:
                    break
                seen.add(store[first])
                curr.next = store[first]
                first += 1
                trigger = False
            curr = curr.next
        curr.next = None
        return store[0]

