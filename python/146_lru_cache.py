"""Design and implement a data structure for Least Recently Used (LRU) cache.
    It should support the following operations: get and set.

    get(key) - Get the value (will always be positive) of the key
    if the key exists in the cache, otherwise return -1.

    set(key, value) - Set or insert the value if the key is not already present.
    When the cache reached its capacity, it should invalidate the least recently
    used item before inserting a new item."""
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.table = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.table:
            return -1
        value = self.table[key]
        self.table.pop(key)
        self.table[key] = value
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.table:
            self.table.pop(key)
            self.table[key] = value
        else:
            if self.capacity == 0:
                self.table.popitem(last=False)
            else:
                self.capacity -= 1
            self.table[key] = value


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
