from random import randint, choice, seed


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

    def __validate(self, value, size=10):
        return type(value) is int and 0 <= value <= (self.size if self.size == size else size)

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
        if value is None or self.__validator(value):
            self._x = value
        else:
            raise ValueError(f'Ошибочная координата x = {value}')

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value is None or self.__validator(value):
            self._y = value
        else:
            raise ValueError(f'Ошибочная координата y = {self.y}')

    @property
    def cells(self):
        return self._cells

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
            return False
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

    def is_out_pole(self, size=10):
        """- проверка на выход корабля за пределы игрового поля
        (size - размер игрового поля, обычно, size = 10);
        возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;"""
        if self.x is None or self.y is None:
            return False
        condition = [not self.__validator(self.x + (self.length if self._tp == 1 else 0), size),
                     not self.__validator(self.y + (self.length if self._tp == 2 else 0), size)]
        return any(condition)

    def hurt(self, deck):
        if type(deck) == int and 0 <= deck < self.length:
            self._cells[deck] = 2
            if self._is_move:
                self._is_move = False

    def get_health(self):
        return sum(self._cells) / self.length

    def __str__(self):
        return f'Ship(x={self.x},y={self.y}, {self.length}, {"ГОР" if self._tp == 1 else "ВЕР"})'

    def __repr__(self):
        return f'Ship(x={self.x},y={self.y}, {self.length}, {"ГОР" if self._tp == 1 else "ВЕР"})'


class GamePole:
    COMPOSITION_OF_THE_FLEET = {1: 4, 2: 3, 3: 2, 4: 1}

    def __init__(self, size):
        self._size = size
        self._ships = {}
        self.__validator = Validator(size)
        self._pole = None

    def init(self):
        """Корабли формируются в коллекции _ships следующим образом:
        однопалубных - 4;
        двухпалубных - 3;
        трехпалубных - 2;
        четырехпалубный - 1"""
        # Пополняем флот согласно расписания
        _ships = []
        for number_of_decks, number_of_ships in self.COMPOSITION_OF_THE_FLEET.items():
            ships_temp = [Ship(number_of_decks, randint(1, 2), validator=self.__validator) for _ in
                          range(number_of_ships)]
            _ships += ships_temp
        count = []  # Кэш для использованных координат
        for i, ship in enumerate(_ships):
            with ShipDefender(ship) as s:
                while True and len(count) <= self._size * self._size:
                    try:
                        lim_x = self._size - 1 if s.tp == 2 else self._size - s.length  # Правый лимит для Х
                        lim_y = self._size - 1 if s.tp == 1 else self._size - s.length  # Правый лимит для Y
                        x, y = randint(0, lim_x), randint(0, lim_y)
                        while (x, y) in count and len(count) <= (self._size * self._size) * 0.7:
                            # Коэффициент 0,7 подобран экспериментально, если взять больше, то возрастает вероятность
                            # безконечного цикла
                            x, y = randint(0, lim_x), randint(0, lim_y)
                        s.set_start_coords(x, y)
                        count.append((x, y))
                    except ValueError:
                        pass
                    fl = [_ships[_].is_collide(s) for _ in range(i)]
                    if not fl or (not any(fl) and not s.is_out_pole(self._size)):
                        break
                if len(count) == self._size * self._size:
                    raise Exception(f"Все варианты проверены, нет возможности разместить {s}")
        self._ships = {(s.x, s.y): s for s in _ships}
        self._pole = self.get_pole()

    def __fill_ship(self, ship):
        for j in range(ship.length):
            self._pole[ship.x if ship.tp == 2 else ship.x + j][ship.y if ship.tp == 1 else ship.y + j] = \
                ship.cells[j]

    def show(self):
        for _, row in enumerate(self._pole):
            for el in row:
                print(f'{el}', end='')
            print()

    def show_human(self):
        print(" |", *[f'{_:^2}' for _ in range(self.__validator.size)])
        print('-' * self.__validator.size * 3)
        for _, row in enumerate(self._pole):
            print(f'{_}|', end='')
            for el in row:
                ch = el if el else " "
                print(f'{ch:^3}', end='')
            print()

    def get_ships(self):
        """возвращает коллекцию _ships"""
        return [sh for sh in self._ships.values()]

    def move_ships(self):
        """перемещает каждый корабль из коллекции _ships на одну клетку
        (случайным образом вперед или назад) в направлении ориентации корабля;
        если перемещение в выбранную сторону невозможно (другой корабль или пределы игрового поля),
        то попытаться переместиться в противоположную сторону,
        иначе (если перемещения невозможны), оставаться на месте"""
        for ship in self._ships.values():
            with ShipDefender(ship) as s:
                try:
                    go = choice([-1, 1])
                    s.move(go)
                    collides = [sh.is_collide(s) for sh in self._ships.values()]
                    if any(collides) or s.is_out_pole(self._size):
                        raise ValueError
                except ValueError:
                    try:
                        go *= -1
                        s.move(go)
                        collides = [sh.is_collide(s) for sh in self._ships.values()]
                        if any(collides) or s.is_out_pole(self._size):
                            raise ValueError
                    except ValueError:
                        pass
        self._pole = self.get_pole()

    def get_pole(self):
        self._pole = [[0] * self._size for _ in range(self._size)]
        for s in self._ships.values():
            self.__fill_ship(s)
        return tuple(tuple(row) for row in self._pole)

    def get_ship_on_coords(self, x, y) -> Ship:
        for coords in self._ships:
            if x in coords or y in coords:
                return self._ships[coords]
        return None

    def check_turn(self, x, y):
        self._pole = self.get_pole()
        if self._pole[x][y]:
            ship = self.get_ship_on_coords(x, y)
            deck = x - ship.x if ship.tp == 1 else y - ship.y
            ship.hurt(deck)

        else:
            self.move_ships()
            return False


class SeaBattle:

    def __init__(self, size):
        self.human = GamePole(size)
        self.computer = GamePole(size)
        self.size = size
        self.computer_turns = {}

    def computer_turn(self):
        x_lim = self.size - 1
        y_lim = self.size - 1
        x, y = randint(0, x_lim), randint(0, y_lim)
        while (x, y) in self.computer_turns:
            x, y = randint(0, x_lim), randint(0, y_lim)
        self.computer_turns[(x, y)] = 1
        self.human.check_turn(x, y)

    def get_victory(self):
        human_ships = self.human.get_ships()
        sum_human = sum([s.get_health() for s in human_ships]) / len(human_ships)
        comp_ships = self.computer.get_ships()
        sum_comp = sum([s.get_health() for s in comp_ships]) / len(comp_ships)
        return sum_comp,sum_human


if __name__ == '__main__':
    seed(20)
    game = SeaBattle(10)
    game.human.init()
    game.computer.init()
    comp, hum = game.get_victory()
    print(comp, hum)
    for _ in range(100):
        game.computer_turn()
    comp, hum = game.get_victory()
    print(comp, hum)
    game.human.show_human()
    print(game.computer_turns)
    # sh = Ship(2, 2, 5, 0)
    # sh1 = Ship(1,1,6,0)
    # print(sh.is_collide(sh1))
    # print(sh.is_out_pole())
