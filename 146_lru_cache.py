"""Design and implement a data structure for Least Recently Used (LRU) cache.
    It should support the following operations: get and set.

    get(key) - Get the value (will always be positive) of the key
    if the key exists in the cache, otherwise return -1.

    set(key, value) - Set or insert the value if the key is not already present.
    When the cache reached its capacity, it should invalidate the least recently
    used item before inserting a new item."""
from collections import deque


class LRUCache:
    def __init__(self, capacity):
        self.currSize = 0
        self.capacity = capacity
        self.queue = deque([])
        self.store = {}

    def __get__(self, key):
        if key in self.store:
            # The key got used, thus update chronology
            self.queue.remove(key)
            self.queue.appendleft(key)
            return self.store[key]
        else:
            return -1

    def set(self, key, value):
        if key in self.store:
            # The key got used, thus update chronology
            self.queue.remove(key)
            self.queue.appendleft(key)
            self.store[key] = value
        else:
            if self.currSize == self.capacity:
                k = self.queue.pop()
                self.store.pop(k)
                self.currSize -= 1

            self.queue.appendleft(key)
            self.store[key] = value
            self.currSize += 1
