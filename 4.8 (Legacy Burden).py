import math


class Vertex:
    __slots__ = ("_links", "_id")
    ID = -1

    def __init__(self):
        self._links = {}
        Vertex.ID += 1
        self._id = Vertex.ID

    @property
    def id(self):
        return self._id

    @property
    def links(self):
        return list(self._links.values())

    def add_link(self, link):
        if link not in self._links:
            self._links[link] = link

    def __repr__(self):
        return f'V[{self._id + 1}]'


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
        return hash(hash(self.v1) ^ hash(self.v2))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __repr__(self):
        return f'{self.v1}<-{self._dist}->{self.v2}'


class LinkedGraph:

    def __init__(self):
        self._links = {}
        self._vertex = []

    @property
    def vertex(self):
        return self._vertex

    @property
    def links(self):
        return self._links.values()

    def add_vertex(self, v):
        if isinstance(v, Vertex) and v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if isinstance(link, Link) and link not in self._links:
            self._links[link] = link
            if link.v1 not in self._vertex:
                self.add_vertex(link.v1)
            if link.v2 not in self._vertex:
                self.add_vertex(link.v2)
        else:
            print(f'{link} {link not in self._links}')

    def get_link(self, v1, v2):
        return self._links.get(hash(hash(v1) ^ hash(v2)), None)

    def find_path(self, start_v, stop_v):
        find_path_res = DijkstraAlgorithm(self)
        route = find_path_res(start_v, stop_v)
        vertex_list = [v for v in self._vertex if v.id in route]
        link_list = [self.get_link(vertex_list[i], vertex_list[i + 1]) for i in range(len(vertex_list) - 1)]
        return vertex_list, link_list


class AdjacencyMatrix:

    def __init__(self, graph: LinkedGraph):
        N = len(graph.vertex)
        # заполняем матрицу смежности бесконечностями, а по главной диагонали нулями
        self.matrix = [[math.inf if i != j else 0 for j in range(N)] for i in range(N)]
        # для всех рёбер из графа заполняем веса
        for l in graph.links:
            self.matrix[l.v1.id][l.v2.id] = l.dist
            self.matrix[l.v2.id][l.v1.id] = l.dist

    def __repr__(self):
        return "\n".join([str(row) for row in self.matrix])

    def __len__(self):
        return len(self.matrix)


class DijkstraAlgorithm:

    def __init__(self, graph: LinkedGraph):
        self.graph = graph
        self.adjacency_matrix = AdjacencyMatrix(self.graph)  # матрица смежности
        self.table_row = [math.inf] * len(self.adjacency_matrix)  # строка смежности
        self.viewed_vertices = set()
        self.route = [0] * len(self.adjacency_matrix)

    def get_min_weight(self):
        index_min = -1
        min_weight = math.inf
        for i, weight in enumerate(self.table_row):
            if weight < min_weight and i not in self.viewed_vertices:
                min_weight = weight
                index_min = i
        return index_min

    def find_path(self, start_v: Vertex, stop_v: Vertex):
        vertice = start_v.id  # стартовая вершина
        self.viewed_vertices.add(vertice)  # добавляем в просмотренные вершины стартовую
        self.table_row[vertice] = 0  # нулевой вес для стартовой вершины

        while vertice != -1:  # цикл, пока не просмотрим все вершины
            for j, dw in enumerate(
                    self.adjacency_matrix.matrix[vertice]):  # перебираем все связанные вершины с вершиной vertice
                if j not in self.viewed_vertices:  # если вершина еще не просмотрена
                    w = self.table_row[vertice] + dw  # итоговый вес до вершины j
                    if w < self.table_row[j]:  # если вычисленный вес меньше текущего
                        self.table_row[j] = w  # записываем в строку смежности
                        self.route[j] = vertice  # связываем вершину j с вершиной v

            vertice = self.get_min_weight()  # выбираем следующий узел с наименьшим весом
            if vertice >= 0:  # выбрана очередная вершина
                self.viewed_vertices.add(vertice)  # добавляем новую вершину в рассмотрение

        # формирование оптимального маршрута:
        vertice = start_v.id
        end = stop_v.id
        point = [end]
        while end != vertice:
            end = self.route[point[-1]]
            point.append(end)
        return point[::-1]

    def __call__(self, start_v: Vertex, stop_v: Vertex):
        return self.find_path(start_v, stop_v)


class Station(Vertex):

    def __init__(self, name):
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return self.name


class LinkMetro(Link):

    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist


if __name__ == '__main__':
    # map_graph = LinkedGraph()
    #
    # v1 = Vertex()
    # v2 = Vertex()
    # v3 = Vertex()
    # v4 = Vertex()
    # v5 = Vertex()
    # v6 = Vertex()
    # v7 = Vertex()
    #
    # map_graph.add_link(Link(v1, v2))
    # map_graph.add_link(Link(v2, v3))
    # map_graph.add_link(Link(v1, v3))
    #
    # map_graph.add_link(Link(v4, v5))
    # map_graph.add_link(Link(v6, v7))
    #
    # map_graph.add_link(Link(v2, v7))
    # map_graph.add_link(Link(v3, v4))
    # map_graph.add_link(Link(v5, v6))
    #
    # for val in map_graph.links:
    #     print(f'{val}')
    # print(len(map_graph.links))  # 8 связей
    #
    # print(len(map_graph.vertex))  # 7 вершин
    # path = map_graph.find_path(v1, v6)
    # print(path[0])
    # print(path[1])

    map_metro = LinkedGraph()
    v1 = Station("Сретенский бульвар")
    v2 = Station("Тургеневская")
    v3 = Station("Чистые пруды")
    v4 = Station("Лубянка")
    v5 = Station("Кузнецкий мост")
    v6 = Station("Китай-город 1")
    v7 = Station("Китай-город 2")

    map_metro.add_link(LinkMetro(v1, v2, 1))
    map_metro.add_link(LinkMetro(v2, v3, 1))
    map_metro.add_link(LinkMetro(v1, v3, 1))

    map_metro.add_link(LinkMetro(v4, v5, 1))
    map_metro.add_link(LinkMetro(v6, v7, 1))

    map_metro.add_link(LinkMetro(v2, v7, 5))
    map_metro.add_link(LinkMetro(v3, v4, 3))
    map_metro.add_link(LinkMetro(v5, v6, 3))

    print(len(map_metro._links))
    print(len(map_metro._vertex))
    path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
    print(path[0])  # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
    print(path[1])
    print(sum([x.dist for x in path[1]]))
