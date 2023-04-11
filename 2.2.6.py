class StackObj:

    def __init__(self, data: str):
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
        if type(next) in (StackObj, None):
            self.__next = next


class Stack:

    def __init__(self):
        self.top = None

    def __get_last_obj(self):
        cur_obj = self.top
        prev_obj = cur_obj
        while cur_obj.next:
            cur_obj = cur_obj.next
            prev_obj = cur_obj
        return cur_obj, prev_obj

    def push(self, obj):
        if type(obj) is not StackObj:
            return None
        if not self.top:
            self.top = obj
        else:
            last_obj, prev_obj = self.__get_last_obj()
            last_obj.next = obj

    def pop(self):
        last_obj, prev_obj = self.__get_last_obj()
        prev_obj.next = None
        return last_obj

    def get_data(self):
        result = []
        if self.top:
            cur_obj = self.top
            result.append(cur_obj.data)
            while cur_obj.next:
                cur_obj = cur_obj.next
                result.append(cur_obj.data)
        return result


s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1

assert n == 0, "при удалении всех объектов, стек-подобная стурктура оказалась не пустой"

s = Stack()
top = StackObj("name_1")
s.push(top)
obj = s.pop()
assert obj == top, "метод pop() должен возвращать удаляемый объект"