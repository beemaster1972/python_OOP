class FloatValue:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.__check_value(value)
        instance.__dict__[self.name] = value

    @classmethod
    def __check_value(cls, value):
        if not isinstance(value, float):
            raise TypeError("Присваивать можно только вещественный тип данных.")

class Cell:

    value = FloatValue()

    def __init__(self, start_value=0.0):
        self.value = start_value

class TableSheet:

    def __init__(self, N, M):
        self.cells = []
        for i in range(N):
            self.cells.append([])
            for j in range(M):
                self.cells[i].append(Cell())


N, M = 5, 3
table = TableSheet(N, M)
count = 1.0
for i in range(N):
    for j in range(M):
        table.cells[i][j].value = count
        count += 1.0

res = [int(x.value) for row in table.cells for x in row]
print(*res)
for i in range(N):
    print()
    for j in range(M):
        print(table.cells[i][j].value, end=' ')



