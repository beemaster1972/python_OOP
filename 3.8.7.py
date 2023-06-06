class RadiusVector:
    __slots__ = '_coords'

    def __init__(self, *args):
        self.coords = list(args)

    @property
    def coords(self):
        return self._coords

    @coords.setter
    def coords(self, coords):
        self.__check_coords(coords)
        self._coords = coords

    @staticmethod
    def __check_coords(coords):
        if isinstance(coords, (list, tuple)):
            if not all([isinstance(c, (int, float)) for c in coords]):
                raise ValueError("Координаты должны быть целым или вещественным числом")
        elif not isinstance(coords,(int, float)):
            raise ValueError("Координаты должны быть целым или вещественным числом")

    @staticmethod
    def __check_index(item):
        if isinstance(item, (int, slice)):
            is_slice = isinstance(item, slice)
            return item, is_slice
        raise IndexError(f"Неправильный индекс {item}")

    def __getitem__(self, item):
        item, is_slice = self.__check_index(item)
        return tuple(self.coords[item]) if is_slice else self._coords[item]

    def __setitem__(self, key, value):
        key, is_slice = self.__check_index(key)
        self.__check_coords(value)
        self.coords[key] = value

    def __repr__(self):
        return '[' + ' '.join(map(str, self.coords)) + ']'


if __name__ == '__main__':
    v = RadiusVector(1, 2, 3, 4, 5, 6)
    print(v)
    print(v[1:4], v[0])
    v[:3] = [0, 1, 2]
    v[3] = 3
    print(v)
