class StackObj:

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    def __repr__(self):
        return f'{self.data} --> {self.next.data if self.next else "None"}'

    def __str__(self):
        return f'{self.data}'


class Stack:

    def __init__(self):
        self.top = self.tail = None
        self.__length = 0

    def push(self, obj):
        if not self.tail:
            self.top = self.tail = obj
        else:
            self.tail.next = obj
            self.tail = obj
        self.__length += 1

    def pop(self):
        if not self.tail:
            return False
        res = self.tail
        self.tail = self[self.__length - 2]
        self.tail.next = None
        self.__length -= 1
        return res

    def __len__(self):
        return self.__length

    def __check_index(self, item):
        if not isinstance(item, int) or not 0 <= item < self.__length:
            raise IndexError(f'неверный индекс {item}')

    def __get_item_by_index(self, index):
        cur_obj = self.top
        cnt = 0
        while cnt < index:
            cur_obj = cur_obj.next
            cnt += 1
        return cur_obj

    def __getitem__(self, item):
        self.__check_index(item)
        return self.__get_item_by_index(item)

    def __setitem__(self, key, value):
        self.__check_index(key)
        cur_obj = self.__get_item_by_index(key)
        next = cur_obj.next
        prev = self.__get_item_by_index(key-1)
        prev.next = cur_obj = value
        cur_obj.next = next


if __name__ == '__main__':
    st = Stack()
    st.push(StackObj("obj11"))
    st.push(StackObj("obj12"))
    st.push(StackObj("obj13"))
    st[1] = StackObj("obj2-new")
    assert st[0].data == "obj11" and st[
        1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

    try:
        obj = st[3]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    obj = st.pop()
    assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

    n = 0
    h = st.top
    while h:
        assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
        n += 1
        h = h.next

    assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"
    print("Всё отлично!!!")
