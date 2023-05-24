class Value:

    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Triangle:
    a = Value()
    b = Value()
    c = Value()

    def __init__(self, *args):
        self.a, self.b, self.c = args
        if not all((args[0] < args[1] + args[2], args[1] < args[0] + args[2], args[2] < args[0] + args[1])):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        if len(self.__dict__) == 3 and value >= sum([x for k, x in self.__dict__.items() if k[-1] != key]):
            raise ValueError(f"с указанной длиной {key[-1]}={value} нельзя образовать треугольник")
        object.__setattr__(self, key, value)

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self, *args, **kwargs):
        p = len(self) / 2
        return pow(p * (p - self.a) * (p - self.b) * (p - self.c), 1 / 2)


egypt_triangle = Triangle(3, 4, 5)
egypt_triangle.a = 8.99999999999
print(len(egypt_triangle), egypt_triangle())
