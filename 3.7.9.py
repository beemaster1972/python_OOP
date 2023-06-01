class Vector:

    def __init__(self, *args):
        self.__coords = list(args)

    def __setattr__(self, key, value):
        for arg in value:
            if not isinstance(arg, (int, float)):
                raise TypeError(f'Invalid type {type(arg)} for coordinates ')
        object.__setattr__(self, key, value)

    def __get_other(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ArithmeticError('размерности векторов не совпадают')
            return other.__coords
        else:
            return [other]*len(self)

    def __len__(self):
        return len(self.__coords)

    def __ne__(self, other):
        try:
            return len(self) != len(other) or all([self.__coords[i] != other.__coords[i] for i in range(len(self))])
        except TypeError:
            return True

    def __eq__(self, other):
        try:
            return len(self) == len(other) and sum(self.__coords) == sum(other.__coords)
        except TypeError:
            return False

    def __add__(self, other):
        other = self.__get_other(other)
        res = [self.__coords[i]+other[i] for i in range(len(self))]
        return Vector(*res)

v1 = Vector()
v2 = Vector()
print(v1 == v2, v1 != v2)