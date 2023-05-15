class StackObj:

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


class Stack:

    def __init__(self):
        self.top = None
        self.tail = None

    def __get_penult(self):
        obj = self.top
        while obj.next:
            obj = obj.next
        return obj

    def push_back(self, obj: StackObj):
        if not self.top:
            self.top = self.tail = obj
        else:
            self.tail.next = obj
            self.tail = obj
        return self

    def pop_back(self):
        obj = self.__get_penult()
        self.tail = obj
        obj.next = None

    def __add__(self, other):
        self.push_back(other)
        return self

    def __iadd__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        if not isinstance(other, list):
            raise TypeError(f"{other} must be a list")
        for i, val in enumerate(other):
            self.push_back(StackObj(val))
        return self

    def __imul__(self, other):
        self.__mul__(other)
        return self


assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"
