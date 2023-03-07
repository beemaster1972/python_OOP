class Point:

    def __init__(self, *args):
        self.set_coords(*args)

    @classmethod
    def check_coords(cls, *args):
        return all([type(val) in (int, float) for val in args])

    def set_coords(self, *args):
        if self.check_coords(*args):
            self.__x, self.__y = args

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:

    def __init__(self, *args):
        check = self.check_coords(*args)
        if  check == 0:
            self.set_coords(*args)
        elif check == 1:
            self.set_coords(Point(args[0], args[1]), Point(args[2], args[3]))
        else:
            raise ValueError('Неправильные координаты')


    @classmethod
    def check_coords(cls, *args):
        if len(args) == 2 and all([type(val)==Point for val in args]):
            return 0
        if len(args) == 4:
            return 1
        else:
            return 'ЙУХАН'


    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        x1, y1 = self.__sp.get_coords()
        x2, y2 = self.__ep.get_coords()
        print(f"Прямоугольник с координатами: ({x1}, {y1}) ({x2}, {y2})")


rect = Rectangle(0,0,20,34)
assert isinstance(rect, Rectangle) and hasattr(Rectangle, 'set_coords') and hasattr(Rectangle, 'get_coords') and hasattr(Rectangle, 'draw'), "в классе Rectangle присутствуют не все методы"

r = Rectangle(1, 2.6, 3.3, 4)
r.set_coords(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

r = Rectangle(Point(1, 2), Point(3, 4))
sp, ep = r.get_coords()
a, b = sp.get_coords()
c, d = ep.get_coords()
assert a == 1 and b == 2 and c == 3 and d == 4, "метод get_coords вернул неверные значения координат"

assert isinstance(r._Rectangle__sp, Point) and isinstance(r._Rectangle__ep, Point), "атрибуты __sp и __ep должны ссылаться на объекты класса Point"