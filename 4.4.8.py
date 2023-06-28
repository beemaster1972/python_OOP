class Aircraft:
    _attrs = {'_model': (str,), '_mass': (int, float), '_speed': (int, float), '_top': (int, float)}

    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def _check_attr(self, key, value):
        conditions = [tv := type(value) in self._attrs[key], value > 0 if tv in (int, float) else True]
        return all(conditions)

    def __setattr__(self, key, value):
        if not self._check_attr(key, value):
            raise TypeError(f'неверный тип аргумента {key} = {value}')
        object.__setattr__(self, key, value)

    def __repr__(self):
        attrs = [str(el) for key, el in self.__dict__.items()]
        return f'{self.__class__.__name__}({", ".join(attrs)})'


class PassengerAircraft(Aircraft):

    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._attrs.update({'_chairs': (int,)})
        self._chairs = chairs


class WarPlane(Aircraft):

    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._attrs.update({'_weapons': (dict,)})
        self._weapons = weapons


if __name__ == '__main__':
    input_data = """PassengerAircraft:: 'МС-21', 1250, 8000, 12000.5, 140
    PassengerAircraft:: 'SuperJet', 1145, 8640, 11034, 80
    WarPlane:: 'Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}
    WarPlane:: 'Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7}""".splitlines()
    lst = [el.split("::") for el in input_data]
    planes = [eval(f"{x[0].strip()}({x[1].strip()})") for x in lst]
    print(*planes, sep='\n')


    planes[2]._weapons['ракета'] = 3
    print(*planes, sep='\n')
