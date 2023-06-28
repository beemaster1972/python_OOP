class Animal:

    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        self.__kind = value

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, value):
        self.__old = value

    def __repr__(self):
        return f'Animal({self.name}, {self.kind}, {self.old})'


if __name__ == '__main__':
    input_data = """Васька; дворовый кот; 5
                    Рекс; немецкая овчарка; 8
                    Кеша; попугай; 3"""
    animals = []
    for s in input_data.split("\n"):
        animals.append(Animal(*map(lambda x: x.strip() if not x.isdigit() else int(x.strip()), s.split(';'))))
    print(animals)
