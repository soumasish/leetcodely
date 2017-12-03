from threading import Timer

class Uniqify:
    def __init__(self, k):
        self.string_map = {}
        self.timer = Timer(k, self.print)

    def add(self, item):
        if item not in self.string_map:
            self.string_map[item] = 1

    def print(self):
        for k, v in self.string_map.items():
            print(k)
        self.timer = {}





class Topology:
    pass


class Spout:
    pass


class Bolt:
    pass



