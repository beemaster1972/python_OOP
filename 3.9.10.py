class Matrix:

    def __init__(self, *args):
        if len(args) == 3:
            if not isinstance(args[2], (int, float)) and not all(
                    [isinstance(args[i], int) and args[i] > 0 for i in (0, 1)]):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.__coords = (args[0], args[1])
            self.__matrix = [[args[2] for j in range(args[1])] for i in range(args[0])]
        else:
            if not (isinstance(args[0], list) and isinstance(args[0][0], list)) or not all(
                    [len(row) == len(args[0][i - 1]) for i, row in enumerate(args[0])]) or not all(
                    [isinstance(el, (int, float)) for row in args[0] for el in row]):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            self.__matrix = args[0]
            self.__coords = (len(args[0]), len(args[0][0]))

    def __repr__(self):
        return f'Matrix({self.__coords[0]}, {self.__coords[1]}, {self[(0, 0)]})'

    def __check_index(self, item):
        if not isinstance(item, tuple) or not all(
                [isinstance(item[i], int) and 0 <= item[i] < self.__coords[i] for i in (0, 1)]):
            raise IndexError('недопустимые значения индексов')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.__matrix[item[0]][item[1]]

    def __setitem__(self, key, value):
        self.__check_index(key)
        if not isinstance(value, (int, float)):
            raise TypeError('значения матрицы должны быть числами')
        self.__matrix[key[0]][key[1]] = value

    def get_coords(self):
        return self.__coords

    def __get_other(self, other):
        if isinstance(other, Matrix) and self.__coords != other.get_coords():
            raise ValueError('операции возможны только с матрицами равных размеров')

        if isinstance(other, (int, float)):
            res = Matrix(*self.__coords, other)
        elif isinstance(other, Matrix):
            res = other
        return res

    def __add__(self, other):
        other = self.__get_other(other)
        return Matrix(
            [[self[(i, j)] + other[(i, j)] for j in range(self.__coords[1])] for i in range(self.__coords[0])])

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = self.__get_other(other)
        return Matrix(
            [[self[(i, j)] - other[(i, j)] for j in range(self.__coords[1])] for i in range(self.__coords[0])])

    def __rsub__(self, other):
        other = self.__get_other(other)
        return Matrix(
            [[other[(i, j)] - self[(i, j)] for j in range(self.__coords[1])] for i in range(self.__coords[0])])


if __name__ == '__main__':
    list2D = [[1, 2], [3, 4], [5, 6, 7]]
    try:
        st = Matrix(list2D)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

    list2D = [[1, []], [3, 4], [5, 6]]
    try:
        st = Matrix(list2D)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

    try:
        st = Matrix('1', 2, 0)
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

    list2D = [[1, 2], [3, 4], [5, 6]]
    matrix = Matrix(list2D)
    assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

    matrix = Matrix(4, 5, 10)
    assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

    try:
        v = matrix[3, -1]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    try:
        v = matrix['0', 4]
    except IndexError:
        assert True
    else:
        assert False, "не сгенерировалось исключение IndexError"

    matrix[0, 0] = 7
    assert matrix[0, 0] == 7, "неверно отработал __setitem__"

    try:
        matrix[0, 0] = 'a'
    except TypeError:
        assert True
    else:
        assert False, "не сгенерировалось исключение TypeError в __setitem__"

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 1], [1, 1], [1, 1]])

    try:
        matrix = m1 + m2
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[1, 1], [1, 1]])
    matrix = m1 + m2
    assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
    assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
    assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
           and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

    m1 = Matrix(2, 2, 1)
    id_m1_old = id(m1)
    m2 = Matrix(2, 2, 1)
    m1 = m1 + m2
    id_m1_new = id(m1)
    assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

    matrix = Matrix(2, 2, 0)
    m = matrix + 10
    assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
    assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

    m1 = Matrix(2, 2, 1)
    m2 = Matrix([[0, 1], [1, 0]])
    identity_matrix = m1 - m2  # должна получиться единичная матрица
    assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
           and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
    assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

    matrix = Matrix(2, 2, 1)
    m = matrix - 1
    assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
    assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"
    print('Всё отлично!!!')
