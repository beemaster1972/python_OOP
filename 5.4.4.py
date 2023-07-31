class StringException(Exception):
    """String exception"""


class NegativeLengthString(StringException):
    """ошибка, если длина отрицательная"""
    def __str__(self):
        return "Ошибка: длина отрицательная"


class ExceedLengthString(StringException):
    """ошибка, если длина превышает заданное значение"""
    def __str__(self):
        return "Ошибка: длина превышает заданное значение"

if __name__ == '__main__':
    try:
        raise ExceedLengthString("Error")
    except ExceedLengthString as e:
        print(e)
