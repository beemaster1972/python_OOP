class ListInteger(list):

    def __init__(self, *args):
        if not all(map(lambda x: isinstance(x, int), *args)):
            raise TypeError('можно передавать только целочисленные значения')
        super().__init__(*args)

    def __setitem__(self, key, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        super().__setitem__(key, value)

    def append(self, value):
        if not isinstance(value, int):
            raise TypeError('можно передавать только целочисленные значения')
        super().append(value)


if __name__ == '__main__':
    s = ListInteger((1, 2, 3))
    s[1] = 10
    s.append(11)
    print(s)
    s[0] = 10.5  # TypeError
