class Line:

    def __init__(self, x1, y1, x2, y2):
        pass

    def set_coords(self, *args):
        if self.__check_coords(x1, y1, x2, y2):
            self.__x1, self.__x2, self.__y1, self.__y2 = *args

    @classmethod
    def __check_coords(cls, *args):
        return type(x1) in (int, float) and type(x2) in (int, float) and type(y1) in (int, float) and \
               type(y2) in (int, float)

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(self.__x1, self.__y1, self.__x2, self.__y2)