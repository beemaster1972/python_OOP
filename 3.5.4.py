class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, *args):
        self.__a, self.__b, self.__c = args

    def __setattr__(self, key, value):
        if isinstance(value, (int, float)) and self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            object.__setattr__(self, key, value)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c

    def get_volume(self):
        return self.a * self.b * self.c

    @staticmethod
    def get_other(other):
        return other.get_volume() if isinstance(other, Dimensions) else other

    def __ge__(self, other):
        vol = self.get_other(other)
        return self.get_volume() >= vol

    def __gt__(self, other):
        vol = self.get_other(other)
        return self.get_volume() > vol


class ShopItem:

    def __init__(self, *args):
        for _, arg in enumerate(args):
            if isinstance(arg, str):
                self.name = arg
            elif isinstance(arg, (int, float)):
                self.price = arg
            elif isinstance(arg, Dimensions):
                self.dim = arg
            elif isinstance(arg, tuple):
                self.dim = Dimensions(*arg)
            else:
                raise TypeError(f"Не применимый тип аргумента {arg} type({type(arg)})")

    def __str__(self):
        return f'{self.name} цена {self.price} р. объём {self.dim.get_volume():,} куб.ед'


lst_shop = [ShopItem('кеды', 1024, (40, 30, 120)),
            ShopItem('зонт', 500.24, (10, 20, 50)),
            ShopItem('холодильник', 40000, (2000, 600, 500)),
            ShopItem('табуретка', 2000.99, (500, 200, 200))]

lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
print(*lst_shop, sep='\n')
print('********************************')
print(*lst_shop_sorted, sep='\n')

