from abc import ABC, abstractmethod


class StackObj:

    def __init__(self, data):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        if isinstance(value, StackObj) or value is None:
            self._next = value


class StackInterface(ABC):

    @abstractmethod
    def push_back(self, obj):
        """добавление объекта в конец стека"""
        ...

    @abstractmethod
    def pop_back(self):
        """удаление последнего объекта из стека."""
        ...


class Stack(StackInterface):

    def __init__(self):
        self._top = self._tail = None

    def get_prev(self, obj):
        node = StackObj('__fake__')
        node.next = self._top
        while node.next and node.next != obj:
            node = node.next
        return node

    def push_back(self, obj):
        if not self._tail:
            self._top = self._tail = obj
            return True
        if self._top is self._tail:
            self._top.next = obj
        self._tail.next = obj
        self._tail = obj

    def pop_back(self):
        if not self._top:
            return None
        node = self._tail
        self._tail = self.get_prev(node)
        self._tail.next = None
        if self._tail.data == "__fake__":
            self._tail = self._top = None
        return node


if __name__ == '__main__':
    assert issubclass(Stack, StackInterface), "класс Stack должен наследоваться от класса StackInterface"

    try:
        a = StackInterface()
        a.pop_back()
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError при вызове абстрактного метода класса StackInterface"

    st = Stack()
    assert st._top is None, "атрибут _top для пустого стека должен быть равен None"

    obj_top = StackObj("obj")
    st.push_back(obj_top)

    assert st._top == obj_top, "неверное значение атрибута _top"

    obj = StackObj("obj")
    st.push_back(obj)

    n = 0
    h = st._top
    while h:
        assert h._data == "obj", "неверные данные в объектах стека"
        h = h._next
        n += 1

    assert n == 2, "неверное число объектов в стеке (или структура стека нарушена)"

    del_obj = st.pop_back()
    assert del_obj == obj, "метод pop_back возвратил неверный объект"

    del_obj = st.pop_back()
    assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

    assert st._top is None, "неверное значение атрибута _top"
    print("Всё отлично!!!")

