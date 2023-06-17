import sys
from random import randint


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
        if self.is_free and value in [0, 1, 2]:
            self._value = value
            self.is_free = not self.is_free
        else:
            raise ValueError('клетка уже занята')

    def __bool__(self):
        return self.is_free

    def __repr__(self):
        return f"{[' ', 'X', '0'][self.value]}"


class TicTacToe:
    __slots__ = 'pole', '__N', '__pole', '__wins'  # , 'FREE_CELL', 'HUMAN_X', 'COMPUTER_0'
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self, dimension=3):
        self.__N = dimension
        self.pole = ()
        self.__pole = {}
        self.__wins = {}
        self.init()

    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(self.__N)) for __ in range(self.__N))
        self.__pole = {(i, j): 0 for i in range(self.__N) for j in range(self.__N)}
        self.__wins[self.FREE_CELL] = self.__wins[self.HUMAN_X] = self.__wins[self.COMPUTER_O] = False

    def __check_index(self, item):
        if not isinstance(item, tuple) or \
                not all([isinstance(c, (int, slice)) for c in item]) or \
                not all([0 <= i < self.__N for i in item if isinstance(i, int)]):
            raise IndexError(f'неверный индекс клетки {item}')
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
        self.__check_win(value)

    def show(self):
        width = 1
        print("  " + " ".join(list(map(str, range(1, self.__N + 1)))))
        line = "--" + '+'.join(['-' * width] * self.__N) + '+'
        print(line)
        cnt = 1
        for r in self.pole:
            print(str(cnt) + '|' + '|'.join(map(str, r)) + '|')
            print(line)
            cnt += 1
        print()

    def __check_win(self, whom_checking):
        if self.__wins[whom_checking]:
            return True
        for _ in range(self.__N):
            row = self[_, :]  # получаем срез по строке
            col = self[:, _]  # получаем срез по колонке
            row_fl, col_fl = whom_checking, whom_checking  # флаги для строки и колонки
            for __ in range(self.__N):
                row_fl &= row[__]
                col_fl &= col[__]
            if whom_checking and (row_fl == whom_checking or col_fl == whom_checking):
                self.__wins[whom_checking] = True
                return True  # возвращаем истину что победил тот кого проверяем
        main_diagonal = [self[i, i] for i in range(self.__N)]  # срез по главной диагонали
        side_diagonal = [self[i, self.__N - i - 1] for i in range(self.__N)]  # срез по побочной диагонали
        md_fl, sd_fl = whom_checking, whom_checking  # флаги по диагоналям
        for _ in range(self.__N):
            md_fl &= main_diagonal[_]
            sd_fl &= side_diagonal[_]
        if whom_checking and (md_fl == whom_checking or sd_fl == whom_checking):
            self.__wins[whom_checking] = True
            return True
        self.__wins[self.FREE_CELL] = not whom_checking and not len(self.__pole)
        return self.__wins[self.FREE_CELL]

    @property
    def is_human_win(self):
        return self.__wins[self.HUMAN_X]

    @property
    def is_computer_win(self):
        return self.__wins[self.COMPUTER_O]

    @property
    def is_draw(self):
        return self.__wins[self.FREE_CELL]

    def __bool__(self):
        anybody_wins = self.__check_win(self.FREE_CELL) or self.__check_win(self.HUMAN_X) or \
                       self.__check_win(self.COMPUTER_O)
        return not anybody_wins and bool(len(self.__pole))

    def human_go(self):
        while True:
            coords = input("Введите координаты клетки через пробел")
            try:
                coords = list(map(int, coords.split()))
            except ValueError:
                print("Координаты должны быть целыми положительными числами")
                continue
            try:
                coords[0] -= 1
                coords[1] -= 1
                self[tuple(coords)] = self.HUMAN_X
                break
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                print(exc_obj)
                continue
        del self.__pole[tuple(coords)]

    def computer_go(self):
        while True:
            row, col = randint(0, self.__N - 1), randint(0, self.__N - 1)
            try:
                self[(row, col)] = self.COMPUTER_O
                break
            except:
                continue
        del self.__pole[(row, col)]


if __name__ == '__main__':
    cell = Cell()
    assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
    assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
    cell.value = 1
    assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

    assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe,
                                                                                     'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

    game = TicTacToe()
    assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
    assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
    game[1, 1] = TicTacToe.HUMAN_X
    assert game[
               1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

    game[0, 0] = TicTacToe.COMPUTER_O
    assert game[
               0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

    game.init()
    assert game[0, 0] == TicTacToe.FREE_CELL and game[
        1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

    try:
        game[3, 0] = 4
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    game.init()
    assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

    game[0, 0] = TicTacToe.HUMAN_X
    game[1, 1] = TicTacToe.HUMAN_X
    game[2, 2] = TicTacToe.HUMAN_X
    assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

    game.init()
    game[0, 0] = TicTacToe.COMPUTER_O
    game[1, 0] = TicTacToe.COMPUTER_O
    game[2, 0] = TicTacToe.COMPUTER_O
    assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
    raise ValueError("ВСЁ ОТЛИЧНО!!!")


    game = TicTacToe()
    game.init()
    step_game = 0
    while game:
        game.show()

        if step_game % 2 == 0:
            game.human_go()
        else:
            game.computer_go()

        step_game += 1

    game.show()

    if game.is_human_win:
        print("Поздравляем! Вы победили!")
    elif game.is_computer_win:
        print("Все получится, со временем")
    else:
        print("Ничья.")
