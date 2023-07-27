import math


class Vertex:
    __slots__ = ("_links", "_id")
    __ID = 0

    def __init__(self):
        self._links = []
        Vertex.__ID += 1
        self._id = Vertex.__ID

    @property
    def id(self):
        return self._id

    @property
    def links(self):
        return self._links

    def add_link(self, link):
        if link not in self._links:
            self._links.append(link)

    def __repr__(self):
        return f'V[{self._id}]'


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

    def __eq__(self, other):
        conditions = [self.v1 in (other.v1, other.v2), self.v2 in (other.v1, other.v2)]
        return all(conditions)

    def __repr__(self):
        return f'{self.v1}<-{self._dist}->{self.v2}'


class LinkedGraph:

    def __init__(self):
        self._links = []
        self._vertex = []

    @property
    def vertex(self):
        return self._vertex

    @property
    def links(self):
        return self._links

    def add_vertex(self, v):
        if isinstance(v, Vertex) and v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if isinstance(link, Link) and link not in self._links:
            self._links.append(link)
            if link.v1 not in self._vertex:
                self.add_vertex(link.v1)
            if link.v2 not in self._vertex:
                self.add_vertex(link.v2)
        else:
            print(f'связь {link} уже есть {self._links[self._links.index(link)]}')

    def get_link(self, v1, v2):
        return list(filter(lambda x: x == Link(v1, v2), self._links))[0]

    def find_path(self, start_v, stop_v):
        find_path_res = DijkstraAlgorithm(self)
        route = find_path_res(start_v, stop_v)
        link_list = [self.get_link(route[i], route[i + 1]) for i in range(len(route) - 1)]
        return route, link_list


class DijkstraAlgorithm:

    def __init__(self, graph: LinkedGraph):
        self.graph = graph
        self.table_row = {v: math.inf for v in self.graph.vertex}  # строка смежности
        self.viewed_vertices = set()  # множество просмотренных вершин
        self.route = {v: None for v in self.graph.vertex}  # маршрут

    def get_min_weight(self):
        index_min = -1
        min_weight = math.inf
        for v, weight in self.table_row.items():
            if weight < min_weight and v not in self.viewed_vertices:
                min_weight = weight
                index_min = v
        return index_min

    @staticmethod
    def get_links(v):
        """Функция-генератор для получения кортежа(вершина, связь)
           v - объект Vertex """
        for link in v.links:
            if link.v1 == v:
                yield link.v2, link
            elif link.v2 == v:
                yield link.v1, link

    def find_path(self, start_v: Vertex, stop_v: Vertex):
        vertice = start_v  # стартовая вершина
        self.viewed_vertices.add(vertice)  # добавляем в просмотренные вершины стартовую
        self.table_row[vertice] = 0  # нулевой вес для стартовой вершины

        while vertice != -1:  # цикл, пока не просмотрим все вершины
            for v, link in self.get_links(vertice):  # перебираем все связанные вершины с вершиной vertice
                if v not in self.viewed_vertices:  # если вершина еще не просмотрена
                    w = self.table_row[vertice] + link.dist  # итоговый вес до вершины vertice
                    if w < self.table_row[v]:  # если вычисленный вес меньше текущего
                        self.table_row[v] = w  # записываем в строку смежности
                        self.route[v] = vertice  # связываем вершину v с вершиной vertice

            vertice = self.get_min_weight()  # выбираем следующую вершину с наименьшим весом
            if vertice != -1:  # выбрана очередная вершина
                self.viewed_vertices.add(vertice)  # добавляем новую вершину в рассмотрение

        # формируем оптимальный маршрут:
        vertice = start_v
        end = stop_v
        points = [end]  # строим маршрут с конечной точки
        while end != vertice:
            end = self.route[points[-1]]  # получаем следующую вершину
            points.append(end)  # добавляем в список точек
        return points[::-1]  # возвращаем список точек маршрута с начальной по конечную

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
    print(path[0])
    print(path[1])

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
    map_metro.add_link(LinkMetro(v7, v2, 5))
    map_metro.add_link(LinkMetro(v3, v4, 3))
    map_metro.add_link(LinkMetro(v5, v6, 3))

    print(len(map_metro._links))
    print(len(map_metro._vertex))
    path = map_metro.find_path(v1, v6)  # от сретенского бульвара до китай-город 1
    print(path[0])  # [Сретенский бульвар, Тургеневская, Китай-город 2, Китай-город 1]
    print(path[1])
    print(sum([x.dist for x in path[1]]))
