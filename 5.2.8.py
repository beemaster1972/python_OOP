import turtle


class Rect:

    def __init__(self, x, y, width, height):
        self._x, self._y, self._width, self._height = x, y, width, height

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise ValueError(f'некорректные координаты и параметры прямоугольника {key} = {value}')
        elif key in ('_width', '_height') and value <= 0:
            raise ValueError(f'некорректные параметры прямоугольника {key} = {value}')
        else:
            object.__setattr__(self, key, value)

    def is_collision(self, rect):
        collision = [self.x > rect.x + rect.width,
                     self.x + self.width < rect.x,
                     self.y > rect.y + rect.height,
                     self.y + self.height < rect.y
                     ]
        if not any(collision):
            raise TypeError('прямоугольники пересекаются')
        return rect

    def draw(self, pen: turtle.Turtle):
        pen.goto(self.x * 10, self.y * 10)
        pen.pendown()
        pen.forward(self.width * 10)
        pen.right(90)
        pen.forward(self.height * 10)
        pen.right(90)
        pen.forward(self.width * 10)
        pen.right(90)
        pen.forward(self.height * 10)
        pen.penup()
        pen.right(90)

    def __repr__(self):
        return f'Rect({self.x}, {self.y}, width={self.width}, height={self.height})'


def get_collision(rect):
    for el in lst_rect:
        if el == rect:
            continue
        try:
            el.is_collision(rect)
        except:
            return False
    return True


if __name__ == '__main__':
    coords = """0; 0; 5; 3
6; 0; 3; 5
3; 2; 4; 4
0; 8; 8; 1""".splitlines()
    lst_rect = [Rect(*tuple(map(int, el.split('; ')))) for el in coords]
    print(lst_rect)
    lst_not_collision = list(filter(get_collision, lst_rect))
    print(lst_not_collision)

    r = Rect(1, 2, 10, 20)
    assert r._x == 1 and r._y == 2 and r._width == 10 and r._height == 20, "неверные значения атрибутов объекта класса Rect"

    r2 = Rect(1.0, 2, 10.5, 20)

    try:
        r2 = Rect(0, 2, 0, 20)
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при создании объекта Rect(0, 2, 0, 20)"

    assert len(lst_rect) == 4, "список lst_rect содержит не 4 элемента"
    assert len(lst_not_collision) == 1, "неверное число элементов в списке lst_not_collision"


    def not_collision(rect):
        for x in lst_rect:
            try:
                if x != rect:
                    rect.is_collision(x)
            except TypeError:
                return False
        return True


    f = list(filter(not_collision, lst_rect))
    assert lst_not_collision == f, "неверно выделены не пересекающиеся прямоугольники, возможно, некорректно работает метод is_collision"

    r = Rect(3, 2, 2, 5)
    rr = Rect(1, 4, 6, 2)

    try:
        r.is_collision(rr)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError при вызове метода is_collision() для прямоугольников Rect(3, 2, 2, 5) и Rect(1, 4, 6, 2)"
    print("Всё отлично!!!")
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.shape('turtle')

    for rect in lst_rect:
        rect.draw(pen)
    pen.color('red')
    for rect in lst_not_collision:
        rect.draw(pen)
    window.mainloop()
