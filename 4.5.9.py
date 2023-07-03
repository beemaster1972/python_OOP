import time
from random import random, randint


class PointTrack:
    __slots__ = ('__x', '__y', '__next', '__prev')

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__next = self.__prev = None

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, value):
        self.__prev = value

    def __setattr__(self, key, value):
        if key in ('_PointTrack__next', '_PointTrack__prev') and not (isinstance(value, PointTrack) or value is None):
            raise TypeError(f"Ошибочный атрибут указателя {value}")
        elif key in ('_PointTrack__x', '_PointTrack__y') and not isinstance(value, (int, float)):
            raise TypeError('координаты должны быть числами')
        object.__setattr__(self, key, value)

    def __repr__(self):
        return f'PointTrack: {self.__x}, {self.__y}'


class Track:

    def __init__(self, *args):
        if type(args[0]) in (int, float) and type(args[1]) in (int, float):
            self.top = self.tail = PointTrack(args[0], args[1])
            slice = 2
        else:
            slice = 0
            self.top = self.tail = None
        for pt in args[slice:]:
            self.add_back(pt)
        self.__points = []

    def add_back(self, point):
        if not self.tail:
            self.top = self.tail = point
            return
        point.prev = self.tail
        self.tail.next = point
        self.tail = point

    def add_front(self, point):
        if not self.top:
            self.top = self.tail = point
            return
        self.top.prev = point
        point.next = self.top
        self.top = point

    def pop_front(self):
        if not self.top:
            return None
        point = self.top
        self.top = self.top.next
        self.top.prev = None
        return point

    def pop_back(self):
        if not self.tail:
            return None
        point = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        return point

    @property
    def points(self):
        point = self.top
        lst = [point]
        while point.next:
            point = point.next
            lst.append(point)
        return tuple(lst)


if __name__ == '__main__':
    # seed(1)
    complexity = 100_000
    start = time.time()
    track = Track(random() * randint(-10, 10), random() * randint(-10, 10),
                  PointTrack(random(), random()), PointTrack(random(), random()))
    for _ in range(complexity):
        track.add_back(PointTrack(random() * _, random() * _))
    for _ in range(complexity):
        track.add_front(PointTrack(-1 * random() * _, -1 * random() * _))
    elapsed_time_dll = time.time() - start
    print(f'complexity = {complexity}. Doubly linked list: {elapsed_time_dll}')
    start = time.time()
    track_lst = []
    track = Track(random() * randint(-10, 10), random() * randint(-10, 10),
                  PointTrack(random(), random()), PointTrack(random(), random()))
    for _ in range(complexity):
        track_lst.append(PointTrack(random() * _, random() * _))
    for _ in range(complexity):
        track_lst.insert(0, PointTrack(-1 * random() * _, -1 * random() * _))
    elapsed_time_lst = time.time() - start
    print(f'complexity = {complexity}. List: {elapsed_time_lst}')
    # for i, point in enumerate(track.points):
    # if i == randint(0, complexity):
    # print(point)

    # track.pop_back()
    # print('after pop_back')
    # for point in track.points:
    #     print(point)
    # track.pop_front()
    # print('after pop_front')
    # for point in track.points:
    #     print(point)
