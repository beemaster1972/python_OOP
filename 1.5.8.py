class Goods:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class Table(Goods):
    pass


class TV(Goods):
    pass


class Notebook(Goods):
    pass


class Cup(Goods):
    pass


class Cart:

    def __init__(self):
        self.goods = []

    def add(self, *gd):
        self.goods.extend(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return [f'{el.name}: {el.price}' for el in self.goods]


cart  = Cart()
cart.add(TV('Samsung', 25000),TV('Philips', 30000),Table('Karpa', 10**5),
         Notebook('Lenovo', 145000),Notebook('Asus', 200000),Cup('Форфор',250))

print(cart.get_list())