class LineTo:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        self.__start = None

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        self.__start = start

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
