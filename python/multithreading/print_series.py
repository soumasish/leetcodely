"""Print series 010203040506. Using multi-threading 1st thread will print only 0 2nd thread will print
only even numbers and 3rd thread print only odd numbers."""
import threading


class Solution:
    def printSeries(self):
        s = ''
        lock = threading.Lock()
        t1 = SeriesPrinter(0, 0, 0)
        t2 = SeriesPrinter(1, 5, 2)
        t3 = SeriesPrinter(2, 6, 2)
        t1.start()
        t2.start()
        t3.start()
        with lock:
            t1.join()
        with lock:
            t2.join()
        with lock:
            t3.join()


class SeriesPrinter(threading.Thread):
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def run(self, s):
        if self.start != self.stop:
            s += self.start
            self.start += self.step
