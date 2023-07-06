class Star:
    __slots__ = ("_name", "_massa", "_temp")
    _string_properties = ["_name"]

    def __init__(self, *args):
        for _, attr in enumerate(self.__slots__):
            setattr(self, attr, args[_])

    def __setattr__(self, key, value):
        if key not in self._string_properties:
            if type(value) not in (int, float):
                raise TypeError(f"Свойство {key} должно быть числом ({value})")
            elif value <= 0:
                raise ValueError(f"Свойство {key} должно быть положительным")
        object.__setattr__(self, key, value)

    def __repr__(self):
        if self.__class__ is not Star:
            attrs = [str(getattr(super, v)) for v in super(self.__class__).__slots__]+[str(getattr(self, v)) for v in self.__slots__]
        return f"{self.__class__.__name__}({', '.join(attrs)})"


class WhiteDwarf(Star):
    __slots__ = "_type_star", "_radius"
    _string_properties = Star._string_properties + ["_type_star"]


class YellowDwarf(Star):
    __slots__ = "_type_star", "_radius"
    _string_properties = Star._string_properties + ["_type_star"]


class RedGiant(Star):
    __slots__ = "_type_star", "_radius"
    _string_properties = Star._string_properties + ["_type_star"]


class Pulsar(Star):
    __slots__ = "_type_star", "_radius"
    _string_properties = Star._string_properties + ["_type_star"]


if __name__ == '__main__':
    input_data = """RedGiant: Альдебаран; 5; 3600; красный гигант; 45
WhiteDwarf: Сириус А; 2,1; 9250; белый карлик; 2
WhiteDwarf: Сириус B; 1; 8200; белый карлик; 0,01
YellowDwarf: Солнце; 1; 6000; желтый карлик; 1""".replace(",", ".").splitlines()
    input_data = [l.split(": ") for l in input_data]
    stars = [eval(
        f"{el[0]}({','.join([chr(39) + attr + chr(39) if attr.isalpha() or attr.find(' ') > 0 else attr for attr in el[1].split('; ')])})")
             for el in input_data]
    print(*stars, sep="\n")
