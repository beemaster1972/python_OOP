class Cell:

    def __init__(self, data=None):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    def __repr__(self):
        return f'{self.data}'


class IterTable:

    def __init__(self, row):
        self.__row = row

    def __iter__(self):
        for _, el in enumerate(self.__row):
            yield el

    def __repr__(self):
        return f'IterTable({self.__row})'


class TableValues:

    def __init__(self, *args, type_data=int):
        if not all([isinstance(args[i], int) and args[i] > 0 for i in range(2)]):
            raise ValueError(f'Неверные размерности таблицы {args}')
        self.coords = args
        self.type_data = type_data
        self.__index = -1
        if type_data is int:
            default = 0
        elif type_data is float:
            default = 0.0
        elif type_data is str:
            default = ''
        else:
            default = None

        self.__table = {(i, j): Cell(default) for i in range(self.coords[0]) for j in range(self.coords[1])}

    def __check_index(self, item):
        if isinstance(item, tuple) and all((type(item[i]) == int and 0 <= item[i] < self.coords[i] for i in (0, 1))):
            return True
        else:
            raise IndexError(f'Неверные индексы {item}')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.__table[item].data

    def __setitem__(self, key, value):
        self.__check_index(key)
        if not isinstance(value, self.type_data):
            raise TypeError('неверный тип присваиваемых данных')
        self.__table[key].data = value

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        self.__index += 1
        if self.__index < self.coords[0]:
            return IterTable([self.__table[(self.__index, i)].data for i in range(self.coords[1])])
        else:
            raise StopIteration

    def __repr__(self):
        return f'TableValues({self.coords[0]},{self.coords[1]}, {self.type_data})'


if __name__ == '__main__':
    tb = TableValues(3, 2)
    n = m = 0
    for row in tb:
        n += 1
        for value in row:
            m += 1
            assert type(
                value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

    assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

    tb[0, 0] = 10
    assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

    try:
        tb[2, 0] = 5.2
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError"

    try:
        a = tb[2, 4]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    print("Всё отлично!!!")
