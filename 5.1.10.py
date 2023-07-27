class Validator:
    VAL_TYPE = None

    def __init__(self, min_val, max_val):
        self._min_val = min_val
        self._max_val = max_val

    def __call__(self, checked_value):
        condition = [type(checked_value) == self.VAL_TYPE, self._min_val <= checked_value <= self._max_val]
        if not all(condition):
            raise ValueError('значение не прошло валидацию')
        return checked_value


class FloatValidator(Validator):
    VAL_TYPE = float


class IntegerValidator(Validator):
    VAL_TYPE = int


def is_valid(lst, validators):
    res = []
    for el in lst:
        for validator in validators:
            try:
                res.append(validator(el))
            except:
                pass
    return res

if __name__ == '__main__':
    fv = FloatValidator(0, 10.5)
    iv = IntegerValidator(-10, 20)
    lst_out = is_valid([1, 4.5, -10.5, 100, True, 'abc', (1, 2)], validators=[fv, iv])  # [1, 4.5]
    print(lst_out)