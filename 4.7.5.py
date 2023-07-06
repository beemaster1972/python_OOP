class Planet:
    __slots__ = ('_name', '_diametr', '_period_solar', '_period')

    def __init__(self, *args):
        for i, attr in enumerate(self.__slots__):
            setattr(self, attr, args[i])

    def __setattr__(self, key, value):
        if key != '_name':
            if type(value) not in (int, float):
                raise TypeError(f"Свойство {key} может быть только числом")
            elif value <= 0:
                raise ValueError(f"Свойство {key} может быть только положительным")
        object.__setattr__(self, key, value)

    def __str__(self):
        return f'Планета {self._name} D={self._diametr} км. Год равен {self._period_solar} суткам. Сутки составляют {self._period} часа'


class SolarSystem:
    __instance = None
    __slots__ = ("_mercury", "_venus", "_earth", "_mars", "_jupiter", "_saturn", "_uranus", "_neptune")
    planet_data = """Меркурий,4878,87.97,1407.5
Венера,12 104,224.7,5832.45
Земля,12 756,365.3,23.93
Марс,6794,687,24.62
Юпитер,142 800,4330,9.9
Сатурн,120 660,10753,10.63
Уран,51 118,30665,17.2
Нептун,49 528,60150,16.1""".splitlines()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        for _, attr in enumerate(self.__slots__):
            attrs = [el if el.isalpha() else float(el.replace(" ", "")) for el in self.planet_data[_].split(",")]
            setattr(self, attr, Planet(*attrs))

    def __str__(self):
        return "\n".join([str(getattr(self, el)) for el in self.__slots__])


if __name__ == '__main__':
    solar_system = SolarSystem()
    print(solar_system)
