class Thing:

    def __init__(self, *args):
        self.name, self. weight = args


class ArtObject(Thing):

    def __init__(self, *args):
        super().__init__(*args[:2])
        self.author, self.date = args[-2:]


class Computer(Thing):

    def __init__(self, *args):
        super().__init__(*args[:2])
        self.memory, self.cpu = args[-2:]


class Auto(Thing):

    def __init__(self, *args):
        super().__init__(*args[:2])
        self.dims = args[-1:]


class Mercedes(Auto):

    def __init__(self, *args):
        super().__init__(*args[:3])
        self.model, self.old = args[-2:]


class Toyota(Auto):

    def __init__(self, *args):
        super().__init__(*args[:3])
        self.model, self.wheel = args[-2:]

