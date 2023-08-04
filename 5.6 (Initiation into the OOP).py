from random import choice, shuffle, seed

import numpy as np


class ShipDefender:
    def __init__(self, ship):
        self.__ship = ship

    def __enter__(self):
        self.__temp = self.__ship.x, self.__ship.y, self.__ship.tp
        return self.__ship

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.__ship.x, self.__ship.y, self.__ship.tp = self.__temp
        return False


class Validator:
    def __init__(self, max_value):
        self.__max_value = max_value

    @property
    def size(self):
        return self.__max_value

    def __validate(self, value, size=None, length=0):
        specified_length = self.size if size is None else size
        return type(value) is int and 0 <= value <= specified_length and value + length <= specified_length

    def __call__(self, *args, **kwargs):
        return self.__validate(*args, **kwargs)


class Ship:

    def __init__(self, length, tp=1, x=None, y=None, validator=Validator(10)):
        self._length = length
        self._tp = tp
        self._x, self._y = x, y
        self._is_move = True
        self._cells = [1] * self._length
        self.__validator = validator

    @property
    def tp(self):
        return self._tp

    @tp.setter
    def tp(self, value):
        if type(value) == int and value in (1, 2):
            self._tp = value

    @property
    def length(self):
        return self._length

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        length = self.length if self.tp == 1 else 0
        if value is None or self.__validator(value, length=length):
            self._x = value
        else:
            raise ValueError(f'Ошибочная координата x = {value}')

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        length = self.length if self.tp == 2 else 0
        if value is None or self.__validator(value, length=length):
            self._y = value
        else:
            raise ValueError(f'Ошибочная координата y = {self.y}')

    # @property
    # def cells(self):
    #     return self._cells

    def set_start_coords(self, x, y):
        """- установка начальных координат (запись значений в локальные атрибуты _x, _y)"""
        self.x, self.y = x, y

    def get_start_coords(self):
        """- получение начальных координат корабля в виде кортежа x, y"""
        return self._x, self._y

    def move(self, go):
        """- перемещение корабля в направлении его ориентации на go клеток
        (go = 1 - движение в одну сторону на клетку;
         go = -1 - движение в другую сторону на одну клетку);
         движение возможно только если флаг _is_move = True"""
        if not self._is_move:
            raise ValueError('Корабль ранен и не может двигаться')
        moving_coord = self.x if self.tp == 1 else self.y
        moving_coord += go
        self.set_start_coords(moving_coord if self.tp == 1 else self.x, moving_coord if self.tp == 2 else self.y)

    def is_collide(self, ship):
        """- проверка на столкновение с другим кораблем ship
        (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается,
        в том числе и по диагонали);
        метод возвращает True, если столкновение есть и False - в противном случае;"""
        is_none = [self.x is None, self.y is None, ship.x is None, ship.y is None]
        if any(is_none) or self is ship:
            return False
        collision = [self.x > (ship.x + (ship.length if ship.tp == 1 else 1)),
                     (self.x + (self.length if self._tp == 1 else 1)) < ship.x,
                     self.y > (ship.y + (ship.length if ship.tp == 2 else 1)),
                     (self.y + (self.length if self._tp == 2 else 1)) < ship.y
                     ]
        if not any(collision):
            return True
        return False

    def is_out_pole(self, size=None):
        """- проверка на выход корабля за пределы игрового поля
        (size - размер игрового поля, обычно, size = 10);
        возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;"""
        if self.x is None or self.y is None:
            return False
        size = self.length if size is None else size
        condition = [not self.__validator(self.x + (self.length if self._tp == 1 else 0), size=size),
                     not self.__validator(self.y + (self.length if self._tp == 2 else 0), size=size)]
        return any(condition)

    def hurt(self, deck):
        if type(deck) == int and 0 <= deck < self.length:
            self[deck] = 2
            if self._is_move:
                self._is_move = False

    def get_health(self):
        return sum(self._cells) / self.length

    def __str__(self):
        return f'Ship(x={self.x},y={self.y}, {self.length}, {"ГОР" if self._tp == 1 else "ВЕР"})'

    def __repr__(self):
        return f'Ship(x={self.x},y={self.y}, {self.length}, {"ГОР" if self._tp == 1 else "ВЕР"})'

    def __check_index(self, key):
        if not (type(key) == int and 0 <= key < len(self._cells)):
            raise IndexError(f'Неверный индекс {key}')
        return key

    def __getitem__(self, key):
        key = self.__check_index(key)
        return self._cells[key]

    def __setitem__(self, key, value):
        key = self.__check_index(key)
        if not (type(value) == int and value in (1, 2)):
            raise ValueError(f'Неверное значение {value}')
        self._cells[key] = value


