class Validator:

    def _is_valid(self, data):
        return True

    def __call__(self, *args, **kwargs):
        if not self._is_valid(args[0]):
            raise ValueError('данные не прошли валидацию')
        return args[0]


class IntegerValidator(Validator):

    def __init__(self, min_val: int, max_val: int):
        self.min_val = min_val
        self.max_val = max_val

    def _is_valid(self, data):
        return isinstance(data, int) and self.min_val <= data <= self.max_val


class FloatValidator(Validator):

    def __init__(self, min_val: float, max_val: float):
        self.min_val = min_val
        self.max_val = max_val

    def _is_valid(self, data):
        return isinstance(data, float) and self.min_val <= data <= self.max_val


if __name__ == '__main__':
    integer_validator = IntegerValidator(-10, 10)
    float_validator = FloatValidator(-1, 1)
    res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
    res2 = float_validator(10)  # исключение ValueError