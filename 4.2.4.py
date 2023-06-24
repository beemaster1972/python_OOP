class Thing:

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

    def __repr__(self):
        return f'Thing({self.name}, {self.price}, {self.weight})'


class DictShop(dict):

    def __init__(self, things={}):
        if things:
            if not isinstance(things, dict):
                raise TypeError('аргумент должен быть словарем')
            conditions = all(map(self.__check_key, things))
        super().__init__(things)

    def __check_key(self, key):
        if not isinstance(key, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')
        return key

    def __setitem__(self, key, value):
        key = self.__check_key(key)
        super().__setitem__(key, value)


if __name__ == '__main__':
    th_1 = Thing('Лыжи', 11000, 1978.55)
    th_2 = Thing('Книга', 1500, 256)
    dict_things = DictShop()
    dict_things[th_1] = th_1
    dict_things[th_2] = th_2

    for x in dict_things:
        print(x.name)
    try:
        dict_things[1] = th_1  # исключение TypeError
    except TypeError:
        assert True
    else:
        assert False

    try:
        dt1 = DictShop({'t1': th_1, 't2': th_2})
    except TypeError:
        assert True
    else:
        assert False