class GamePole:
    COMPOSITION_OF_THE_FLEET = {1: 4, 2: 3, 3: 2, 4: 1}

    def __init__(self, size, name='COMPUTER'):
        self._size = size
        self._ships = {}
        self.__validator = Validator(size)
        self._pole = None
        self.turns = np.array([[0] * self._size for _ in range(self._size)])
        self._ships_coords = [(x, y) for x in range(self._size) for y in range(self._size)]
        self.__name__ = name

    def __repr__(self):
        return f'{self.__name__}'

    def __delete_coords(self, ship):
        x_range = [j for j in
                   range(max(0, ship.x - 1), min(self._size, ship.x + ship.length + 1 if ship.tp == 1 else ship.x + 2))]
        y_range = [i for i in
                   range(max(0, ship.y - 1), min(self._size, ship.y + ship.length + 1 if ship.tp == 2 else ship.y + 2))]
        for x in x_range:
            for y in y_range:
                try:
                    del self._ships_coords[self._ships_coords.index((x, y))]
                except ValueError as e:
                    pass

    def init(self):
        """Корабли формируются в коллекции _ships следующим образом:
        однопалубных - 4;
        двухпалубных - 3;
        трехпалубных - 2;
        четырехпалубный - 1"""
        # Пополняем флот согласно расписания
        _ships_array = []
        for number_of_decks, number_of_ships in self.COMPOSITION_OF_THE_FLEET.items():
            ships_temp = [Ship(number_of_decks, choice([1, 2]), validator=self.__validator) for _ in
                          range(number_of_ships)]
            _ships_array += ships_temp
        for i, ship in enumerate(_ships_array[::-1]):
            while True and len(self._ships_coords):
                try:
                    shuffle(self._ships_coords)
                    x, y = choice(self._ships_coords)
                    with ShipDefender(ship) as s:
                        s.set_start_coords(x, y)

                except ValueError:
                    pass

                l = len(_ships_array) - 1
                fl = [_ships_array[_].is_collide(s) for _ in range(l, l - i, -1)]
                # Если нет ни одной коллизии с другими кораблями и координаты присвоены,
                # то выходим из цикла
                if not any(fl) and ship.x is not None and ship.y is not None:
                    self.__delete_coords(ship)
                    break
                # На всякий случай проверяем что больше нет доступных координат для размещения кораблей
                if not len(self._ships_coords):
                    raise Exception(f"Все варианты проверены, нет возможности разместить {s}")
        self._ships = {s: (s.x, s.y) for s in _ships_array}
        self._pole = self.get_pole()

    def __fill_ship(self, ship):
        for j in range(ship.length):
            try:
                self._pole[ship.y if ship.tp == 1 else ship.y + j][ship.x if ship.tp == 2 else ship.x + j] = \
                    ship[j]
            except (TypeError, IndexError, ValueError):
                pass

    def show(self):
        for _, row in enumerate(self._pole):
            for el in row:
                print(f'{el}', end='')
            print()

    def show_human(self):
        print(" |", *[f'{_:^2}' for _ in range(self.__validator.size)], end='    ')
        print(" |", *[f'{_:^2}' for _ in range(self.__validator.size)])
        print('-' * self._size * 3 + '-', end='      ')
        print('-' * self._size * 3 + '-')
        temp_pole = [tuple(zip(self._pole[_], self.turns[_])) for _ in range(self._size)]
        for _, row in enumerate(temp_pole):
            print(f'{_}|', end='')
            for el in row:
                ch = el[0] if el[0] else " "
                print(f'{ch:^3}', end='')

            print('    ' + f'{_}|', end='')
            for el in row:
                ch = el[1] if el[1] else " "
                ch = ch if el[1] >= 0 else "X"
                print(f'{ch:^3}', end='')

            print()

    def get_ships(self):
        """возвращает коллекцию _ships"""
        return [sh for sh in self._ships]

    def move_ships(self):
        """перемещает каждый корабль из коллекции _ships на одну клетку
        (случайным образом вперед или назад) в направлении ориентации корабля;
        если перемещение в выбранную сторону невозможно (другой корабль или пределы игрового поля),
        то попытаться переместиться в противоположную сторону,
        иначе (если перемещения невозможны), оставаться на месте"""
        for ship in self._ships:
            try:
                with ShipDefender(ship) as s:
                    go = choice([-1, 1])
                    s.move(go)
                    collides = [sh.is_collide(s) for sh in self._ships]
                    if any(collides) or s.is_out_pole(self._size):
                        raise ValueError
            except ValueError:
                try:
                    with ShipDefender(ship) as s:
                        go *= -1
                        s.move(go)
                        collides = [sh.is_collide(s) for sh in self._ships]
                        if any(collides) or s.is_out_pole(self._size):
                            raise ValueError
                except ValueError:
                    pass
            self._ships[ship] = ship.x, ship.y
        self._pole = self.get_pole()

    def get_pole(self):
        self._pole = [[0] * self._size for _ in range(self._size)]
        for s in self._ships:
            self.__fill_ship(s)
        return tuple(tuple(row) for row in self._pole)

    def get_ship_on_coords(self, x, y) -> Ship:
        for ship, coords in self._ships.items():
            if (coords[0] <= x < ship.length + coords[0] and ship.tp == 1 and y == coords[1]) or (
                    coords[1] <= y < coords[1] + ship.length and ship.tp == 2 and x == coords[0]):
                return ship
        return None

    def check_turn(self, x, y):
        self._pole = self.get_pole()
        if self._pole[y][x]:
            ship = self.get_ship_on_coords(x, y)
            deck = x - ship.x if ship.tp == 1 else y - ship.y
            ship.hurt(deck)
            return int(ship.get_health())
        else:
            self.move_ships()
            return 0


