class IterColumn:

    def __init__(self, lst, column):
        self.lst = lst
        self.column = column
        self._index = -1

    def __iter__(self):
        self._index = -1
        return self

    def __next__(self):
        self._index += 1
        if self._index < len(self.lst):
            return self.lst[self._index][self.column]
        else:
            raise StopIteration


if __name__ == '__main__':
    N, M = 3, 10
    lst = [list(range(M)) for _ in range(N)]
    for el in lst:
        print(el)

    it = IterColumn(lst, 2)
    for el in it:
        print(el)
