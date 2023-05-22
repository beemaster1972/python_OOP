class Thing:

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __setattr__(self, key, value):
        if key == 'name' and not isinstance(value, str):
            raise TypeError("Name должно быть str")
        elif key == 'mass' and not isinstance(value, (int, float)):
            raise TypeError('Mass должна быть int или float')
        object.__setattr__(self, key, value)

    def __hash__(self):
        return hash(self.name.lower() + str(self.mass))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __str__(self):
        return self.name.lower()+str(self.mass)


class Box:

    def __init__(self, *args):
        self.things = []
        if len(args):
            self.things.extend(list(args))

    def add_thing(self, thing):
        self.things.append(thing)

    def get_things(self):
        return self.things

    def __hash__(self):
        lst = sorted(self.things, key=hash)
        lst = [str(x) for x in lst]
        return hash(''.join(lst))

    def __eq__(self, other):
        return hash(self) == hash(other)

a = Thing('Mel', 10)
b = Thing('TabLe', 20.1)
c = Thing('AbRaKaDabra', 30.54562)
b1 = Box(a, b, c)
b2 = Box(c, b, a, b, c)

print(hash(b1), hash(b2), b1 == b2, sep='\n')

# TEST-TASK___________________________________
b1 = Box()
b2 = Box()
assert hasattr(Box, "add_thing") and callable(b1.add_thing), "объявите метод add_thing"
assert hasattr(Box, "get_things") and callable(b1.get_things), "объявите метод get_things"

temp = Thing('мел', 100)
temp2 = Thing('мел', 100)
temp3 = Thing('мел', 101)
assert hasattr(temp, "name"), "ошибка в объекте класса Thing - name"
assert hasattr(temp, "mass"), "ошибка в объекте класса Thing - mass"
assert type(temp.name) is str, "значение в name должно быть строкой"
assert type(temp.mass) in (int, float), "значение в mass должно быть (int, float)"

assert hasattr(temp, "__eq__"), "ошибка в объекте класса Thing отсутствует метод __eq__"
assert temp == temp2, "ошибка в методе сравнения obj == obj1 (__eq__)"
assert temp != temp3, "ошибка в методе сравнения obj != obj1"

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))
#
b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

assert hasattr(b2, "__eq__"), "ошибка в объекте класса Box отсутствует метод __eq__"
assert b1 == b2, "ошибка при сравнении двух ящиков box1 == box2\n" \
                 "Ящики считаются равными, если одинаковы их содержимое\n" \
                 "(для каждого объекта класса Thing одного ящика и можно найти ровно один равный объект из второго ящика)"

b2.add_thing(Thing('доска', 2001))
assert b1 != b2, "ошибка при сравнении двух ящиков box1 != box2"
print("Правильный ответ )")