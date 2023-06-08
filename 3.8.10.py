class Cell:
    __slots__ = "__value"

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class SparseTable:
    __slots__ = ("rows", "cols", "__table")

    def __init__(self):
        self.rows, self.cols = 0, 0
        self.__table = {}

    def add_data(self, row, col, data):
        self.__check_index((row, col))
        self.__table[(row, col)] = data if isinstance(data, Cell) else Cell(data)
        self.rows = max((self.rows, row+1))
        self.cols = max((self.cols, col+1))

    def __check_index(self, item, exists=False):
        if not isinstance(item, tuple):
            raise IndexError(f"Индексы должны быть кортежем")
        if not all([isinstance(x, int) and x >= 0 for x in item]):
            raise IndexError(f"Неправильные индексы {item}")
        if exists and self.__table.get(item, None) is None:
            return False
        else:
            return True

    def __getitem__(self, item):
        if not self.__check_index(item, True):
            raise ValueError('ячейка с указанными индексами не существует')
        return self.__table[item].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.__table[key] = value if isinstance(value, Cell) else Cell(value)
        self.rows = max(self.rows, key[0]+1)
        self.cols = max(self.cols, key[1]+1)

    def __delitem__(self, key):
        if not self.__check_index(key, True):
            raise IndexError('ячейка с указанными индексами не существует')
        del self.__table[key]
        self.rows = max(self.__table.keys(), key=lambda x: x[0])[0]+1
        self.cols = max(self.__table.keys(), key=lambda x: x[1])[1]+1

    def remove_data(self, row, col):
        del self[(row, col)]


if __name__ == '__main__':
    st = SparseTable()
    st.add_data(2, 5, Cell(25))
    st.add_data(1, 1, Cell(11))
    assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"

    try:
        v = st[3, 2]
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    st[3, 2] = 100
    assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
    assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"

    st.remove_data(1, 1)
    try:
        v = st[1, 1]
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    try:
        st.remove_data(1, 1)
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    d = Cell('5')
    assert d.value == '5', "неверное значение атрибута value в объекте класса Cell, возможно, некорректно работает инициализатор класса"

    print("Всё отлично!!!")