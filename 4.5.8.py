from abc import ABC, abstractmethod


class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @population.setter
    @abstractmethod
    def population(self, value):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @square.setter
    @abstractmethod
    def square(self, value):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):

    def __init__(self, name, population, square):
        self.__name = name
        self.population = population
        self.square = square

    @property
    def name(self):
        return self.__name

    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, value):
        if type(value) == int and value >= 0:
            self.__population = value

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, value):
        if type(value) in (int, float) and value > 0:
            self.__square = value

    def get_info(self):
        return f'{self.name}: {self.square}, {self.population}'


if __name__ == '__main__':
    country = Country("Россия", 140000000, 324005489.55)
    name = country.name
    pop = country.population
    country.population = 150000000
    country.square = 354005483.0
    print(country.get_info())  # Россия: 354005483.0, 150000000
