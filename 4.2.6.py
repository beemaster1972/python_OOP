class Tuple(tuple):

    def __add__(self, other):
        if not isinstance(other, tuple):
            if not hasattr(other, '__iter__'):
                raise TypeError('Операция сложения возможна только с итерируемыми объектами')
            other = tuple(other)
        return Tuple(super().__add__(other))


if __name__ == '__main__':
    t = Tuple([1, 2, 3])
    t = t + 'Python'
    print(t)
    t = (t + "Python") + "ООП"
    print(t)
    t = t + 123
