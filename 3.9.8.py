class StackObj:

    def __init__(self, data):
        self.data = data
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        if isinstance(next, StackObj) or next is None:
            self._next = next
        else:
            raise TypeError("Ссылка дложна быть StackObj")

    def __repr__(self):
        return f'StackObj({self.data})'


class Stack:
    __slots__ = ('top', '_length', '_index')

    def __init__(self):
        self.top = None
        self._length = 0
        self._index: StackObj = self._get_fake_top()

    def _get_fake_top(self):
        fake_top = StackObj(None)
        fake_top.next = self.top
        return fake_top

    def __len__(self):
        return self._length

    @staticmethod
    def __check_obj(obj):
        if isinstance(obj, StackObj):
            return obj
        else:
            return StackObj(obj)

    def push_back(self, obj: StackObj):
        obj = self.__check_obj(obj)
        if not self.top:
            self.top = obj
        else:
            it = iter(self)
            last = next(it)
            while last.next:
                last = next(it)
            last.next = obj
        self._length += 1

    def push_front(self, obj: StackObj):
        obj = self.__check_obj(obj)
        if not self.top:
            self.top = obj
        else:
            obj.next, self.top = self.top, obj
        self._length += 1

    def __iter__(self):
        self._index = self._get_fake_top()
        return self

    def __next__(self):
        self._index = self._index.next
        if self._index:
            return self._index
        else:
            raise StopIteration

    def __check_index(self, item: int):
        if not isinstance(item, int) or not 0 <= item < self._length:
            raise IndexError(f'Неправильный индекс {item}')

    def __getitem__(self, item):
        self.__check_index(item)
        cnt, it = 0, iter(self)
        obj = next(it)

        while cnt < item:
            obj = next(it)
            cnt += 1
        return obj.data

    def __setitem__(self, key, value):
        self.__check_index(key)
        cnt, it = 0, iter(self)
        obj = next(it)

        while cnt < key:
            obj = next(it)
            cnt += 1
        obj.data = value


if __name__ == '__main__':
    st = Stack()
    st.push_back(StackObj("1"))
    st.push_front(StackObj("2"))
    res1, res2 = st[0], st[1]
    assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

    st[0] = "0"
    assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

    for obj in st:
        assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

    try:
        a = st[3]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    st.push_back("3")
    for el in st:
        print(el.data)
