class Vector:

    def __init__(self, *args):
        self.__coords = args

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
            return [other] * len(self)

    def __get_result(self, operation, other):
        return tuple((eval(f'{x} {operation} {y}') for x, y in zip(self.__coords, other)))

    def __str__(self):
        return ' '.join(tuple(map(str, self.__coords)))

    def __len__(self):
        return len(self.__coords)

    def __ne__(self, other):
        other = self.__get_other(other)
        try:
            return len(self) != len(other) or any([x != y for x, y in zip(self.__coords, other)])
        except TypeError:
            return False

    def __eq__(self, other):
        other = self.__get_other(other)
        try:
            return len(self) == len(other) and all([x == y for x, y in zip(self.__coords, other)])
        except TypeError:
            return False

    def __add__(self, other):
        other = self.__get_other(other)
        res = self.__get_result('+', other)
        return Vector(*res)

    def __iadd__(self, other):
        other = self.__get_other(other)
        self.__coords = self.__get_result('+', other)
        return self
    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = self.__get_other(other)
        res = self.__get_result('-', other)
        return Vector(*res)

    def __isub__(self, other):
        other = self.__get_other(other)
        self.__coords = self.__get_result('-', other)
        return self

    def __mul__(self, other):
        other = self.__get_other(other)
        res = self.__get_result('*', other)
        return Vector(*res)


if __name__ == '__main__':
    v1 = Vector(1, 2, 3, 4)
    v2 = Vector(1, 2, 3, 4)
    v3 = Vector(0.5, 1, 2, 3)
    v4 = v1 + v3
    v5 = v1 - v3
    v6 = v1 * v3
    v1 += v6
    v2 -= v3
    print(v1 == v2, v1 != v2, v1, v2, v3, v4, v5, v6, sep='\n')
    v1 += 10
    v2 -= 5

# TEST-TASK___________________________________
v1 = Vector(1, 1, 1, 1)
v2 = Vector(1, 2, 3, 4)
# При реализации бинарных операторов +, -, *
# следует создавать новые объекты класса Vector с новыми (вычисленными) координатами.
v3 = v1 + v2
assert list(*v3.__dict__.values()) == [2, 3, 4, 5], \
    "ошибка предпологается что в объекте будет только 1 локальный атрибут с координатами"
assert id(v3) != id(v1) and id(v3) != id(v2), "ошибка, при + должен создаваться новый объект"

v4 = v1 - v2
assert list(*v4.__dict__.values()) == [0, -1, -2, -3], \
    "ошибка предпологается что в объекте будет только 1 локальный атрибут с координатами"
assert id(v4) != id(v1) and id(v4) != id(v2), "ошибка, при - должен создаваться новый объект"

v5 = v1 * v2
assert list(*v4.__dict__.values()) == [0, -1, -2, -3], \
    "ошибка предпологается что в объекте будет только 1 локальный атрибут с координатами"
assert id(v5) != id(v1) and id(v5) != id(v2), "ошибка, при * должен создаваться новый объект"

# При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.
temp = id(v1)
v1 += 10
assert id(v1) == temp and list(*v1.__dict__.values()) == [11, 11, 11, 11], \
    "ошибка, при v1 += 10 объект должен оставаться прежним, не нужно создавать новый объект"

v1 += v5
assert id(v1) == temp and list(*v1.__dict__.values()) == [12, 13, 14, 15], \
    "ошибка, при v1 += v5 объект должен оставаться прежним, не нужно создавать новый объект"

v1 -= v5
assert id(v1) == temp and list(*v1.__dict__.values()) == [11, 11, 11, 11], \
    "ошибка, при v1 -= v5 объект должен оставаться прежним, не нужно создавать новый объект"

v1 -= 10
assert id(v1) == temp and list(*v1.__dict__.values()) == [1, 1, 1, 1], \
    "ошибка, при v1 -= 10 объект должен оставаться прежним, не нужно создавать новый объект"

v11 = Vector(1, 1, 1, 1)
v22 = Vector(1, 1, 1, 1)
ans = v11 == v22  # True
assert ans, f"ошибка, {v11} == {v22} # {ans}, если соответствующие координаты векторов равны"
ans1 = v1 != v2  # True
assert ans1, f"ошибка, {v1} != {v2} # {ans1}, если хотя бы одна пара координат векторов не совпадает"

# Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, *
# должно генерироваться исключение командой:
# raise ArithmeticError('размерности векторов не совпадают')
x1 = Vector(1, 1, 1)
x2 = Vector(1, 1, 1, 1)
try:
    x1 + x2
except ArithmeticError:
    assert True
else:
    assert False, "ошибка, не сгенерировалась ошибка ArithmeticError при операции x1 + x2"

try:
    x1 - x2
except ArithmeticError:
    assert True
else:
    assert False, "ошибка, не сгенерировалась ошибка ArithmeticError при операции x1 - x2"

try:
    x1 * x2
except ArithmeticError:
    assert True
else:
    assert False, "ошибка, не сгенерировалась ошибка ArithmeticError при операции x1 * x2"

print("Правилно, так держать !")
