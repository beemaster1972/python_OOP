class ListMath:

    def __init__(self, lst):
        self.lst_math = [el for el in lst if isinstance(el, (int, float))]

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)):
            raise ArithmeticError("Второй операнд должен быть int или float")
        object.__setattr__(self, key, value)

    def __add__(self, other):
        return ListMath([el+other for el in self.lst_math])

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self.lst_math = [el+other for el in self.lst_math]
        return self

    def __sub__(self, other):
        pass