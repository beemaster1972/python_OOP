class Thing:
    __slots__ = ('_name', '_weight', '__next')

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.__next = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if isinstance(weight, (int, float)) and weight >= 0:
            self._weight = weight

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if isinstance(next, Thing) or next is None:
            self.__next = next

    def __repr__(self):
        return f'Thing: {self.name} вес: {self.weight} --> {self.next.name if self.next else "None"}'


class Bag:
    __slots__ = ('__max_weight', 'head', 'tail', '__weight')

    def __init__(self, max_weight):
        self.__max_weight = max_weight
        self.head = self.tail = None
        self.__weight = 0

    @property
    def weight(self):
        return self.__weight

    @property
    def max_weight(self):
        return self.__max_weight

    def add_thing(self, thing: Thing):
        if self.__weight + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        if not self.tail:
            self.head = self.tail = thing
            self.__weight = thing.weight
        else:
            self.tail.next = thing
            self.tail = thing
            self.__weight += thing.weight

    def __get_by_index(self, idx: int):
        cur = self.head
        prev = None
        cnt = 0
        while cnt < idx:
            prev = cur
            if cur.next:
                cur = cur.next
            else:
                break
            cnt += 1
        if cnt != idx:
            raise IndexError(f"Неправильный индекс {idx}")
        return cur, prev

    def __getitem__(self, item):
        things = self.__get_by_index(item)
        return things[0]

    def __setitem__(self, key, value):
        things = self.__get_by_index(key)
        if isinstance(value, Thing):
            cur, prev = things
            if self.weight + value.weight - cur.weight > self.max_weight:
                raise ValueError('превышен суммарный вес предметов')
            if prev:
                prev.next = value
            else:
                self.head = value
            if not cur.next:
                self.tail = value
            self.__weight -= cur.weight
            self.__weight += value.weight
            value.next = cur.next

    def __delitem__(self, key):
        things = self.__get_by_index(key)
        cur, prev = things
        if prev:
            prev.next = cur.next
        else:
            self.head = cur.next
        if not cur.next:
            self.tail = prev
        self.__weight -= cur.weight

    def __repr__(self):
        return f"Bag: {self.weight} из {self.max_weight}"


if __name__ == '__main__':

    b = Bag(700)
    b.add_thing(Thing('книга', 100))
    b.add_thing(Thing('носки', 200))

    try:
        b.add_thing(Thing('рубашка', 500))
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    assert b[0].name == 'книга' and b[
        0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

    t = Thing('Python', 20)
    b[1] = t
    assert b[1].name == 'Python' and b[
        1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

    del b[0]
    assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

    try:
        t = b[2]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    b = Bag(700)
    b.add_thing(Thing('книга', 100))
    b.add_thing(Thing('носки', 200))

    b[0] = Thing('рубашка', 500)

    try:
        b[0] = Thing('рубашка', 800)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"

    print("Всё отлично!!")