class Validator:

    def _is_valid(self, value):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):

    def __init__(self, min_val, max_val):
        self.__min_val = min_val
        self.__max_val = max_val

    def _is_valid(self, value):
        conditions = [tf := isinstance(value, float), self.__min_val <= value <= self.__max_val if tf else False]
        return all(conditions)

    def __call__(self, value):
        return self._is_valid(value)


if __name__ == '__main__':
    float_validator = FloatValidator(0, 10.5)
    res_1 = float_validator(1)  # False (целое число, а не вещественное)
    res_2 = float_validator(1.0)  # True
    res_3 = float_validator(-1.0)  # False (выход за диапазон [0; 10.5])
