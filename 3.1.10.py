import time
class Filter:

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == 'date' and len(self.__dict__) > 0:
            return
        object.__setattr__(self, key, value)


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:

    MAX_DATE_FILTER = 100
    type_of_filters = [Mechanical, Aragon, Calcium]
    def __init__(self):
        self.filters = [None, None, None]

    def add_filter(self, slot_num, filtr):
        if self.type_of_filters[slot_num-1] == type(filtr) and not self.filters[slot_num-1]:
            self.filters[slot_num-1] = filtr

    def remove_filter(self, slot_num):
        self.filters[slot_num-1] = None

    def get_filters(self):
        return (fl for fl in self.filters)

    def water_on(self):
        life_time = [0 <= (time.time() - fl.date) <= self.MAX_DATE_FILTER for fl in self.filters if fl]
        return len(life_time) == 3 and all(life_time)


my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))

assert my_water.water_on() == False, "метод water_on вернул True, хотя не все фильтры были установлены"

my_water.add_filter(3, Calcium(time.time()))
assert my_water.water_on(), "метод water_on вернул False при всех трех установленных фильтрах"

f1, f2, f3 = my_water.get_filters()
assert isinstance(f1, Mechanical) and isinstance(f2, Aragon) and isinstance(f3, Calcium), "фильтры должны быть устанлены в порядке: Mechanical, Aragon, Calcium"

my_water.remove_filter(1)
assert my_water.water_on() == False, "метод water_on вернул True, хотя один из фильтров был удален"

my_water.add_filter(1, Mechanical(time.time()))
assert my_water.water_on(), "метод water_on вернул False, хотя все три фильтра установлены"

f1, f2, f3 = my_water.get_filters()
my_water.remove_filter(1)

my_water.add_filter(1, Mechanical(time.time() - GeyserClassic.MAX_DATE_FILTER - 1))
assert my_water.water_on() == False, "метод water_on вернул True, хотя у одного фильтра истек срок его работы"

f1 = Mechanical(1.0)
f2 = Aragon(2.0)
f3 = Calcium(3.0)
assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "неверное значение атрибута date в объектах фильтров"

f1.date = 5.0
f2.date = 5.0
f3.date = 5.0

assert 0.9 < f1.date < 1.1 and 1.9 < f2.date < 2.1 and 2.9 < f3.date < 3.1, "локальный атрибут date в объектах фильтров должен быть защищен от изменения"