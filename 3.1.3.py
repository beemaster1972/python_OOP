class Book:

    def __init__(self, title='', author='', pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in ('title', 'author'):
            if isinstance(value, str):
                object.__setattr__(self, key, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")
        else:
            if isinstance(value, int):
                object.__setattr__(self, key, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)


# TEST-TASK___________________________________
assert issubclass(Book, object), "Класс Book не является подклассом object, скорее всего не создан"

assert book.__dict__ == {
    'title': 'Python ООП',
    'author': 'Сергей Балакирев',
    'pages': 123,
    'year': 2022
    }, " Ошибка в атрибутах"
# проверка что метод __setattr__ переопределенн в классе
# если методы не идентичны значит метод непереопределён в классе
assert Book.__setattr__ != object.__setattr__, "Метод __setattr__ не переопределен в классе MyClass"

# проверка атрибутов объекта
assert type(book.title) == str, "title не является строкой"
assert type(book.author) == str, "title не является строкой"
assert type(book.pages) == int, "pages не целое число"
assert type(book.year) == int, "pages не целое число"

# проверка принудительной генерации ошибки
try:
    book.title = 111
except  TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"


try:
    book.pages = '111'
except  TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

print("Правильный ответ !")