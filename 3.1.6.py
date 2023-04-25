class Exhibit:

    check_attr = {'name': str, 'descr': str}

    def __init__(self, *args, **kwargs):
        self.name = args[0]
        self.descr = args[2]

    def __setattr__(self, key, value):
        if key in self.check_attr:
            if type(value) != self.check_attr[key] and not self.check_value():
                raise TypeError(f"Неверный тип присваиваемых данных в переменную {key} = {value}.")

        object.__setattr__(self, key, value)

    def check_value(self):
        return False


class Picture(Exhibit):

    def __new__(cls, *args, **kwargs):
        exh = super().__new__(cls)
        exh.check_attr = Exhibit.check_attr
        exh.check_attr['author'] = str
        setattr(exh, 'author', args[1])
        return exh


class Mummies(Exhibit):

    def __new__(cls, *args, **kwargs):
        exh = super().__new__(cls)
        exh.check_attr = Exhibit.check_attr
        exh.check_attr['location'] = str
        setattr(exh, 'location', args[1])
        return exh


class Papyri:
    def __new__(cls, *args, **kwargs):
        exh = super().__new__(cls)
        exh.check_attr = Exhibit.check_attr
        exh.check_attr['date'] = str
        setattr(exh, 'date', args[1])
        return exh


class Museum:
    pass


pic = Picture('9 val', 'Aivazovsky', ' Aivazovsky was paint 9 val')
print(pic.name, pic.author, pic.descr)
