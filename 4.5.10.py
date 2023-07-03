class Food:
    _base_attrs = {'_name': (str,), '_weight': (int, float), '_calories': (int, float)}
    _child_attrs = {}

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(tuple(self._base_attrs.keys()) + tuple(self._child_attrs.keys()), args))
        if self._check_attrs(attrs):
            self.__dict__.update(attrs)
        if self._check_attrs(kwargs):
            self.__dict__.update(kwargs)

    def _check_attrs(self, attrs, ):
        all_attrs = self._base_attrs.copy()
        all_attrs.update(self._child_attrs)
        for key, val in attrs.items():
            if not isinstance(attrs[key], all_attrs.get(key)):
                raise TypeError(f'Неверный тип для значения {val} атрибута {key}')
            if all_attrs[key] == (int, float) and val < 0:
                raise ValueError(f'Значение для {key} должно быть положительным')
        return True

    def __repr__(self):
        return f'{self.__class__.__name__}({",".join(map(str, self.__dict__.values()))})'


class BreadFood(Food):
    """ хлеб """
    _child_attrs = {'_white': (bool,)}


class SoupFood(Food):
    """ суп """
    _child_attrs = {'_dietary': (bool,)}


class FishFood(Food):
    """ рыба """
    _child_attrs = {'_fish': (str,)}


if __name__ == '__main__':
    bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
    sf = SoupFood("Черепаший суп", 520, 890.5, False)
    ff = FishFood("Консерва рыбная", 340, 1200, "семга")
    print(bf, sf, ff)
