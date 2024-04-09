"""Design and implement a data structure for Least Recently Used (LRU) cache.
    It should support the following operations: get and set.

    get(key) - Get the value (will always be positive) of the key
    if the key exists in the cache, otherwise return -1.

    set(key, value) - Set or insert the value if the key is not already present.
    When the cache reached its capacity, it should invalidate the least recently
    used item before inserting a new item."""
from collections import deque


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.table = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def _remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def _add_to_head(self, node):
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node

    def _update(self, node):
        self._remove(node)
        self._add_to_head(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.table:
            node = self.table[key]
            self._update(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.table:
            node = self.table[key]
            node.value = value
            self._update(node)
        else:
            node = Node(key, value)
            self.table[key] = node
            if len(self.table) > self.capacity:
                # Remove the least recently used item
                del self.table[self.tail.key]
                self._remove(self.tail)
            self._add_to_head(node)


if __name__ == '__main__':
    cache = LRUCache(2)

    print(cache.get(2))
    cache.put(2, 6)
    print(cache.get(1))  # returns 1
    cache.put(1, 5)  # evicts key 2
    cache.put(1, 2)  # evicts key 1
    print(cache.get(1))  # returns - 1(not found)
    print(cache.get(2))  # returns 3

"""On get update order
On put -> if key already present update order
If key new pop the least recently used and update key"""
