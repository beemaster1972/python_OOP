class PrimaryKeyError(Exception):

    def __init__(self, *args, **kwargs):
        self._message = "Первичный ключ должен быть целым неотрицательным числом"
        if len(kwargs) > 0:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def __setattr__(self, key, value):
        if key != '_message':
            setattr(self, "_message", f"Значение первичного ключа {key} = {value} недопустимо")
        object.__setattr__(self, key, value)

    def __str__(self):
        return self._message


if __name__ == '__main__':
    e = PrimaryKeyError(id=-10.5)
    assert issubclass(PrimaryKeyError, Exception), "класс PrimaryKeyError должен наследоваться от класса Exception"

    e1 = PrimaryKeyError(id=1)
    e2 = PrimaryKeyError(pk=2)
    e3 = PrimaryKeyError()

    assert str(e1) == "Значение первичного ключа id = 1 недопустимо", f"неверное сообщение для исключения объекта класса PrimaryKeyError {str(e1)}"
    assert str(e2) == "Значение первичного ключа pk = 2 недопустимо", f"неверное сообщение для исключения объекта класса PrimaryKeyError {str(e2)}"
    assert str(e3) == "Первичный ключ должен быть целым неотрицательным числом", f"неверное сообщение для исключения объекта класса PrimaryKeyError {str(e3)}"