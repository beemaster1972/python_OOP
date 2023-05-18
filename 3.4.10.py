import numpy as np


class MaxPooling:
    # Кортеж валидных типов матрицы
    VALID_MATRiX = (list, np.ndarray)
    # Кортеж валидных элементов матрицы
    VALID_ELEMENTS = (int, float, np.int32, np.int64)

    def __init__(self, step=(2, 2), size=(2, 2)):
        self.__step = step
        self.__size = size

    @property
    def step(self):
        return self.__step

    @property
    def size(self):
        return self.__size

    def __pooling(self, matrix):
        if not (all([isinstance(row, self.VALID_MATRiX) and len(row) == len(matrix[0]) for row in matrix]) and
                all([isinstance(x, self.VALID_ELEMENTS) for row in matrix for x in row])):
            raise ValueError("Неверный формат для первого параметра matrix.")
        res = []
        sub_row = 0  # Инициализируем нижнюю границу окна сканирования
        s_row = self.step[1]  # шаг по вертикали
        s_col = self.step[0]  # шаг по горизантали
        # Исключаем ряды по размеру окна сканирования
        bottom_edge = len(matrix) - len(matrix) % self.size[1]
        for i in range(0, bottom_edge, s_row):
            res1 = []  # Ряд в результирующей матрице
            sub_row += self.size[1]  # Увеличиваем нижнюю границу на размер окна
            sub_column = 0  # Инициализируем правую границу окна сканирования

            # Исключаем колонки по размеру окна сканирования
            right_edge = len(matrix[i]) - len(matrix[i]) % self.size[0]
            for j in range(0, right_edge, s_col):
                sub_column += self.size[0]  # Увеличиваем правую границу на размер окна
                intermediate_res = [x for row in matrix[i:sub_row] for x in row[j:sub_column]]
                if len(intermediate_res) == self.size[0] * self.size[1]:
                    res1.append(max(intermediate_res))
            if res1:
                res.append(res1)
        return res

    def __call__(self, *args, **kwargs):
        return self.__pooling(args[0])


a = MaxPooling(size=(2, 2), step=(2, 2))

m = np.random.randint(-1000, 1000, (7, 8))

# print(m)
# print(np.array(a(m)))

mp = MaxPooling(step=(2, 2), size=(2, 2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2, 2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"
