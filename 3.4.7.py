class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __setattr__(self, key, value):
        if (key == 'year' and isinstance(value, int)) or (key in ('title', 'author') and isinstance(value, str)):
            object.__setattr__(self, key, value)
        else:
            raise TypeError(f'Неверный тип {type(value)} для {key}')


class Lib:

    def __init__(self):
        self.book_list = []
        self.__length = 0

    def __len__(self):
        return self.__length

    def __add__(self, other):
        self.book_list.append(other)
        self.__length += 1
        return self

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) == int:
            self.book_list.pop(other)
        elif type(other) == Book:
            self.book_list.remove(other)
        self.__length -= 1
        return self

    def __isub__(self, other):
        return self - other


lib = Lib()

lib += Book("1", '1', 1870)
lib = lib + Book('2','2',1900)
assert len(lib) == 2, 'Ошибка при добавлении книг в библиотеку'
lib -= 1
book = Book('3','3', 2000)
lib = lib + book
assert len(lib) == 2, 'Ошибка при добавлении книг в библиотеку'
print (*lib.book_list)