class Array:

    def __init__(self, max_length, cell):
        self.__max_length = max_length
        self.__array = [cell() for _ in range(max_length)]

    def __check_index(self, item):
        if not isinstance(item, int) or not 0 <= item < self.__max_length:
            raise IndexError(f'неверный индекс {item} для доступа к элементам массива')

    def __len__(self):
        return len(self.__array)

    def __getitem__(self, item):
        self.__check_index(item)
        return self.__array[item].value

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.__array[key].value = value

    def __str__(self):
        return ' '.join(map(str, self.__array))

    def __repr__(self):
        return f'{self.__name__} {self.__array[0]}...{self.__array[-1]} '

class Numeric:

    def __init__(self, type, descr, start_value=0):
        self.type = type
        self.descr = descr
        self.__value = start_value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def __setattr__(self, key, value):
        if 'value' in key and not isinstance(value, self.type):
            raise ValueError(f'должно быть {self.descr} число')
        object.__setattr__(self, key, value)

    def __str__(self):
        return str(self.value)

class Integer(Numeric):

    def __init__(self, start_value=0):
        super().__init__(int, 'целое', start_value)


class Float(Numeric):

    def __init__(self, start_value=0.0):
        super().__init__(float, 'вещественное', start_value)


if __name__ == '__main__':
    ar_int = Array(10, cell=Integer)
    print(ar_int[3])
    print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
    ar_int[1] = 10
    # ar_int[1] = 10.5  # должно генерироваться исключение ValueError
    # ar_int[10] = 1  # должно генерироваться исключение IndexError
    print(ar_int)
    ar_float = Array(10, cell=Float)
    print(ar_float)
    for _ in range(len(ar_float)):
        ar_float[_] = _ * 1000.0

    print(ar_float)
