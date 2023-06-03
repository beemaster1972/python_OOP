class Track:

    def __init__(self, start_x, start_y):
        self.__start_x = start_x
        self.__start_y = start_y
        self.__points = []

    def add_point(self, x, y, speed):
        self.__points.append([(x, y), speed])

    def __check_index(self, item):
        if isinstance(item, int) and 0 <= item < len(self):
            return True
        else:
            raise IndexError(f'некорректный индекс {item}')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.__points[item]

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.__points[key][-1] = value

    def __len__(self):
        return len(self.__points)

    def __str__(self):
        return '\n'.join(map(str, self.__points))


tr = Track(0, 0)
tr.add_point(10, 10, 20)
tr.add_point(20, 30, 15)
print(tr[0])
с, speed = tr[1]
print(с, speed)
tr[0] = 1.2
print(tr)
