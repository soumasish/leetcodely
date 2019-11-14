from collections import deque
import threading


class PubSub:
    def __init__(self, capacity):
        self.queue = deque()
        self.capacity = capacity
        self.lock = threading.Lock()
        self.buffer_not_full = threading.Condition(lock=self.lock)
        self.buffer_not_empty = threading.Condition(lock=self.lock)

    def enque(self, item):
        with self.lock:
            while len(self.queue) == self.capacity:
                self.buffer_not_full.wait()
            self.queue.append(item)
            self.buffer_not_empty.notify_all()

    def deque(self):
        with self.lock:
            while len(self.queue) == 0:
                self.buffer_not_empty.wait()
            item = self.queue.popleft()
            self.buffer_not_full.notify_all()
