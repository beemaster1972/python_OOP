class Protists:

    def __init__(self, name: str, weight: float, old: int):
        self.name = name
        self.weight = weight
        self.old = old

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.weight}, {self.old})'


class Plants(Protists):
    pass


class Animals(Protists):
    pass


class Mosses(Plants):
    pass


class Flowering(Plants):
    pass


class Worms(Animals):
    pass


class Mammals(Animals):
    pass


class Human(Mammals):
    pass


class Monkeys(Mammals):
    pass


class Monkey(Monkeys):
    pass


class Person(Human):
    pass


class Flower(Flowering):
    pass


class Worm(Worms):
    pass


if __name__ == '__main__':
    objects_string = ('Monkey, "мартышка", 30.4, 7',
                      'Monkey, "шимпанзе", 24.6, 8',
                      'Person, "Балакирев", 88, 34',
                      'Person, "Верховный жрец", 67.5, 45',
                      'Flower, "Тюльпан", 0.2, 1',
                      'Flower, "Роза", 0.1, 2',
                      'Worm, "червь", 0.01, 1',
                      'Worm, "червь 2", 0.02, 1')
    lst_objs = []
    for obj in objects_string:
        s = obj.split(",")
        lst_objs.append(eval(f'{s[0]}({s[1]}, {float(s[2])}, {int(s[3])})'))
    lst_animals = [obj for obj in lst_objs if isinstance(obj, Animals)]
    lst_plants = [obj for obj in lst_objs if isinstance(obj, Plants)]
    lst_mammals = [obj for obj in lst_objs if isinstance(obj, Mammals)]
    print(lst_objs)
    print(lst_animals)
    print(lst_mammals)
    print(lst_plants)
