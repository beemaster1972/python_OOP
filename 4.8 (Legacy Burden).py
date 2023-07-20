import numpy as np
import math

class Vertex:
    __slots__ = ("_links", "_id")
    ID = -1

    def __init__(self):
        self._links = []
        Vertex.ID += 1
        self._id = Vertex.ID

    @property
    def links(self):
        return self._links

    def add_link(self, link):
        if link not in self._links:
            self._links.append(link)

    def __repr__(self):
        return str(self._id)


class Link:
    __slots__ = ('_v1', '_v2', '_dist')

    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1
        self._v1.add_link(self)
        self._v2.add_link(self)

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value

    def __hash__(self):
        return hash(hash(self.v1) + hash(self.v2))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __repr__(self):
        return f'{self.v1}<-->{self.v2}'


class LinkedGraph:

    def __init__(self):
        self._links = {}
        self._vertex = []
        self._adjacency_matrix = None

    @property
    def vertex(self):
        return self._vertex

    @property
    def links(self):
        return self._links.values()

    def add_vertex(self, v):
        if type(v) == Vertex and v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if type(link) == Link and link not in self._links:
            self._links[link] = link
            if link.v1 not in self._vertex:
                self.add_vertex(link.v1)
            if link.v2 not in self._vertex:
                self.add_vertex(link.v2)

    def get_link(self, v1, v2):
        return self._links.get(hash(hash(v1) + hash(v2)), None)

    def find_path(self, start_v, stop_v):
        if not self._adjacency_matrix:
            self._adjacency_matrix = AdjacencyMatrix(self)


class AdjacencyMatrix:

    def __init__(self, graph: LinkedGraph):
        N = len(graph.vertex)
        self._adj_matrix = np.zeros((N, N))
        for l in graph.links:
            self._adj_matrix[l.v1._id][l.v2._id] = l.dist
            self._adj_matrix[l.v2._id][l.v1._id] = l.dist
        for i, row in enumerate(self._adj_matrix):
            for j, col in enumerate(row):
                if j == i:
                    continue
                if not col:
                    self._adj_matrix[i][j] = math.inf
        print(self._adj_matrix)


if __name__ == '__main__':
    map_graph = LinkedGraph()

    v1 = Vertex()
    v2 = Vertex()
    v3 = Vertex()
    v4 = Vertex()
    v5 = Vertex()
    v6 = Vertex()
    v7 = Vertex()

    map_graph.add_link(Link(v1, v2))
    map_graph.add_link(Link(v2, v3))
    map_graph.add_link(Link(v1, v3))

    map_graph.add_link(Link(v4, v5))
    map_graph.add_link(Link(v6, v7))

    map_graph.add_link(Link(v2, v7))
    map_graph.add_link(Link(v3, v4))
    map_graph.add_link(Link(v5, v6))

    for val in map_graph.links:
        print(f'{val}')
    print(len(map_graph.links))  # 8 связей

    print(len(map_graph.vertex))  # 7 вершин
    path = map_graph.find_path(v1, v6)
