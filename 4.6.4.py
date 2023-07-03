class Digit:
    _CONDITIONS = [True]
    __slots__ = 'value'

    def __init__(self, value):
        self.value = value

    def __setattr__(self, key, value):
        if all(self._CONDITIONS):
            object.__setattr__(self, key, value)
        else:
            raise TypeError(f'значение {value} не соответствует типу объекта')


class Integer(Digit):
    _CONDITIONS = [isinstance()]