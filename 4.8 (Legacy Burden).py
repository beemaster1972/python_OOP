class Vertex:
    __slots__ = ("_links",)

    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links


class Link:
    __slots__ = ('_v1', '_v2', '_dist')

    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

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
