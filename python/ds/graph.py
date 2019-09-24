from collections import deque
from python.ds.graph_errors import GraphError


class Graph:
    def __init__(self, directed=False):
        self.vertices = 0
        self.directed = directed
        self.vertex_map = {}

    def add_edge(self, v1, v2, weight=1):
        if v1 in self.vertex_map:
            V1 = self.vertex_map[v1]
        else:
            self.vertices += 1
            V1 = Node(self.vertices, v1)
            self.vertex_map[v1] = V1
        if v2 in self.vertex_map:
            V2 = self.vertex_map[v2]
        else:
            self.vertices += 1
            V2 = Node(self.vertices, v2)
            self.vertex_map[v2] = V2
        try:
            V1.add_edge(V2)
            if not self.directed:
                V2.add_edge(V1)
        except ValueError as e:
            raise GraphError(str(e))

    def get_edge_weight(self, v1, v2):
        pass

    def _get_indegree(self, v):
        indegree = 0
        for item in self.vertex_map.values():
            neighbors = item.get_neighbors()
            if v in neighbors:
                indegree += 1
        return indegree

    def breadth_first(self, start=1):
        p = None
        if not start:
            p = self.vertex_map[1]
        else:
            try:
                p = self.vertex_map[start]
            except KeyError:
                raise GraphError("Not a valid key for this graph")
        queue = deque()
        queue.appendleft(p)
        visited = set()
        while len(queue) > 0:
            vertex = queue.pop()
            if vertex not in visited:
                neighbors = vertex.get_neighbors()
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.appendleft(neighbor)

    def depth_first(self, start=0):
        p = None
        if not start:
            p = self.vertex_map[1]
        else:
            try:
                p = self.vertex_map[start]
            except KeyError:
                raise GraphError('Not a valid key for this graph')
        visited = set()

        def helper(node):
            if node in visited:
                return
            visited.add(node)
            for vertex in node.get_neighbors():
                helper(vertex)
        helper(p)

    def topological_sort(self):
        queue = deque()
        indegree_map = {vertex: self._get_indegree(vertex) for vertex in self.vertex_map.values()}

        for k, v in indegree_map.items():
            if v == 0:
                queue.appendleft(k)
        result = []
        while len(queue) > 0:
            vertex = queue.pop()
            result.append(vertex)
            for neighbor in vertex.get_neighbors():
                indegree_map[neighbor] -= 1
                if indegree_map[neighbor] == 0:
                    queue.appendleft(neighbor)
        return result

    def build_distance_table(self, source):
        _source = self.vertex_map[source]
        distance_table = {value: [None, None] for value in self.vertex_map.values()}
        distance_table[_source] = [0, _source]
        queue = deque()
        queue.appendleft(_source)
        while len(queue) > 0:
            current_vertex = queue.pop()
            current_distance = distance_table[current_vertex][0]
            for neighbor in current_vertex.get_neighbors():
                if not distance_table[neighbor][0]:
                    distance_table[neighbor] = [1 + current_distance, current_vertex]
                    if len(neighbor.get_neighbors()) > 0:
                        queue.appendleft(neighbor)
        return distance_table

    def shortest_path(self, source, destination):
        distance_table = self.build_distance_table(source)
        path = [destination]
        previous_vertex = distance_table[destination][1]

        while previous_vertex and previous_vertex is not source:
            path = [previous_vertex] + path
            previous_vertex = distance_table[previous_vertex][1]

        if not previous_vertex:
            return []
        else:
            path = [source] + path
            return path

    def get_all_nodes(self):
        return [(key.id, key.value) for key, value in self.vertex_map.items()]

    def __str__(self):
        s = "{ "
        for k, v in self.vertex_map.items():
            s += str(k)
            s += ":"
            s += str(v)
            s += '\n'
        s += " }"
        return s

    def __len__(self):
        return self.vertices


class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.neighbors = set()

    def add_edge(self, v):
        if v.id == self.id:
            raise ValueError("Vertex cannot be added to itself!")
        self.neighbors.add(v)

    def get_neighbors(self):
        return sorted(list(self.neighbors))

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash((self.id, self.value))

    def __repr__(self):
        return '(id:{}, value:{}, neighbors: {} )'.format(self.id, self.value, str(self.neighbors))


if __name__ == '__main__':
    graph = Graph(directed=True)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(3, 7)
    # graph.breadth_first()
    # print(graph)
    # graph.depth_first(1)
    # print(graph)

    print(graph.topological_sort())
