class Body:
    ro = 0.0
    volume = 0.0

    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.__weight = self.ro * self.volume

    def __setattr__(self, key, value):
        if key == 'name' and not isinstance(value, str):
            raise TypeError(f"Значение {key} должно быть str")
        elif key in ('ro', 'volume') and not isinstance(value, (int, float)):
            raise TypeError(f"Значение {key} должно быть int или float")
        object.__setattr__(self, key, value)
        if key in ('ro', 'volume'):
            object.__setattr__(self, '_Body__weight', self.ro * self.volume)

    def get_other(self, other):
        res = other.__weight if isinstance(other, self.__class__) else other
        return res

    def __eq__(self, other):
        weight = self.get_other(other)
        return self.__weight == weight

    def __gt__(self, other):
        weight = self.get_other(other)
        return self.__weight > weight

    def __ge__(self, other):
        weight = self.get_other(other)
        return self.__weight >= weight

    def __lt__(self, other):
        weight = self.get_other(other)
        return self.__weight < weight

    def __le__(self, other):
        weight = self.get_other(other)
        return self.__weight <= weight

    def __str__(self):
        return f'{self.name}  плотность = {self.ro} объём = {self.volume} масса = {self.__weight}'


# TEST-TASK___________________________________
a = Body('Lora', 10, 10)
b = Body('Dora', 20, 20)
assert hasattr(a, "name") and hasattr(a, "ro") and hasattr(a, "volume"), "ошибка в локальных атрибутах"
assert type(a.name) is str, "name может быть только строкой"
assert type(a.ro) in (int, float), "ro  должно быть int или float"
assert type(a.volume) in (int, float), "volume  должно быть int или float"
assert not a > b, "ошибка при сравнении объектов >"
assert a < b, "ошибка при сравнении объектов <"
assert 10 < a, "ошибка при сравнении число < объект"
assert not 10 > a, "ошибка при сравнении число > объект"
assert not a == 5, "ошибка при сравнении объект == число"
assert a != 5, "ошибка при сравнении объект != число"
a.ro = 5.23
a.volume = 4.768
b.ro = 4.768
b.volume = 5.23
assert a == b, f"ошибка сравнения float {a} {b}"
print("Правильное решение.")
