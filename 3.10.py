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
    __slots__ = 'pole', '__N'  # , 'FREE_CELL', 'HUMAN_X', 'COMPUTER_0'
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self, dimension=3):
        self.__N = dimension
        self.pole = ()
        self.init()

    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(self.__N)) for __ in range(self.__N))

    def __check_index(self, item):
        if not isinstance(item, tuple) or \
                not all([isinstance(c, (int, slice)) for c in item]) or \
                not all([0 <= i < self.__N for i in item if isinstance(i, int)]):
            raise IndexError('неверный индекс клетки')
        return item, all([isinstance(c, int) for c in item])

    def __getitem__(self, item):
        item, is_int = self.__check_index(item)
        if not is_int:
            res = []

            row_range = range(item[0], item[0] + 1) if isinstance(item[0], int) else range(*item[0].indices(self.__N))
            col_range = range(item[1], item[1] + 1) if isinstance(item[1], int) else range(*item[1].indices(self.__N))
            for _ in row_range:
                for __ in col_range:
                    res.append(self.pole[_][__].value)

        return self.pole[item[0]][item[1]].value if is_int else tuple(res)

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
