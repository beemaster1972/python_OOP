class Value:

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value if self.check(value) else 0
    @staticmethod
    def check(value):
        return isinstance(value, (int, float))


class Track:
    start_x = Value()
    start_y = Value()
    track_length = Value()

    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.__tracks = []
        self.__segment_lengths = []
        self.track_length = 0

    def add_track(self, tr):
        start = (self.__tracks[-1].to_x, self.__tracks[-1].to_y) if self.track_length else (self.start_x, self.start_y)
        length = ((tr.to_x - start[0]) ** 2 + (tr.to_y - start[1]) ** 2) ** (1 / 2)
        self.__tracks.append(tr)
        self.__segment_lengths.append(length)
        self.track_length += round(length)

    def get_tracks(self):
        return tuple(self.__tracks)

    @staticmethod
    def get_length(other):
        return other.track_length if isinstance(other, Track) else other

    def __eq__(self, other):
        l = self.get_length(other)
        return self.track_length == l

    def __gt__(self, other):
        l = self.get_length(other)
        return self.track_length > l

    def __len__(self):
        return self.track_length


class TrackLine:
    to_x = Value()
    to_y = Value()
    max_speed = Value()

    def __init__(self, to_x, to_y, max_speed=0):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1 = Track(0, 0)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2 = Track(0, 1)
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2

# TEST-TASK___________________________________
# ВНИМАНИЕ - тест работает только в случае, что у экземпляра класса Track будут локальные атрибуты с именами start_x, start_y
from math import sqrt


# метод подсчета длинны отрезков по формуле
# sqrt(pow(x0 - x1, 2) + pow(y0 - y1, 2)) формула подсчёта длины маршрута
def sum_len_points(obj):
    distance = 0
    # определяем название списка координат
    key = str(*(i for i, v in track1.__dict__.items() if type(v) is list or type(v) is tuple))

    for _i in range(len(obj.__dict__[key])):
        # если это начало списка
        if _i == 0:
            distance += sqrt(pow(obj.start_x - obj.__dict__[key][_i].to_x, 2) +
                             pow(obj.start_y - obj.__dict__[key][_i].to_y, 2))
            # начало цикла со второго элемента, что бы просуммировать полное расстояние между точками.
        else:
            _a = obj.__dict__[key][_i].to_x, obj.__dict__[key][_i].to_y
            _b = obj.__dict__[key][_i - 1].to_x, obj.__dict__[key][_i - 1].to_y
            distance += sqrt(sum(pow(i[0] - i[1], 2) for i in zip(_b, _a)))

    return distance


track3 = Track(0, 0)
assert hasattr(track3, "add_track") and hasattr(track3, "get_tracks"), "не все методы объявлены в экземпляре класса"
assert hasattr(track3, "start_x") and hasattr(track3, "start_y"), "ошибка локальных атрибутах start_x и start_y"
assert type(track3.start_x) in (int, float) and type(track3.start_y) in (
    int, float), "начальные координаты могут быть только int или float"

p1 = TrackLine(2, 4, 100)
assert type(p1.__dict__['to_x']) in (int, float) and type(p1.__dict__['to_y']) in (
    int, float), "to_x и to_y могут быть толко int или float"
assert type(p1.__dict__["max_speed"]) is int, "max_speed может бsть только типом int"

# add_track(self, tr) - добавление линейного сегмента маршрута (следующей точки);
track3.add_track(p1)
assert len(track3.get_tracks()) == 1 and track3.get_tracks()[0] == p1, "метод add_track работает неверно"

# get_tracks(self) - получение кортежа из объектов класса TrackLine.
assert len(track3.get_tracks()) == 1 and type(track3.get_tracks()) is tuple, "метод get_tracks должен вернуть кортеж"
assert all(True if isinstance(_, TrackLine) else False for _ in track3.get_tracks()), \
    "метод get_tracks вернул кортеж, но в коллекции должны быть только объекты класса TrackLine"

# Также для объектов класса Track должны быть реализованные следующие операции сравнения:
# track1 == track2  # маршруты равны, если равны их длины
assert (track1 == track2) is False and (sum_len_points(track1) == sum_len_points(track2)) is False, \
    "ошибка при операции =="

# track1 != track2  # маршруты не равны, если не равны их длины
assert (track1 != track2) is True and sum_len_points(track1) != sum_len_points(track2), "ошибка при операции !="

# track1 > track2   # True, если длина пути для track1 больше, чем для track2
assert (track1 > track2) is True and sum_len_points(track1) > sum_len_points(track2), "ошибка при операции  >"

# track1 < track2   # True, если длина пути для track1 меньше, чем для track2
assert (track1 < track2) is False and (sum_len_points(track1) < sum_len_points(track2)) is False, \
    "ошибка при операции  <"

# И функция:
# n = len(track) # возвращает целочисленную длину маршрута (привести к типу int) для объекта track
assert type(len(track1)) is int and len(track1) == 13, "ошибка в методе len()"

assert res_eq is False, "при сравнени вернулся неверный результат"

print("Правильный ответ )!")
