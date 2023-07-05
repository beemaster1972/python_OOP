from random import randint, random


class Digit:
    _CONDITIONS = "[isinstance(value, (int, float, complex))]"
    __slots__ = 'value'

    def __init__(self, value):
        self.value = value

    def __setattr__(self, key, value):
        if all(eval(self._CONDITIONS)):
            object.__setattr__(self, key, value)
        else:
            raise TypeError(f'значение {value} не соответствует типу объекта')

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'


class Integer(Digit):
    _CONDITIONS = "[isinstance(value, int)]"


class Float(Digit):
    _CONDITIONS = "[isinstance(value, float)]"


class Positive(Digit):
    _CONDITIONS = "[value > 0]"


class Negative(Digit):
    _CONDITIONS = "[value < 0]"


class PrimeNumber(Integer, Positive):
    _CONDITIONS = Integer._CONDITIONS + "+" + Positive._CONDITIONS + "+[self._is_prime(value)]"

    @staticmethod
    def _is_prime(value):
        for _ in range(3, value, 2):
            for __ in range(3, int(pow(_, 1 / 2)) + 1, 2):
                if _ % __ == 0:
                    return False
        return True


class FloatPositive(Float, Positive):
    _CONDITIONS = Float._CONDITIONS + "+" + Positive._CONDITIONS


if __name__ == '__main__':
    d = Digit(1)
    k = 0
    n = 0
    prime_lst = []
    float_lst = []
    while k < 5 or n < 3:
        if n < 3:
            try:
                val = randint(-1000, 1000)
                prime_lst.append(PrimeNumber(val))
                n += 1
            except TypeError:
                print(val)
        if k < 5:
            try:
                val = random() * randint(-1000, 1000)
                float_lst.append(FloatPositive(val))
                k += 1
            except TypeError:
                print(val)

    digit = prime_lst + float_lst
    # print(digit)
    lst_positive = [positive for positive in filter(lambda x: isinstance(x, Positive), digit)]
    lst_float = [flt for flt in filter(lambda x: isinstance(x, Float), digit)]
    # print(lst_positive)
    # print(lst_float)
