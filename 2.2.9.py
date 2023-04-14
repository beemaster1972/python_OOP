class LineTo:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        self.__top = None

    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, top):
        self.__top = top

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
    TOP = (0, 0)

    def __init__(self, *args):
        pass

    def add_line(self, line):
        pass

    @staticmethod
    def get_path():
        pass

    @staticmethod
    def get_length():
        pass

    @staticmethod
    def __get_line_length(x0, y0, x1, y1):
        return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** (1/2)
    