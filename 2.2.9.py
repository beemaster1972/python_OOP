class LineTo:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


class PathLines:

    def __init__(self, *args):
        self.first = LineTo()
        self.last = self.first
        for i, el in enumerate(args):
            self.add_line(el)

    def add_line(self, line):
        self.last.next = line
        self.last = line

    def get_path(self, fl=False):
        res = []
        cur_line = self.first
        while cur_line:
            res.append(cur_line)
            cur_line = cur_line.next
        return res if fl else res[1:]

    def get_length(self):
        l = self.get_path(fl=True)
        length = 0
        for i in range(1, len(l)):
            length += PathLines.__get_line_length(l[i-1].x, l[i-1].y, l[i].x, l[i].y)
        return length

    @staticmethod
    def __get_line_length(x0, y0, x1, y1):
        return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** (1/2)

# TEST-TASK___________________________________
assert isinstance(PathLines, object), "Не создан класс PathLines"
assert hasattr(PathLines, 'get_path'), "Объявите метод get_path"
assert hasattr(PathLines, 'get_length'), "Объявите метод get_length"
assert hasattr(PathLines, 'add_line'), "Объявите метод add_line"

assert isinstance(LineTo, object), "Не создан класс LineTo"
lineto = LineTo(0, 0)
assert hasattr(lineto, 'x'), "В экземпляре класса LineTo нет атрибута x"
assert hasattr(lineto, 'y'), "В экземпляре класса LineTo нет атрибута y"

p = PathLines(LineTo(1, 2))
l = p.get_length()
assert l == 2.23606797749979, f"неверный вывод {l}, а должно быть: 2.23606797749979"

p.add_line(LineTo(10, 20))
p.add_line(LineTo(5, 17))
l = p.get_length()
assert l == 28.191631669843197, f"неверный вывод {l}, а должно быть: 28.191631669843197"

m = p.get_path()
print(len(m))
assert all(isinstance(i, LineTo) for i in m) and len(m) == 3, "неверный вывод должно быть: True"

h = PathLines(LineTo(4, 8), LineTo(-10, 30), LineTo(14, 2))
l = h.get_length()
assert l == 71.8992593599813, f"неверный вывод {l}, а должно быть: 71.8992593599813"

k = PathLines()
assert k.get_length() == 0, "неверный вывод должно быть: 0"

assert k.get_path() == [], "неверный вывод должно быть: [] (пустой список)"
print("Правильный ответ !")