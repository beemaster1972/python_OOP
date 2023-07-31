class Box:

    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._things = []
        self.__cur_weight = 0
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def max_weight(self):
        return self._max_weight
    
    @max_weight.setter
    def max_weight(self, value):
        self._max_weight = value

    def add_thing(self, obj):
        if type(obj) not in (list, tuple):
            raise TypeError("Параметр должен быть списком или кортежем")
        if self.__cur_weight + obj[1] <= self._max_weight:
            self._things.append(obj)
            self.__cur_weight += obj[1]
        else:
            raise ValueError('превышен суммарный вес вещей')


class BoxDefender:

    def __init__(self, box: Box):
        self.__box = box

    def __enter__(self):
        self.__temp = self.__box._things[:]
        return self.__box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.__box._things[:] = self.__temp
        return False


if __name__ == '__main__':
    b = Box('name', 2000)
    assert b._name == 'name' and b._max_weight == 2000, "неверные значения атрибутов объекта класса Box"

    b.add_thing(("1", 100))
    b.add_thing(("2", 200))

    try:
        with BoxDefender(b) as bb:
            bb.add_thing(("3", 1000))
            bb.add_thing(("4", 1900))
    except ValueError:
        assert len(b._things) == 2

    else:
        assert False, "не сгенерировалось исключение ValueError"

    try:
        with BoxDefender(b) as bb:
            bb.add_thing(("3", 100))
    except ValueError:
        assert False, "возникло исключение ValueError, хотя, его не должно было быть"
    else:
        assert len(b._things) == 3, "неверное число элементов в списке _things"

    print("Всё отлично!!!")
    