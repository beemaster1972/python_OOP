class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


class Game(Singleton):

    def __init__(self, name):
        if not hasattr(self, 'name'):
            self.name = name


if __name__ == '__main__':
    g1 = Game('Spider')
    print(g1)
    g2 = Game('Miner')
    g3 = Game('Solider')

    print(g1, g2, g3)
    print(g1.name, g2.name, g3.name)
