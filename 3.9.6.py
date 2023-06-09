class IterTriangle:

    def __init__(self, lst, limiter):
        self.lst = lst
        self.index = -1
        self.limiter = limiter + 1

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index < self.limiter:
            return self.lst[self.index]
        raise StopIteration


class TriangleListIterator:

    def __init__(self, lst):
        self.lst = lst
        self._index = -1

    def __iter__(self):
        self._index = -1
        return self

    def __next__(self):
        self._index += 1
        if self._index < len(self.lst):
            return IterTriangle(self.lst[self._index], self._index)
        raise StopIteration


if __name__ == '__main__':
    lst = [list(range(11)) for i in range(10)]
    print('List')
    for row in lst:
        for el in row:
            print(el, end=' ')
        print()
    tr = TriangleListIterator(lst)
    print('Triangle list')
    for row in tr:
        for el in row:
            print(el, end=' ')
        print()