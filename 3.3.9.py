class Ingredient:

    def __init__(self, name, volume, measure):
        self.__name = name
        self.__volume = volume
        self.__measure = measure

    def __str__(self):
        return f'{self.__name}: {self.__volume}, {self.__measure}'


class Recipe:

    def __init__(self, *args):
        self.__ingrs = args
