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


class PassengerAircraft(Aircraft):

    def __init__(self, ):
        super.__init__()