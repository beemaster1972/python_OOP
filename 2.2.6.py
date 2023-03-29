class StackObj:

    def __init__(self, data: str):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if type(next) in (StackObj,None):
            self.__next = next


class Stack:

    def __init__(self):
        self.__top = None