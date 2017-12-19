"""Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window."""


class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.curr_total = 0
        self.size = size
        self.queue = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) == self.size:
            v = self.queue.pop(0)
            self.curr_total -= v
            self.queue.append(val)
            self.curr_total += val
            return self.curr_total/self.size
        else:
            self.queue.append(val)
            self.curr_total += val
            return self.curr_total/len(self.queue)


if __name__ == '__main__':
    m = MovingAverage(3)
    print(m.next(1))
    print(m.next(10))
    print(m.next(3))
    print(m.next(5))


