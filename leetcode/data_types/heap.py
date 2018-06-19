import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0]

    def __getitem__(self, item):
        return self.heap[item]

    def __len__(self):
        return len(self.heap)


class MaxHeap(MinHeap):
    def push(self, item):
        heapq.heappush(self.heap, Comparator(item))

    def __getitem__(self, i):
        return self.heap[i].val


class Comparator:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __le__(self, other):
        return self.val >= other

    def __gt__(self, other):
        return self.val < other

    def __ge__(self, other):
        return self.val <= other

    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return self.val != other

    def __repr__(self):
        return repr(self.val)


if __name__ == '__main__':
    max_heap = MaxHeap()
    max_heap.push(12)
    max_heap.push(3)
    max_heap.push(17)
    print(max_heap.pop())
