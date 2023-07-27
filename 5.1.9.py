class Triangle:

    def __init__(self, a, b, c):
        self.__check_atrr(a, b, c)
        self._a, self._b, self._c = a, b, c

    def __check_atrr(self, *args):
        if not all([type(arg) in (int, float) and arg > 0 for arg in args]):
            raise TypeError('стороны треугольника должны быть положительными числами')
        a, b, c = args
        condition = [a + b > c, a + c > b, b + c > a]
        if not all(condition):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

    def __repr__(self):
        return f'Triangle({self._a},{self._b},{self._c})'

if __name__ == '__main__':
    input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]
    lst_tr = []
    for sides in input_data:
        try:
            lst_tr.append(Triangle(*sides))
        except:
            pass
    print(lst_tr)