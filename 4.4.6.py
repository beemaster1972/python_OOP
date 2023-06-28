class Furniture:
    _local_attrib = ()

    def __init__(self, name, weight, *args, **kwargs):
        self._name = name
        self._weight = weight
        self.__dict__.update(zip(self._local_attrib, args))
        self.__dict__.update(kwargs)
        self._next = None

    def __setattr__(self, key, value):
        if key == '_name':
            object.__setattr__(self, key, self.__verify_name(value))
        if key == '_weight':
            object.__setattr__(self, key, self.__verify_weight(value))

    @staticmethod
    def __verify_name(name):
        """ для проверки корректности имени"""
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')
        return name

    @staticmethod
    def __verify_weight(weight):
        """ для проверки корректности веса"""
        if not isinstance(weight, (int, float)) and weight <= 0:
            raise TypeError('вес должен быть положительным числом')
        return weight

    def __repr__(self):
        attrs = [str(el) for key, el in self.__dict__.items()]
        return f'{self.__class__.__name__}({", ".join(attrs)})'

    def get_attrs(self):
        return tuple(self.__dict__.values())


class Closet(Furniture):
    """ для представления шкафов"""
    _local_attrib = ('_tp', '_doors')


class Chair(Furniture):
    """для представления стульев"""
    _local_attrib = ('_height',)


class Table(Furniture):
    """для представления столов"""
    _local_attrib = ('_height', '_square')


if __name__ == '__main__':
    cl = Closet('шкаф-купе', 342.56, True, 3)
    chair = Chair('стул', 14, 55.6)
    tb = Table('стол', 34.5, 75, 10)
    print(tb.get_attrs())
