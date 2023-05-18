import numpy as np


class MaxPooling:

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
        if not (all([isinstance(row, list) and len(row) == len(matrix[0])for row in matrix]) and
                all([isinstance(x, (int, float)) for row in matrix for x in row])):
            raise ValueError("Неверный формат для первого параметра matrix.")
        res = []
        sub_rows = self.size[1]
        sub_columns = self.size[0]
        s_row = self.step[1]
        s_col = self.step[0]
        for i in range(0, (len(matrix) // self.size[1])+1, self.step[1]):
            res1 = []
            sub_rows += s_row*i
            for j in range(0, (len(matrix[0]) // self.size[0])+1, self.step[0]):
                sub_columns += s_col*j
                intermediate_res = [x for row in matrix[i:sub_rows] for x in row[j:sub_columns]]
                try:
                    res1.append(max(intermediate_res))
                except ValueError:
                    pass
            res.append(res1)
        return res

    def __call__(self, *args, **kwargs):
        return self.__pooling(args[0])


a = MaxPooling()
matrix = np.array(range(100), int)
matrix = [x for row in np.reshape(matrix, (10, 10)) for x in row]
print(matrix)
print(a(matrix), max(matrix))
