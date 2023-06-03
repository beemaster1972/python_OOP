class IntegerValue:

    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('возможны только целочисленные значения')
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

class TableValues:
    rows = IntegerValue()
    cols = IntegerValue()

    def __init__(self, rows, cols, cell=None):
        if not cell:
            raise ValueError('параметр cell не указан')
        self.rows = abs(rows)
        self.cols = abs(cols)
        self.cells = tuple(tuple(cell() for _ in range(self.cols)) for __ in range(self.rows))

    def __check_index(self, item):
        if isinstance(item, tuple) and len(item) == 2 and all([isinstance(x, int) for x in item]):
            if 0 <= item[0] < self.rows and 0 <= item[1] < self.cols:
                return True
        raise IndexError(f"Неправильный индекс {item}")

    def __getitem__(self, item):
        self.__check_index(item)
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        if self.__check_index(key) and isinstance(value, int):
            self.cells[key[0]][key[1]].value = value
        else:
            raise ValueError('возможны только целочисленные значения')


if __name__ == '__main__':
    table = TableValues(2, 3, cell=CellInteger)
    print(table[0, 1])
    table[1, 1] = 10
#    table[0, 0] = 1.45  # генерируется исключение ValueError

    # вывод таблицы в консоль
    for row in table.cells:
        for x in row:
            print(x.value, end=' ')
        print()

    tb = TableValues(3, 2, cell=CellInteger)
    tb[0, 0] = 1
    assert tb[0, 0] == 1, "некорректно работает запись и/или считывание значения в ячейку таблицы по индексам"

    try:
        tb[2, 1] = 1.5
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    for row in tb.cells:
        for x in row:
            assert isinstance(x, CellInteger), "коллекция cells должна содержать только объекты класса  CellInteger"

    cell = CellInteger(10)
    assert cell.value == 10, "дескриптор value вернул неверное значение"
    print('Всё отлично!!')