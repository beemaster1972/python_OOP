class Shop:

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.goods.append(product)

    def remove_product(self, product):
        if isinstance(product, Product):
            self.goods.remove(product)


class Product:
    UID = 0

    def __new__(cls, *args, **kwargs):
        cls.UID += 1
        return super().__new__(cls)

    def __init__(self, name, weight, price):
        self.id = Product.UID
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key in ('weight', 'price'):
            if not(isinstance(value, (int, float)) and value >= 0):
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'name':
            if not isinstance(value, str):
                raise TypeError("Неверный тип присваиваемых данных.")

        object.__setattr__(self, key, value)



    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


# TEST-TASK___________________________________
assert issubclass(Shop, object), "Класс Book не является подклассом object, скорее всего не создан"
assert issubclass(Product, object), "Класс Product не является подклассом object, скорее всего не создан"

# проверка атрибутов в классах
shop = Shop("Балакирев и К")
# проверка названия
assert 'Балакирев и К' in shop.__dict__.values(), "ошибка в инициализаторе, не создается название магазина "

assert hasattr(shop, "goods"), "Не создан локальный атрибут - goods"
assert hasattr(shop, 'add_product'), "Метод add_product не определен в объекте"
assert hasattr(shop, 'remove_product'), "Метод add_product не определен в объекте"

# проверка атрибутов в классах
book = Product("Python ООП", 100, 1024)

assert hasattr(book, 'id'), "Не создан локальный атрибут - id"
assert type(book.id) == int, "номер id должен быть целым числом"

assert hasattr(book, 'weight'), "Не создан локальный атрибут - weight"
assert type(book.weight) in (int, float) and book.weight > 0, \
    "weight должен быть целое или вещественное положительное число"

assert hasattr(book, 'price'), "Не создан локальный атрибут - price"
assert type(book.price) in (int, float) and book.price > 0, \
    "price должна быть целое или вещественное положительное число "

# проверка, что номера id уникальны
lst = [Product("Python ООП", 100, 1024).id for _ in range(0, 20)]
assert any(False if lst[_] in lst[_ + 1:] else True for _ in range(len(lst))), "ошибка id не уникальны !!!"

# проверка add_product
shop.add_product(Product("Python ООП", 100, 1024))
x = Product("Test", 10, 10)
shop.add_product(x)
assert shop.goods[1] == x, "метод add_product отработал некоректно"

# проверка remove_product


shop.remove_product(x)
assert x not in shop.goods, "метод remove_product отработал некоректно"

try:
    del x.id
except AttributeError:
    assert True
else:
    assert False, "не сгенерировалось исключение AttributeError при попытке удаления из продукта, атрибута id"

print("Правильный ответ !")

