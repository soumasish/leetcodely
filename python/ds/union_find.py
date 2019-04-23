class UnionFind:
    def __init__(self, items):
        self.items = items
        self.table = {}

    def union(self, p, q):
        self.table.setdefault(p, set()).add(q)
        self.table.setdefault(q, set()).add(p)

    def connected(self, p, q):
        pass
