class SellItem:
    _base_attrib = ('name', 'price')
    _local_attrib = ()

    def __init__(self, *args, **kwargs):
        self.__dict__.update(zip(self._base_attrib + self._local_attrib, args))
        self.__dict__.update(kwargs)
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        if isinstance(value, SellItem) or value is None:
            self._next = value

    def __repr__(self):
        attribs = [str(el) for key, el in self.__dict__.items() if key != '_next']
        return f'{self.__class__.__name__}({", ".join(attribs)})'

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, SellItem):
            raise TypeError(f"Неверный аргумент для сравнения {other}")
        conditions = [isinstance(other, self.__class__)] + [other.__dict__.get(key, None) == val for key, val in
                                                            self.__dict__.items()]
        return all(conditions)


class House(SellItem):
    _local_attrib = ('material', 'square')


class Flat(SellItem):
    _local_attrib = ('size', 'rooms')


class Land(SellItem):
    _local_attrib = ('square',)


class Agency:

    def __init__(self, name):
        self.name = name
        self.top: SellItem = None
        self.tail: SellItem = None
        self.__index = SellItem('fake', 0)
        self.__index.next = self.top

    def _check_obj(self, obj):
        if not isinstance(obj, SellItem):
            raise TypeError(f"Не верный объект недвижимости: {obj}")
        return True

    def add_object(self, obj):
        self._check_obj(obj)
        if not self.tail:
            self.top = self.tail = obj
            return True
        self.tail.next = obj
        self.tail = obj

    def remove_object(self, obj):
        self._check_obj(obj)
        if self.top == obj:
            self.top = self.top.next
            return True
        it = iter(self)
        cur_obj = self.top
        prev_obj = SellItem('fake', 0)
        prev_obj.next = self.top
        while cur_obj.next:
            if cur_obj == obj:
                prev_obj.next = cur_obj.next
                break
            prev_obj = cur_obj
            cur_obj = next(it)
        else:
            if self.tail == obj:
                self.tail = prev_obj
                self.tail.next = None

    def get_objects(self):
        return [obj for obj in self]

    def __iter__(self):
        self.__index = SellItem('fake', 0)
        self.__index.next = self.top
        return self

    def __next__(self):
        self.__index = self.__index.next
        if self.__index:
            return self.__index
        raise StopIteration


if __name__ == '__main__':
    ag = Agency("Рога и копыта")
    fl1 = Flat("хрущевка 3-ком", 2_500_000, 62.1, 3)
    ag.add_object(fl1)
    ag.add_object(Flat("квартира, 3к", 10000000, 121.5, 3))
    ag.add_object(Flat("квартира, 2к", 8000000, 74.5, 2))
    ag.add_object(Flat("квартира, 1к", 4000000, 54, 1))
    hs1 = House("дом, крипичный", price=35000000, material="кирпич", square=186.5)
    hs2 = House("дом, деревянный", price=35000000, material="брус", square=206.5)
    ag.add_object(hs1)
    lnd1 = Land("участок под застройку", 3_500_000, 16.48)
    ag.add_object(Land("участок под застройку", 3000000, 6.74))
    print('*' * 30)
    print('Изначальный список недвижимости')
    for obj in ag.get_objects():
        print(obj)
    print('*' * 30)
    ag.remove_object(hs1)
    print(f'Cписок недвижимости после удаления {hs1}')
    for obj in ag.get_objects():
        print(obj)
    print('*' * 30)

    ag.add_object(hs2)
    print(f'Список недвижимости после добавления {hs2}')
    for obj in ag.get_objects():
        print(obj)
    print('*' * 30)

    ag.remove_object(fl1)
    print(f'Список недвижимости после удаления {fl1}')
    for obj in ag.get_objects():
        print(obj)
    print('*' * 30)

    lst_houses = [x for x in ag.get_objects() if isinstance(x, House)]  # выделение списка домов
    lst_flats = [x for x in ag.get_objects() if isinstance(x, Flat)]
    print(lst_houses)
    print(lst_flats)
    ag.add_object(lnd1)
    print(f'Список недвижимости после добавления {lnd1}')
    for obj in ag.get_objects():
        print(obj)
    print('*' * 30)
    ag.remove_object(lnd1)
    print(f'Список недвижимости после удаления {lnd1}')
    for obj in ag.get_objects():
        print(obj)
    print('*' * 30)
