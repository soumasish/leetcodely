from collections import deque
from .graph_errors import GraphError


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

    def get_adjacent_vertices(self, v):
        return self.vertex_map[v].get_adjacent_vertices()

    def get_edge_weight(self, v1, v2):
        pass

    def get_indegree(self, v):
        indegree = 0
        for vertex, neighbors in self.vertex_map.items():
            if v in neighbors:
                indegree += 1
        return indegree

    def breadth_first(self, start=0):
        queue = deque()
        queue.appendleft(start)
        visited = set()
        while len(queue) > 0:
            vertex = queue.pop()
            if vertex not in visited:
                neighbors = vertex.get_adjacent_vertices()
                for neighbor in neighbors:
                    if neighbor not in visited:
                        queue.appendleft(neighbor)

    def depth_first(self, visited, current=0):
        if current in visited:
            return
        visited.add(current)
        for vertex in current.get_adjacent_vertices():
            self.depth_first(visited, vertex)

    def topological_sort(self):
        queue = deque()
        indegree_map = {vertex: vertex.get_indegree for vertex in self.get_adjacent_vertices()}
        for k, v in indegree_map.items():
            if v == 0:
                queue.appendleft(k)
        sorted_list = []
        while len(queue) > 0:
            vertex = queue.pop()
            sorted_list.append(vertex)
            for v in self.get_adjacent_vertices(vertex):
                indegree_map[v] -= 1
                if indegree_map[v] == 0:
                    queue.appendleft(vertex)

    def _build_distance_table(self, source):
        distance_table = {item: (None, None) for item in self.vertex_list}
        distance_table[source] = (0, source)
        queue = deque()
        queue.appendleft(source)
        while len(queue) > 0:
            current_vertex = queue.pop()
            current_distance = distance_table[current_vertex][0]
            for neighbor in self.get_adjacent_vertices(current_vertex):
                if not distance_table[neighbor][0]:
                    distance_table[neighbor] = (1 + current_distance, current_vertex)
                    if len(self.get_adjacent_vertices(neighbor)) > 0:
                        queue.appendleft(neighbor)
        return distance_table

    def shortest_path(self, source, destination):
        distance_table = self._build_distance_table(source)
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

    def get_adjacent_vertices(self):
        return sorted(list(self.neighbors))

    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __eq__(self, other):
        return self.id, self.value == other.id, self.value

    def __hash__(self):
        return hash((self.id, self.value))

    def __repr__(self):
        return '(id:{}, value:{}, neighbors:{}'.format(self.id, self.value, str(self.neighbors))
