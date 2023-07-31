class Ship:

    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._tp = tp
        self._x, self._y = x, y
        self._is_move = True
        self._cells = [1] * self._length

    @property
    def length(self):
        return self._length

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def set_start_coords(self, x, y):
        """- установка начальных координат (запись значений в локальные атрибуты _x, _y)"""

    def get_start_coords(self):
        """- получение начальных координат корабля в виде кортежа x, y"""
        return self._x, self._y

    def move(self, go):
        """- перемещение корабля в направлении его ориентации на go клеток
        (go = 1 - движение в одну сторону на клетку;
         go = -1 - движение в другую сторону на одну клетку);
         движение возможно только если флаг _is_move = True"""

    def is_collide(self, ship):
        """- проверка на столкновение с другим кораблем ship
        (столкновением считается, если другой корабль или пересекается с текущим или просто соприкасается,
        в том числе и по диагонали);
        метод возвращает True, если столкновение есть и False - в противном случае;"""
        collision = [self.x > ship.x + ship.length,
                     self.x + self.length < ship.x,
                     self.y > ship.y + ship.length,
                     self.y + self.length < ship.y
                     ]
        if not any(collision):
            raise TypeError('прямоугольники пересекаются')
        return rect

    def is_out_pole(self, size):
        """- проверка на выход корабля за пределы игрового поля
        (size - размер игрового поля, обычно, size = 10);
        возвращается булево значение True, если корабль вышел из игрового поля и False - в противном случае;"""
