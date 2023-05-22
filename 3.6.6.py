import sys
import re


class ShopItem:

    def __init__(self, *args):
        self.name, self.weight, self.price = args

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return hash(self) == hash(other)


lst_in = list(map(str.strip, (input() for _ in range(4))))
lst_in = [tuple(re.split(r'[:]+', x)) for x in lst_in]
print(lst_in)
# shop_items = {ShopItem(re.split(r': ', x)): []}

