"""Created by sgoswami on 9/13/17."""
"""Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, 
when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key 
would be evicted."""
import heapq

class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.store = {}
        self.usage = heapq([])
        self.capacity = capacity
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.store:
            return self.store[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.store[key] = value
        heapq.heappush(self.usage, KeyUsage(key, 1))
        self.size += 1

class KeyUsage:
    def __init__(self, key, usage):
        self.key = key
        self.usage = usage

    def update_usage(self, key):
        self.usage += 1
