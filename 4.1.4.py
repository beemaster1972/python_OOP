class Animal:

    def __init__(self, name, old):
        self.name = name
        self.old = old

    def get_info(self):
        return f'{self.name}: {self.old}, '


class Cat(Animal):

    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self):
        return super(Cat, self).get_info()+f'{self.color}, {self.weight}'


class Dog(Animal):

    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self):
        return super(Dog, self).get_info() + f'{self.breed}, {self.size}'


if __name__ == '__main__':
    cat = Cat("Tom", 3, "white", 3.5)
    dog = Dog("Archi", 1, "Carry blue terier", (0.5, 0.7))
    print(cat.get_info())
    print(dog.get_info())
