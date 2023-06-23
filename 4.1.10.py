class Vector:

    def __init__(self, *args):
        self._coords = args

    def get_coords(self):
        return self._coords

    def _get_other(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Действия можно проводить только над объектами типа Vector")
        res = other.get_coords()
        if not len(self._coords) == len(res):
            raise TypeError('размерности векторов не совпадают')
        return res

    def __add__(self, other):
        other = self._get_other(other)
        return Vector(*[val + other[i] for i, val in enumerate(self._coords)])

    def __sub__(self, other):
        other = self._get_other(other)
        return Vector(*[val - other[i] for i, val in enumerate(self._coords)])

    def __repr__(self):
        return f'Vector({", ".join(map(str, self._coords))})'


class VectorInt(Vector):

    def __init__(self, *args):
        if all([isinstance(val, int) for val in args]):
            super().__init__(*args)
        else:
            raise ValueError('координаты должны быть целыми числами')

    def __add__(self, other):
        res = self._get_other(other)
        if any([isinstance(val, float) for val in res]):
            return Vector.__add__(self, other)
        else:
            return VectorInt(*[val + res[i] for i, val in enumerate(self._coords)])

    def __sub__(self, other):
        res = self._get_other(other)
        if any([isinstance(val, float) for val in res]):
            return Vector.__sub__(other)
        else:
            return VectorInt(*[val - res[i] for i, val in enumerate(self._coords)])


if __name__ == '__main__':
    v1 = Vector(1, 2, 3, 4, 5)
    v2 = Vector(6, 7, 8, 9, 0)
    v3 = v1 + v2
    v4 = v2 - v1
    v5 = VectorInt(0, 1, 2, 3, 4, 5)
    print('v5', v5)
    v6 = Vector(10, 11, 12, 13, 14, 15.0)
    print('v6', v6)
    v7 = v5 + v6
    v8 = v6 - v5
    print('v3', v3)
    print('v4', v4)
    print('v7', v7)
    print('v8', v8)
    v1 = Vector(1, 2, 3)
    v2 = Vector(3, 4, 5)

    assert (v1 + v2).get_coords() == (
    4, 6, 8), "операция сложения дала неверные значения (или некорректно работает метод get_coords)"
    assert (v1 - v2).get_coords() == (
    -2, -2, -2), "операция вычитания дала неверные значения (или некорректно работает метод get_coords)"

    v = VectorInt(1, 2, 3, 4)
    assert isinstance(v, Vector), "класс VectorInt должен наследоваться от класса Vector"

    try:
        v = VectorInt(1, 2, 3.4, 4)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError для команды v = VectorInt(1, 2, 3.4, 4)"

    v1 = VectorInt(1, 2, 3, 4)
    v2 = VectorInt(4, 2, 3, 4)
    v3 = Vector(1.0, 2, 3, 4)

    v = v1 + v2
    assert type(
        v) == VectorInt, "при сложении вектором с целочисленными координатами должен формироваться объект класса VectorInt"
    v = v1 + v3
    assert type(
        v) == Vector, "при сложении вектором с вещественными координатами должен формироваться объект класса Vector"
    print('Всё отлично!!!')
