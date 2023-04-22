class Exhibit:

    check_attr = {'name': str, 'descr': str}

    def __init__(self, name, descr, *args, **kwargs):
        self.name = name
        self.descr = descr

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

        setattr(exh, 'name', args[0])
        setattr(exh, 'descr', args[2])
        setattr(exh, 'author', args[1])
        return exh




class Mummies(Exhibit):

    def __new__(cls, *args, **kwargs):
        pass


pic = Picture('9 val', 2,' Aivazovsky is paint 9 val')
print(pic.name, pic.author, pic.descr)
