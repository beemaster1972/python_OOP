# здесь объявляйте классы CellException, CellIntegerException, CellFloatException, CellStringException
class CellException(Exception): ...
class CellIntegerException(CellException): ...
class CellFloatException(CellException): ...
class CellStringException(CellException): ...

# здесь объявляйте классы CellInteger, CellFloat, CellString


class Cell:
    VAL_TYPE = None
    CELL_EXCEPTION = Exception

    def __init__(self, min_val, max_val):
        self._min_value = min_val
        self._max_value = max_val
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __setattr__(self, key, value):
        if key not in ('_min_value', '_max_value') and not self._check_value(value):
            raise self.CELL_EXCEPTION('значение выходит за допустимый диапазон')
        object.__setattr__(self, key, value)

    def _check_value(self, value):
        if value is None:
            return True
        conditions = [type(value) == self.VAL_TYPE, self._min_value <= value <= self._max_value]
        return all(conditions)


class CellInteger(Cell):
    VAL_TYPE = int
    CELL_EXCEPTION = CellIntegerException


class CellFloat(Cell):
    VAL_TYPE = float
    CELL_EXCEPTION = CellFloatException


class CellString(Cell):
    VAL_TYPE = str
    CELL_EXCEPTION = CellStringException

    def _check_value(self, value):
        if value is None:
            return True
        conditions = [type(value) == self.VAL_TYPE, self._min_value <= len(value) <= self._max_value]
        return all(conditions)


# здесь объявляйте класс TupleData


class TupleData:

    def __init__(self, *args):
        conditions = [type(x) in (CellInteger, CellFloat, CellString) for x in args]
        if not all(conditions):
            raise CellException('Неверный тип аргумента')
        self._data = args

    def __len__(self):
        return len(self._data)

    def __check_index(self, key):
        if not (type(key) == int and 0 <= key < len(self)):
            raise IndexError(f'Неверный индекс {key}')
        return key

    def __getitem__(self, key):
        key = self.__check_index(key)
        return self._data[key]

    def __setitem__(self, key, value):
        key = self.__check_index(key)
        self._data[key].value = value

    def __iter__(self):
        for el in self._data:
            yield el.value

# эти строчки в программе не менять!


ld = TupleData(CellInteger(0, 10), CellInteger(11, 20), CellFloat(-10, 10), CellString(1, 100))

try:
    ld[0] = 1
    ld[1] = 20
    ld[2] = -5.6
    ld[3] = "Python ООП"
except CellIntegerException as e:
    print(e)
except CellFloatException as e:
    print(e)
except CellStringException as e:
    print(e)
except CellException as e:
    print("Ошибка при обращении к ячейке")
    print(e)
except Exception as e:
    print("Общая ошибка при работе с объектом TupleData")
    print(e)

if __name__ == '__main__':
    t = TupleData(CellInteger(-10, 10), CellInteger(0, 2), CellString(5, 10))

    d = (1, 0, 'sergey')
    t[0] = d[0]
    t[1] = d[1]
    t[2] = d[2]
    for i, x in enumerate(t):
        assert x == d[i], "объект класса TupleData хранит неверную информацию"

    assert len(t) == 3, "неверное число элементов в объекте класса TupleData"

    cell = CellFloat(-5, 5)
    try:
        cell.value = -6.0
    except CellFloatException:
        assert True
    else:
        assert False, "не сгенерировалось исключение CellFloatException"

    cell = CellInteger(-1, 7)
    try:
        cell.value = 8
    except CellIntegerException:
        assert True
    else:
        assert False, "не сгенерировалось исключение CellIntegerException"

    cell = CellString(5, 7)
    try:
        cell.value = "hello world"
    except CellStringException:
        assert True
    else:
        assert False, "не сгенерировалось исключение CellStringException"

    assert issubclass(CellIntegerException, CellException) and issubclass(CellFloatException,
                                                                          CellException) and issubclass(
        CellStringException,
        CellException), "классы CellIntegerException, CellFloatException, CellStringException должны наследоваться от класса CellException"
    print('Всё отлично!!!')