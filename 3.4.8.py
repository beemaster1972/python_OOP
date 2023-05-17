class Value:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):

        instance.__dict__[self.name] = value if self.check(value, self.condition) else 0


class CheckValue:

    _type = None

    def check(self, value, condition):
        return isinstance(value, self._type) and condition(value)


class StringValue(Value, CheckValue):

    def __init__(self):
        self._type = str

    def condition(self, value):
        return 0 < len(value) <= 50


class NumericalValue(Value, CheckValue):

    def __init__(self):
        self._type = (int, float)

    def condition(self, value):
        return True


class Item:
    name = StringValue()
    money = NumericalValue()

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, item):
        self.__next = item

    def __add__(self, other):
        return self.money + other

    def __radd__(self, other):
        return self + other


class Budget:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_item(self, item):
        if not self.tail:
            self.head = self.tail = item
        else:
            self.tail.next = item
            self.tail = item

    def remove_item(self, indx):
        if not self.head:
            return False
        left = None
        node = right = self.head

        i = 0
        while right:
            right = right.next
            if i == indx:
                if i == 0:
                    self.head = right
                    break
                left.next = right
                break
            i += 1
            left = node
            node = right
        else:
            self.tale = left
            self.tale.next = None

    def get_items(self):
        res = []
        node = self.head
        while node:
            res.append(node)
            node = node.next
        return res


# TEST-TASK___________________________________
my_budget = Budget()
assert hasattr(my_budget, "add_item") and hasattr(my_budget, "remove_item") and hasattr(my_budget, "get_items"), \
    "ошибка в не все методы объявлены в екземпляре класса"

st = Item("Курс по Python ООП", 2000)
assert hasattr(st, "name") and hasattr(st, "money"), "ошибка локальных атрибутов в пункте расхода бюджета"

assert len(my_budget.get_items()) == 0, "метод get_items() работает некорректно"

my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
assert len(my_budget.get_items()) == 2, "метод add_item работает некорректно"

# -remove_item(self, indx) - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);
temp = id(my_budget.get_items()[0])
my_budget.remove_item(1)
assert len(my_budget.get_items()) == 1 and id(my_budget.get_items()[0]) == temp, \
    "метод remove_item удалил не тот объект"

x = Item("Курс по Python ООП", '2000')
assert "2000" not in [_ for _ in x.__dict__.values()], "ошибка атрибут money может быть только int или float"

a = Item("Курс по Python ООП", 2000)
b = Item("Курс по Django", 5000.01)
c = Item("Курс по Python ООП", 2000)
s = a + b
assert s == 7000.01, "ошибка при операции - сумма для двух статей расходов"
s = a + b + c
assert s == 9000.01, "ошибка при операции - сумма N статей расходов"

print("Правильный ответ !!")