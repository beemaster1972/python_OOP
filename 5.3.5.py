class Test:

    def __init__(self, descr):
        if not 10 <= len(descr) <= 10_000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):

    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        self._ans_digit = ans_digit
        self._max_error_digit = max_error_digit

    def __setattr__(self, key, value):
        if key == 'descr':
            object.__setattr__(self, key, value)
            return
        conditions = [type(value) in (int, float), value >= 0 if key == '_max_error_digit' else True]
        if not all(conditions):
            raise ValueError('недопустимые значения аргументов теста')
        object.__setattr__(self, key, value)

    def run(self):
        ans = float(input())
        conditions = [
            self._ans_digit - self._max_error_digit <= ans <= self._ans_digit + self._max_error_digit]
        return all(conditions)


if __name__ == '__main__':
    descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
    ans = float(ans)  # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может
    try:
        test = TestAnsDigit(descr, ans)
        print(test.run())
    except Exception as e:
        print(e)
    try:
        test = Test('descr')
    except ValueError:
        assert True
    else:
        assert False, "не сгенерировалось исключение ValueError при вызове инициализатора класса Test с неверным набором аргументов"

    try:
        test = Test('descr ghgfhgjg ghjghjg')
        test.run()
    except NotImplementedError:
        assert True
    else:
        assert False

    assert issubclass(TestAnsDigit, Test)

    t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1)
    t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, 0.5)

    try:
        t = TestAnsDigit('ffhgfh fghfghfghfggfhfghfh', 1, -0.5)
    except ValueError:
        assert True
    else:
        assert False