class SeaBattle:

    def __init__(self, size):
        self.human = GamePole(size, 'HUMAN')
        self.computer = GamePole(size)
        self.size = size
        self.computer_turns = [(x, y) for x in range(self.size) for y in range(self.size)]
        self.human_turns = [(x, y) for x in range(self.size) for y in range(self.size)]

    def computer_turn(self, x=None, y=None):
        if x == self.size or y == self.size:
            return True

        if (x is None or (x, y) not in self.computer_turns) and self.computer_turns:
            x, y = choice(self.computer_turns)
        if x is None or y is None:
            return False
        if self.human.check_turn(x, y) in (1, 2):
            print('ДЕРЖИ КОЖАННЫЙ УБЛЮДОК!!!')
            del self.computer_turns[self.computer_turns.index((x, y))]
            self.computer_turn(min(self.size - 1, x + 1), y)

        return True

    def __human_auto(self, x=None, y=None):
        if x == self.size or y == self.size:
            return True

        if (x is None or (x, y) not in self.human_turns) and len(self.human_turns):
            x, y = choice(self.human_turns)
        if x is None or y is None:
            return False
        if self.computer.check_turn(x, y) in (1, 2):
            print("ПОПАЛ!!!")
            del self.human_turns[self.human_turns.index((x, y))]
            self.human_turn(True, min(self.size - 1, x + 1), y)
        return True

    def human_turn(self, auto=False, x=None, y=None):
        if auto:
            return self.__human_auto(x, y)
        count = 0
        x = y = None
        prompt = 'Введите координаты выстрела x y (целые числа через пробел) :'
        while True and count < 10:
            coords = input(prompt).split()
            if coords[0] == 'DEBUG':
                print('DEBUG:')
                self.computer.show_human()
                continue
            try:
                x, y = map(int, coords)
            except Exception as e:
                count += 1
                if count == 5:
                    prompt = 'Для альтернативно одарённых повторяю:\n' + prompt
                if count == 9:
                    prompt = 'У тебя осталась ОДНА попытка!!! Если просрёшь и её, то компьютер победит\n' + \
                             prompt.split('\n')[1]
            else:
                break
            if count == 10:
                while self.computer_turns:
                    self.computer_turn()
                return
        self.human.turns[y][x] = self.computer.check_turn(x, y)
        if self.human.turns[y][x]:
            message = 'Попал' if self.human.turns[y][x] == 1 else 'УБИЛ!!!'
            print(message)
            self.human_turn()
        else:
            self.human.turns[y][x] = -1

    def get_victory(self):
        human_ships = self.human.get_ships()
        health_human_fleet = sum([s.get_health() for s in human_ships]) / len(human_ships)
        comp_ships = self.computer.get_ships()
        health_comp_fleet = sum([s.get_health() for s in comp_ships]) / len(comp_ships)
        return health_human_fleet, health_comp_fleet


