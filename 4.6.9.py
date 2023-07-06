class MoneyOperators:

    def get_other(self, other):
        if type(other) in (int, float):
            return other

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')
        return other.money

    def __add__(self, other):
        other = self.get_other(other)
        return self.__class__(self.money + other)

    # здесь объявляйте еще один метод
    def __sub__(self, other):
        other = self.get_other(other)
        return self.__class__(self.money - other)

    def __radd__(self, other):
        other = self.get_other(other)
        return self + other

    def __rsub__(self, other):
        other = self.get_other(other)
        return self.__class__(other - self.money)


# здесь объявляйте класс Money
class Money:
    __slots__ = '_money'

    def __init__(self, money):
        self.money = money

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise TypeError('Cумма должна быть числом')
        object.__setattr__(self, key, value)

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value


class MoneyR(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyR: {self.money}"


class MoneyD(Money, MoneyOperators):
    def __str__(self):
        return f"MoneyD: {self.money}"


if __name__ == '__main__':
    m1 = MoneyR(1)
    m2 = MoneyD(2)
    m = m1 + 10
    print(m)  # MoneyR: 11
    m = m - 5.4
    try:
        m = m1 + m2  # TypeError
    except TypeError:
        print('Разные типы объектов')
    m3 = 10 + m2
    m3 = 100 - m3
    print(m1, m2, m3, m)
