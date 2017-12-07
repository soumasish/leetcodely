class stack:
    def __init__(self):
        self.store = []
        self.size = 0

    def push(self, item):
        self.store.append(item)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise ValueError('Popping off an empty stack!')
        self.store.pop()
        self.size -= 1

    def peek(self):
        return self.store[-1]