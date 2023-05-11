class RadiusVector:

    def __init__(self, *args):
        self.__coords = {}
        if len(args) == 1:
            self.__coords = {_: 0 for _ in range(args[0])}
        else:
            self.__coords = {_: args[_] for _ in range(len(args))}
        self.__dimension = len(self.__coords)

    def __setattr__(self, key, value):
        if key == '_RadiusVector__coords' and isinstance(value, dict):
            object.__setattr__(self, key, value)
        if isinstance(value, (int, float)):
            object.__setattr__(self, key, value)

    def set_coords(self, *args):
        length = min(len(args), self.__dimension)
        for _ in range(length):
            self.__coords[_] = args[_]

    def get_coords(self):
        return tuple(self.__coords.values())

    def __len__(self):
        return self.__dimension

    def __abs__(self):
        return pow(sum([val**2 for val in self.get_coords()]), 1/2)


# TEST-TASK___________________________________
from math import sqrt

vector3D = RadiusVector(3)

# k = str(*[_ for _ in vector3D.__dict__.keys()])
# assert len(vector3D.__dict__[k]) == 3, "ошибка в длине списка из значений"
# assert all(True if _ == 0 else False for _ in vector3D.__dict__[k]), "ошибка, значения должны быть нулями"

vector3D.set_coords(3, -5.6, 8)
# k = str(*[_ for _ in vector3D.__dict__.keys()])
# assert len(vector3D.__dict__[k]) == 3 and \
#        (vector3D.__dict__[k] == [3, -5.6, 8] or
#         vector3D.__dict__[k] == (3, -5.6, 8)), "значения координат неправильные"

assert hasattr(vector3D, 'set_coords') and callable(vector3D.set_coords), "метод set_coords не найден"
assert hasattr(vector3D, 'get_coords') and callable(vector3D.get_coords), "метод get_coords не найден"

assert vector3D.get_coords() == (3, -5.6, 8), "не правильные значения в кортеже"
assert type(vector3D.get_coords()) == tuple, "метод get_coords должен был вернуть кортеж"

vector3D = RadiusVector(3)
vector3D.set_coords(1, 1.1, -8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
# assert len(vector3D.__dict__[k]) == 3 and \
#        (vector3D.__dict__[k] == [1, 1.1, -8] or
#         vector3D.__dict__[k] == (1, 1.1, -8)), "метод set_coords работает не верно"

vector3D.set_coords(1, 2)  # ошибки быть не должно, меняются только первые две координаты
assert vector3D.get_coords() == [1, 2, -8] or vector3D.get_coords() == (1, 2, -8), \
    "метод set_coords изменил не те значения"

res_len = len(vector3D)  # res_len = 3
assert len(vector3D) == 3, "неправильно работает метод len()"

assert abs(vector3D) == sqrt(sum([i * i for i in vector3D.get_coords()])), "метод abs() вернул неверное значение"
print("Правильное решение !")