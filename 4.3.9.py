class StringDigit(str):

    def __init__(self, st: str):
        self._check_str(st)
        super().__init__()
        self.__st = st

    def __add__(self, other):
        self._check_str(other)
        return StringDigit(super().__add__(other))

    def __radd__(self, other):
        self._check_str(other)
        return StringDigit(other + self.__st)

    def __iadd__(self, other):
        self._check_str(other)
        return StringDigit(super().__add__(other))

    def _check_str(self, st):
        if not st.isdigit():
            raise ValueError("в строке должны быть только цифры")


if __name__ == '__main__':
    sd = StringDigit("123")
    assert str(sd) == "123", "неверно работает метод __str__ класса StringDigit"

    try:
        sd2 = StringDigit("123a")
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError"

    sd = sd + "345"
    assert sd == "123345", "неверно отработал оператор +"

    sd = "0" + sd
    assert sd == "0123345", "неверно отработал оператор +"

    try:
        sd = sd + "12d"
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"

    try:
        sd = "12d" + sd
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"
    print('Всё отлично!!!')

