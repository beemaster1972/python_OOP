class Value:

    def __set_name__(self, owner, name):
        self.name = '_' + owner.__name__ + '__' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class ObjList:

    data = Value()
    next = Value()
    prev = Value()

    def __init__(self, data: str):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        head = self.prev.data if self.prev else '['
        tail = self.next.data if self.next else ']'
        res = f'{head} {self.data} {tail}'
        return res


class LinkedList:
    len_list = 0

    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if not self.tail:
            self.head = obj
            self.tail = obj
        elif self.head is self.tail:
            self.head.next = obj
            obj.prev = self.head
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

        self.len_list += 1

    def remove_obj(self, indx):
        cur_obj = self.head
        i = 0
        while i < self.len_list:
            if i == indx:
                if cur_obj is self.tail:
                    self.tail = cur_obj.prev
                    cur_obj.prev.next = None
                elif cur_obj is self.head:
                    cur_obj.next.prev = None
                    self.head = cur_obj.next
                else:
                    cur_obj.prev.next = cur_obj.next
                    cur_obj.next.prev = cur_obj.prev
                self.len_list -= 1
                break
            else:
                i += 1
                cur_obj = cur_obj.next

    def __call__(self, *args, **kwargs):
        cur_obj = self.head
        i = 0
        while i < self.len_list:
            if i == args[0]:
                return cur_obj.data
            i += 1
            cur_obj = cur_obj.next

    def __len__(self):
        return self.len_list


ln = LinkedList()
ln.add_obj(ObjList("Сергей"))
ln.add_obj(ObjList("Балакирев"))
ln.add_obj(ObjList("Python ООП"))
ln.remove_obj(2)
assert len(ln) == 2, "функция len вернула неверное число объектов в списке, возможно, неверно работает метод remove_obj()"
ln.add_obj(ObjList("Python"))
assert ln(2) == "Python", "неверное значение атрибута __data, взятое по индексу"
assert len(ln) == 3, "функция len вернула неверное число объектов в списке"
assert ln(1) == "Балакирев", "неверное значение атрибута __data, взятое по индексу"

n = 0
h = ln.head
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__next
    n += 1

assert n == 3, "при перемещении по списку через __next не все объекты перебрались"

n = 0
h = ln.tail
while h:
    assert isinstance(h, ObjList)
    h = h._ObjList__prev
    n += 1

assert n == 3, "при перемещении по списку через __prev не все объекты перебрались"