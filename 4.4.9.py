# здесь объявляйте декоратор и все что с ним связано
def class_log(log_journal: list):
    def decor(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, class_log_decorated(v))
        return cls

    def class_log_decorated(method):
        def wrapper(*args, **kwargs):
            log_journal.append(method.__name__)
            return method(*args, **kwargs)

        return wrapper

    return decor


vector_log = []  # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def __repr__(self):
        return f'Vector({",".join(map(str, self.__coords))})'


if __name__ == '__main__':
    v = Vector(1, 2, 3, 4)
    coord1, coord2 = v[0], v[1]
    v[2] = 5
    print(v)
    print(vector_log)