def test():
    # seed(26)
    validator = Validator(10)
    ship = Ship(2)
    ship = Ship(2, 1)
    ship = Ship(3, 2, 0, 0, validator=validator)

    assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
    assert ship._cells == [1, 1, 1], "неверный список _cells"
    assert ship._is_move, "неверное значение атрибута _is_move"

    ship.set_start_coords(1, 2)
    assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
    assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

    ship.move(1)
    s1 = Ship(4, 1, 0, 0)
    s2 = Ship(3, 2, 0, 0)
    s3 = Ship(3, 2, 0, 2)

    assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
    assert s1.is_collide(
        s3) is False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

    s2 = Ship(3, 2, 1, 1)
    assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

    s2 = Ship(3, 1, 8, 1)
    assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

    s2 = Ship(3, 2, 1, 5)
    assert s2.is_out_pole(10) is False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

    s2[0] = 2
    assert s2[0] == 2, "неверно работает обращение ship[indx]"

    p = GamePole(10)
    p.init()
    for nn in range(5):
        for s in p._ships:
            assert s.is_out_pole(10) is False, "корабли выходят за пределы игрового поля"

            for ship in p.get_ships():
                if s != ship:
                    assert s.is_collide(ship) is False, f"корабли на игровом поле соприкасаются{s} {ship}"
        p.move_ships()

    gp = p.get_pole()
    assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
    assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

    pole_size_8 = GamePole(8)
    pole_size_8.init()
    print('Всё отлично!!!')


def play():
    # seed(20)
    auto_play = input('Желаете авто игру? (y/n)') == 'y'
    game = SeaBattle(10)
    game.human.init()
    game.computer.init()
    human_health, comp_health = game.get_victory()
    while human_health != 2 or comp_health != 2:
        # print('HUMAN')
        if not auto_play:
            game.human.show_human()
        game.human_turn(auto_play)
        human_health, comp_health = game.get_victory()
        if comp_health == 2:
            break
        game.computer_turn()
        human_health, comp_health = game.get_victory()
        if human_health == 2:
            break
        human_health, comp_health = game.get_victory()
    game.human.show_human()
    message = "Победил "
    message += 'ЧЕЛОВЕК' if human_health - comp_health < 0 else 'КОМПЬЮТЕР'
    message = 'Ничья' if human_health - comp_health == 0 else message
    print(f'{message}')

    # sh = Ship(2, 2, 5, 0)
    # sh1 = Ship(1,1,6,0)
    # print(sh.is_collide(sh1))
    # print(sh.is_out_pole())


def main():
    test()


if __name__ == '__main__':
    main()
