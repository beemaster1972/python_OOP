class Record:

    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        self.__index = list(kwargs.keys())

    def __check_index(self, item):
        if isinstance(item, int) and len(self.__index) * -1 <= item < len(self.__index):
            return True
        raise IndexError(f'неверный индекс поля {item}')

    def __getitem__(self, item):
        if self.__check_index(item):
            return self.__dict__.get(self.__index[item], None)

    def __setitem__(self, key, value):
        if self.__check_index(key):
            self.__dict__[self.__index[key]] = value


if __name__ == '__main__':
    r = Record(pk=1, title='Python ООП', author='Балакирев')
    print(r[-1])
    print(r[-2])
    print(r[-3])
    r[0] = 2
    print(r[0])
