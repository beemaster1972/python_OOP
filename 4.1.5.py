from random import choice, random, randint, choices


class Thing:
    ID = 0

    def __init__(self, name, price):
        self.id = Thing.ID
        Thing.ID += 1
        self.name = name
        self.price = price
        self.weight = self.dims = self.memory = self.frm = None

    def get_info(self):
        return tuple(item for item in self.__dict__.values() if item is not None)


class Table(Thing):

    def __init__(self, name, price, weight, dims):
        super(Table, self).__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):

    def __init__(self, name, price, memory, frm):
        super(ElBook, self).__init__(name, price)
        self.memory = memory
        self.frm = frm


if __name__ == '__main__':
    things = [choice(
        [Table(choices('abcdef'), randint(1, 1000), random(), (randint(1, 1000), randint(1, 1000), randint(1, 1000))),

         ElBook(choices('abcdef'), randint(1, 1000), randint(1, 1000), choices('abcdef'))])

        for _ in range(10000)]

    for obj in things:
        print(obj.get_info())
