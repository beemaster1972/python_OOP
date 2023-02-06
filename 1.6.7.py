class SingletonFive:

    __instance = []

    def __new__(cls, *args, **kwargs):
        if len(cls.__instance) < 5:
            cls.__instance.append(super().__new__(cls))
        return cls.__instance[-1]

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
for obj in objs:
    print (obj.name)