"""Created by sgoswami on 9/13/17."""

"""Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, 
when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key 
would be evicted."""

from collections import defaultdict


class Node:
    def __init__(self, key, value, freq=1):
        self.key = key
        self.value = value
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq

class LFUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.value_map = {}  # Maps key to Node
        self.freq_map = defaultdict(list)  # Maps frequency to list of Nodes
        self.min_freq = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.value_map:
            return -1

        node = self.value_map[key]
        self._update(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return

        if key in self.value_map:
            node = self.value_map[key]
            node.value = value
            self._update(node)
        else:
            if len(self.value_map) == self.capacity:
                # Remove the least frequently used node
                least_freq_nodes = self.freq_map[self.min_freq]
                lfu_node = least_freq_nodes.pop(0)
                del self.value_map[lfu_node.key]

            new_node = Node(key, value)
            self.value_map[key] = new_node
            self.freq_map[1].append(new_node)
            self.min_freq = 1

    def _update(self, node):
        # Remove the node from its current frequency list
        freq_nodes = self.freq_map[node.freq]
        freq_nodes.remove(node)
        if not freq_nodes and self.min_freq == node.freq:
            self.min_freq += 1

        # Increment the node's frequency and add it to the new frequency list
        node.freq += 1
        self.freq_map[node.freq].append(node)






