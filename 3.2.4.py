class LengthValidator:

    def __init__(self, min_len, max_len):
        self.min_length = min_len
        self.max_length = max_len

    def __call__(self, *args, **kwargs):
        return isinstance(args[0], str) and self.min_length <= len(args[0]) <= self.max_length


class CharsValidator:

    def __init__(self, chars):
        self.chars = chars

    def __call__(self, *args, **kwargs):
        return isinstance(args[0], str) and set(args[0]).issubset(set(self.chars))


# TEST-TASK___________________________________
try:
    issubclass(LengthValidator, object)
except NameError:
    print("Вы не создали класс - LengthValidator")

try:
    issubclass(CharsValidator, object)
except NameError:
    print("Вы не создали класс - CharsValidator")

# проверка создания объекта LengthValidator
lv = LengthValidator(2, 5)
assert callable(lv), "валидатор LengthValidator не вызываться как функция"
assert not lv('123456'), 'ошибка в LengthValidator, проверяемая строка выходит за заданный диапазон длины знаков'

# проверка создания объекта CharsValidator
cv = CharsValidator('abc')
assert callable(cv), "валидатор CharsValidator не вызываться как функция"
assert not cv('1'), "ошибка в CharsValidator, проверяемая строка содержит недопустимые знаки"
print("Отлично, так держать !!")