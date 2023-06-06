class Cell:
    __slots__ = ('_is_free', '_value')

    def __init__(self):
        self._is_free = True
        self._value = 0

    @property
    def is_free(self):
        return self._is_free

    @is_free.setter
    def is_free(self, val):
        self._is_free = val

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self.is_free and value in [0, 1, 2, 3]:
            self._value = value
            self.is_free = not self.is_free
        else:
            raise ValueError('клетка уже занята')

    def __bool__(self):
        return self.is_free

    def __repr__(self):
        return f"{[' ', 'X', '0'][self.value]}"


class TicTacToe:
    __slots__ = 'pole', '__N'

    def __init__(self, dimension=3):
        self.__N = dimension
        self.pole = tuple(tuple(Cell() for _ in range(self.__N)) for __ in range(self.__N))

    def clear(self):
        self.__init__(self.__N)

    def __check_index(self, item):
        if not isinstance(item, tuple) or \
                not all([isinstance(c, (int, slice)) for c in item]) or \
                not all([0 <= i < self.__N for i in item if isinstance(i, int)]):
            raise IndexError('неверный индекс клетки')
        return item, all([isinstance(c, int) for c in item])

    def __getitem__(self, item):
        item, is_int = self.__check_index(item)
        return self.pole[item[0]][item[1]].value if is_int else tuple(row.value for row in self.pole[item[0]][item[1]])

    def __setitem__(self, key, value):
        key, is_int = self.__check_index(key)
        if not is_int:
            raise IndexError("Можно изменять только одну клетку")
        self.pole[key[0]][key[1]].value = value

    def show(self):
        width = 1
        line = '+'.join(['-' * width] * self.__N)
        for r in self.pole:
            print('|'.join(map(str, r)))
            print(line)
        print()


if __name__ == '__main__':
    cell = Cell()
    cell.value = 2
    game = TicTacToe()
    game[0, 0] = 1
    game[0, 1] = 2
    game[0, 2] = 1
    game[1, 0] = 2
    game[1, 1] = 1
    game[1, 2] = 2
    game[2, 0] = 2
    game[2, 1] = 1
    game[2, 2] = 2
    game.show()
    game.clear()
    game.show()
    g = TicTacToe()
    g.clear()
    assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
    g[1, 1] = 1
    g[2, 1] = 2
    assert g[1, 1] == 1 and g[
        2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

    try:
        res = g[3, 0]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

    try:
        g[3, 0] = 5
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

    g.clear()
    g[0, 0] = 1
    g[1, 0] = 2
    g[2, 0] = 3
    a = g[:, 0]
    assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (
        1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

    cell = Cell()
    assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
    res = cell.is_free
    cell.is_free = True
    assert bool(cell), "функция bool вернула False для свободной клетки"
    print("Всё отлично!!!")
