class Star:
    __slots__ = ("_name", "_massa", "_temp")
    _string_properties = ["_name"]

    def __init__(self, name, massa, temp):
        self._name = name
        self._massa = massa
        self._temp = temp

    def __setattr__(self, key, value):
        if key not in self._string_properties:
            if type(value) not in (int, float):
                raise TypeError(f"Свойство {key} должно быть числом ({value})")
            elif value <= 0:
                raise ValueError(f"Свойство {key} должно быть положительным")
        object.__setattr__(self, key, value)

    def __repr__(self):
        attrs = [str(getattr(self, v)) for prnts in reversed(self.__class__.mro()) if hasattr(prnts,"__slots__") for v in prnts.__slots__]
        return f"{self.__class__.__name__}({', '.join(attrs)})"


class WhiteDwarf(Star):
    __slots__ = ("_type_star", "_radius")
    _string_properties = Star._string_properties + ["_type_star"]

    def __init__(self, *args):
        super().__init__(*args[:3])
        self._type_star, self._radius = args[3:]


class YellowDwarf(Star):
    __slots__ = ("_type_star", "_radius")
    _string_properties = Star._string_properties + ["_type_star"]

    def __init__(self, *args):
        super().__init__(*args[:3])
        self._type_star, self._radius = args[3:]


class RedGiant(Star):
    __slots__ = ("_type_star", "_radius")
    _string_properties = Star._string_properties + ["_type_star"]

    def __init__(self, *args):
        super().__init__(*args[:3])
        self._type_star, self._radius = args[3:]


class Pulsar(Star):
    __slots__ = ("_type_star", "_radius")
    _string_properties = Star._string_properties + ["_type_star"]

    def __init__(self, *args):
        super().__init__(*args[:3])
        self._type_star, self._radius = args[3:]


if __name__ == '__main__':
    input_data = """RedGiant: Альдебаран; 5; 3600; красный гигант; 45
WhiteDwarf: Сириус А; 2,1; 9250; белый карлик; 2
WhiteDwarf: Сириус B; 1; 8200; белый карлик; 0,01
YellowDwarf: Солнце; 1; 6000; желтый карлик; 1""".replace(",", ".").splitlines()
    input_data = [l.split(": ") for l in input_data]
    stars = [eval(
        f"{el[0]}({','.join([chr(39) + attr + chr(39) if attr.isalpha() or attr.find(' ') > 0 else attr for attr in el[1].split('; ')])})")
        for el in input_data]
    white_dwarfs = [wd for wd in filter(lambda x: isinstance(x, WhiteDwarf), stars)]
