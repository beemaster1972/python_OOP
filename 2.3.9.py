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


class NumericalValue:

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



class Bag:

    def __init__(self, max_weight):
        self.__things = []
        self.max_weight = max_weight

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing):
        if isinstance(thing, Thing):
            if self.max_weight >= self.get_total_weight() + thing.weight:
                self.__things.append(thing)

    def remove_thing(self, indx):
        if isinstance(indx, int) and indx < len(self.__things):
            self.__things.pop(indx)

    def get_total_weight(self):
        return sum([th.weight for th in self.__things])

class Thing:
    name = StringValue()
    weight = NumericalValue(1000)

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


# TEST-TASK___________________________________

x_thing = Thing("Книга по Python", 100)

assert hasattr(x_thing, 'name') and hasattr(x_thing, 'weight'), "В классе не созданны локальные атрибуты"

assert type(x_thing.name) is str, "Название должно быть строкой"

assert type(x_thing.weight) is float or type(x_thing.weight) is int, "Вес должен быть числом"

bag = Bag(1000)

assert hasattr(bag, 'max_weight'), "Не создан атрибут max_weight"

assert type(bag.max_weight) is int, "Максимальный суммарный вес вещей должен быть целым числом"

assert '_Bag__things' in bag.__dict__, "Не создан локальный приватный атрибут __things"

assert bag.things == [], "Нет доступа к локальному приватному атрибуту __things"

assert type(bag.things) is list, "__things должен быть списком"

assert len(bag.things) == 0, "__things изначально должен быть пустым"

# проверка add_thing добавление вещей


assert hasattr(bag, "add_thing"), "Не создан метод add_thing"

assert bag.max_weight >= sum(_.weight for _ in bag.things), "Некоректно отработал метод add_thing"

# проверка get_total_weight вес предметов в рюкзаке

assert hasattr(bag, "get_total_weight"), "Не создан метод get_total_weight"

bag.add_thing(Thing("Палатка", 500))

assert bag.get_total_weight() == sum(_.weight for _ in bag.things), "Некоректно отработал метод get_total_weight"

print("Умница правильный ответ !")