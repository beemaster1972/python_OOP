def integer_params_decorated(method):
    def wrapper(*args, **kwargs):
        conditions = [isinstance(v, int) for i, v in enumerate(args) if i > 0]
        conditions.extend([isinstance(v, int) for v in kwargs.values()])
        if not all(conditions):
            raise TypeError("аргументы должны быть целыми числами")
        return method(*args, **kwargs)

    return wrapper


def integer_params(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


v = Vector(1,2,3,4)
print(v[1])
v[3] = 5
print(v[3])
v['a'] = '1'
v1 = Vector(2.3)