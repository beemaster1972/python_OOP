class Validator:
    """ Класс Validator
    ****************************************************************************
     Инициализация:
        valid = Validator(min_val, max_vol, type_v), где:
        min_val, max_val - минимальное и максимальное значение
        type_v - тип сравниваемого значения (строка, целое, float и т.п. или кортеж, список типов)
    ****************************************************************************
    Вызов валидатора:
        valid.validator(value), где
        valiue - проверяемое значение.
        P.S. value in [min_val, max_val]"""

    def __init__(self, min_val=0, max_val=0, type_v=str):
        self.type_v = type_v
        self.min_val = min_val
        self.max_val = max_val

    def validator(self, value):
        if type(value) in (int, float):
            check_val = value
        elif type(value) in (str, list, tuple, dict, set):
            check_val = len(value)
        return isinstance(value, self.type_v) and self.min_val <= check_val <= self.max_val


class StringValue:

    def __init__(self, *args, validator=Validator, **kwargs):

        if len(args) > 0:
            self.min_length = args[0]
            self.max_length = args[1]
        elif len(kwargs) > 0:
            self.min_length = kwargs['min_length']
            self.max_length = kwargs['max_length']
        else:
            self.min_length = 2
            self.max_length = 50

        self.validator = validator(self.min_length, self.max_length).validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validator(value):
            instance.__dict__[self.name] = value


class PriceValue:

    def __init__(self, max_value=10000, validator=Validator):
        self.max_value = max_value
        self.validator = validator(0, self.max_value, type_v=(int, float)).validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validator(value):
            instance.__dict__[self.name] = value


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


class SuperShop:

    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.goods.append(product)

    def remove_product(self, product):
        if isinstance(product, Product):
            self.goods.pop(self.goods.index(product))


shop = SuperShop("У Балакирева")
shop.add_product(Product("name", 100))
shop.add_product(Product("name", 100))
assert shop.name == "У Балакирева", "атрибут name объекта класса SuperShop содержит некорректное значение"

for p in shop.goods:
    assert p.price == 100, "дескриптор price вернул неверное значение"
    assert p.name == "name", "дескриптор name вернул неверное значение"

t = Product("name 123", 1000)
shop.add_product(t)
shop.remove_product(t)
assert len(shop.goods) == 2, "неверное количество товаров: возможно некорректно работают методы add_product и remove_product"

assert hasattr(shop.goods[0], 'name') and hasattr(shop.goods[0], 'price')

t = Product(1000, "name 123")
if hasattr(t, '_name'):
    assert type(t.name) == str, "типы поля name должнен быть str"
if hasattr(t, '_price'):
    assert type(t.price) in (int, float), "тип поля price должнен быть int или float"