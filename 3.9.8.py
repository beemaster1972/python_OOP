class StackObj:

    def __init__(self, data):
        self.data = data
        self._next = None

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next: StackObj):
        if isinstance(next, StackObj) or next is None:
            self._next = next
        else:
            raise TypeError("Ссылка дложна быть StackObj")


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

    def __check_obj(self, obj):
        if isinstance(obj, StackObj):
            return obj
        else:
            return StackObj(obj)

    def push_back(self, obj: StackObj):
        obj = self.__check_obj(obj)
        last = self[len(self) - 1]
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
        cnt, obj, it = 0, none, iter(self)

        while cnt < item:
            
