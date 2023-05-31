from random import randint


DEBUG = False


class Value:

    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Cell:
    is_mine = Value()
    number = Value()
    is_open = Value()

    def __init__(self):
        self.is_mine = False
        self.number = 0
        self.is_open = False

    def __setattr__(self, key, value):
        if 'is' in key and not isinstance(value, bool):
            raise ValueError(f"недопустимое значение атрибута {key}")
        elif 'number' in key and (not isinstance(value, int) or (value > 8 or value < 0)):
            raise ValueError(f"недопустимое значение атрибута {key}")
        else:
            object.__setattr__(self, key, value)

    def __bool__(self):
        return not self.is_open

    def __str__(self):
        if not DEBUG and self:
            return ' '
        return '*' if self.is_mine else str(self.number)

    # def __repr__(self):
    #     return f'{self.__class__} {"O" if self.is_open else "X"} {"MINE" if self.is_mine else self.number}'


class GamePole:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not GamePole.instance:
            GamePole.instance = super().__new__(cls)
        return GamePole.instance

    def __init__(self, *args):
        self.__n, self.__m, self.__total_mines = args
        self.__pole_cells = tuple()

    @property
    def total_mines(self):
        return self.__total_mines

    @property
    def pole(self):
        return self.__pole_cells

    @property
    def n(self):
        return self.__n

    @property
    def m(self):
        return self.__m

    def init_pole(self):
        pole = [[Cell() for _ in range(self.m)] for __ in range(self.n)]
        cnt = 0
        while cnt < self.total_mines:
            i, j = randint(0, self.n-1), randint(0, self.m-1)
            if pole[i][j].is_mine:
                continue
            pole[i][j].is_mine = True
            cnt += 1
        for i in range(self.n):
            for j in range(self.m):
                pole[i][j].number = self.__set_mines_around(pole, i, j)
        self.__pole_cells = tuple(tuple(pole[i][j] for j in range(self.m)) for i in range(self.n))

    def __set_mines_around(self, pole: list, x: int, y: int):
        if pole[x][y].is_mine:
            return 0
        sub_matrix = [pole[i][j].is_mine for j in range(max(0, y-1), min(self.m, y+2))
                      for i in range(max(0, x-1), min(self.n, x+2))]
        return sum(sub_matrix)

    def open_cell(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.m:
            self.pole[i][j].is_open = True
        else:
            raise IndexError(f'некорректные индексы {i}, {j} клетки игрового поля')

    def show_pole(self):
        for i in range(self.n):
            print('-' * (self.m * 2+1))
            print('|', end='')
            for j in range(self.m):
                print(self.pole[i][j], end='|')
            print()
        print('-' * (self.m * 2+1))


p1 = GamePole(10, 20, 10)
p2 = GamePole(10, 20, 10)
assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
p = p1

cell = Cell()
# assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
#     Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"

cell.is_mine = True
cell.number = 5
cell.is_open = True
assert bool(cell) == False, "функция bool() вернула неверное значение"

try:
    cell.is_mine = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    cell.number = 10
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

p.init_pole()
m = 0
for row in p.pole:
    for x in row:
        assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
        if x.is_mine:
            m += 1

assert m == 10, "на поле расставлено неверное количество мин"
p.open_cell(0, 1)
p.open_cell(9, 19)

try:
    p.open_cell(10, 20)
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"


def count_mines(pole, i, j):
    n = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            ii, jj = k + i, l + j
            if ii < 0 or ii > 9 or jj < 0 or jj > 19:
                continue
            if pole[ii][jj].is_mine:
                n += 1

    return n


for i, row in enumerate(p.pole):
    for j, x in enumerate(row):
        if not p.pole[i][j].is_mine:
            m = count_mines(p.pole, i, j)
            assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"
