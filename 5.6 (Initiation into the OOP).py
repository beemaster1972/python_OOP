class Validator:
    def __init__(self, max_value):
        self.__max_value = max_value

    def __validate(self, value):
        return type(value) is int and 0 <= value <= self.__max_value

    def __call__(self, *args, **kwargs):
        return self.__validate(*args, **kwargs)


class Ship:

    def __init__(self, length, tp=1, x=None, y=None, validator=Validator):
        self._length = length
        self._tp = tp
        self._x, self._y = x, y
        self._is_move = True
        self._cells = [1] * self._length
        self.__validator = validator

    @property
    def length(self):
        return self._length

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if self.__validator(value):
            self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if self.__validator(value):
            self._y = value

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

    def is_collide(self, ship):
        """- проверка на столкновение с другим кораблем ship
        (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается,
        в том числе и по диагонали);
        метод возвращает True, если столкновение есть и False - в противном случае;"""
        collision = [self.x > ship.x + ship.length if ship._tp == 1 else 0,
                     self.x + self.length if self._tp == 1 else 0 < ship.x,
                     self.y > ship.y + ship.length if ship._tp == 2 else 0,
                     self.y + self.length if self._tp == 2 else 0 < ship.y
                     ]
        if not any(collision):
            return True
        return False

    def is_out_pole(self, size=10):
        """- проверка на выход корабля за пределы игрового поля
        (size - размер игрового поля, обычно, size = 10);
        возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;"""
        condition = [self.x + self.length if self._tp == 1 else 0]

