class Dimensions:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        object.__setattr__(self, key, value)

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __gt__(self, other):
        return hash(self) > hash(other)

    def __ge__(self, other):
        return hash(self) >= hash(other)

    def __lt__(self, other):
        return hash(self) < hash(other)

    def __le__(self, other):
        return hash(self) <= hash(other)

    def __repr__(self):
        return f'{self.a} {self.b} {self.c}'

s_inp = input()  # эту строку (переменную s_inp) в программе не менять
lst_dims = list(map(str.strip, s_inp.split(';')))
lst_dims = [list(x.split()) for x in lst_dims]
for i, dims in enumerate(lst_dims):
    for j, dim in enumerate(dims):
        try:
            lst_dims[i][j] = int(dim)
        except:
            lst_dims[i][j] = float(dim)
lst_dims = [Dimensions(x[0], x[1], x[2]) for x in lst_dims]
lst_dims.sort(key=hash)
print(*lst_dims)