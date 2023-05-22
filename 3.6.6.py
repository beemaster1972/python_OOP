# import sys


class ShopItem:

    def __init__(self, *args):
        self.name = args[0]
        try:
            self.weight = int(args[1])
        except:
            self.weight = float(args[1])
        try:
            self.price = int(args[2])
        except:
            self.price = float(args[2])

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __repr__(self):
        return f'{self.name} {self.weight} {self.price}'


lst_in = list(map(str.strip, (input() for _ in range(4))))
list_in = [ShopItem(x[:x.index(':')], *list(map(float, x[x.index(':')+1:].split()))) for x in lst_in]

shop_items = {x: [x, list_in.count(x)] for x in list_in}




it1 = ShopItem('name', 10, 11)
it2 = ShopItem('name', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

it2 = ShopItem('name', 10, 12)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('name', 11, 11)
assert hash(it1) != hash(it2), "равные хеши у разных объектов"

it2 = ShopItem('NAME', 10, 11)
assert hash(it1) == hash(it2), "разные хеши у равных объектов"

name = lst_in[0].split(':')
for sp in shop_items.values():
    assert isinstance(sp[0], ShopItem) and type(sp[1]) == int, "в значениях словаря shop_items первый элемент должен быть объектом класса ShopItem, а второй - целым числом"

v = list(shop_items.values())
print(*v)
if v[0][0].name.strip() == "Системный блок":
    assert v[0][1] == 1 and v[1][1] == 2 and v[2][1] == 1 and len(v) == 3, "неверные значения в словаре shop_items"

if v[0][0].name.strip() == "X-box":
    assert v[0][1] == 2 and v[1][1] == 1 and v[2][1] == 2 and len(v) == 3, "неверные значения в словаре shop_items"


