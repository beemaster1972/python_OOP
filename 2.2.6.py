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
        self.top = None

    def __get_last_obj(self):
        cur_obj = self.top
        while cur_obj.next:
            cur_obj = cur_obj.next
        return cur_obj

    def push(self, obj):
        if type(obj) is not StackObj:
            return None
        if not self.top:
            self.top = obj
        else:
            last_obj = self.__get_last_obj()
            last_obj.next = obj

    def pop(self):
        last_obj = self.__get_last_obj()




