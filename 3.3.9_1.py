class Ingredient:

    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


class Recipe:

    def __init__(self, *args):
        self.head = None
        self.tail = None
        self.count_ingredient = 0
        if args:
            for _, ingr in enumerate(args):
                self.add_ingredient(ingr)

    def add_ingredient(self, ingr):
        if not self.tail:
            self.head = ingr
        elif self.tail is self.head:
            self.head.next = ingr
        else:
            self.tail.next = ingr
        self.tail = ingr
        self.count_ingredient += 1

    def remove_ingredient(self, ingr):
        if not self.count_ingredient:
            return False
        if ingr is self.head:
            if self.tail is self.head:
                self.head = self.tail = None
                self.count_ingredient = 0
            else:
                self.head = self.head.next
                self.count_ingredient -= 1
            return True

        cur_obj = self.head.next
        prev_obj = self.head
        while cur_obj:
            if cur_obj is ingr:
                prev_obj.next = cur_obj.next
                if cur_obj is self.tail:
                    self.tail = prev_obj
                self.count_ingredient -= 1
                break
            cur_obj = cur_obj.next
            prev_obj = prev_obj.next

    def get_ingredients(self):
        cur_obj = self.head
        res = []
        while cur_obj:
            res.append(cur_obj)
            cur_obj = cur_obj.next
        return tuple(res)

    def __len__(self):
        return self.count_ingredient


i1 = Ingredient("Соль", 1, "столовая ложка")
i2 = Ingredient("Мука", 1, "кг")
i3 = Ingredient("Мясо баранины", 10, "кг")
i4 = Ingredient("Масло", 100, "гр")
recipe = Recipe(i1, i2, i3)
recipe.add_ingredient(i4)
recipe.remove_ingredient(i3)

assert len(recipe) == 3, "функция len вернула неверное значение"
lst = recipe.get_ingredients()
for x in lst:
    assert isinstance(x, Ingredient), "в списке рецептов должны быть только объекты класса Ingredient"
    assert hasattr(x, 'name') and hasattr(x, 'volume') and hasattr(x, 'measure'), "объект класса Ingredient должен иметь атрибуты: name, volume, measure"

assert str(i4) == "Масло: 100, гр", "метод __str__ вернул неверное значение"

i4 = Ingredient("Масло", 120, "гр")
recipe.add_ingredient(i4)
assert len(recipe) == 4, "функция len вернула неверное значение"