class IteratorAttrs:

    def __iter__(self):
        for key, val in self.__dict__.items():
            yield key, val


class SmartPhone(IteratorAttrs):

    def __init__(self, model: str, size: tuple, memory: int):
        self.model = model
        self.size = size
        self.memory = memory


if __name__ == '__main__':
    phone = SmartPhone('Samsung Galaxy S22 Ultra', (8, 17), 256)
    for i, j in phone:
        print(i, j)
