
class StringBuilder():

    def __init__(self):
        self.store = []

    def append(self, item):
        self.store.append(item)

    def build(self):
        return ''.join(self.store)
