class Exhibit:

    check_attr = {'name': str, 'descr': str}

    def __init__(self, name, descr):
        self.name = name
        self.descr = descr

    def __setattr__(self, key, value):
        if type(value) != self.check_attr[key] and not self.check_value():
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def check_value(self):
        return True


class Picture(Exhibit):


    def __new__(cls, *args, **kwargs):
        check_attr = Exhibit.check_attr
        check_attr['author'] = str
        exh = super().__new__(Exhibit)
        setattr(exh, 'name', args[0])
        setattr(exh, 'descr', args[2])
        setattr(exh, 'author', args[1])
        return exh




class Mummies(Exhibit):

    def __new__(cls, *args, **kwargs):
        pass


pic = Picture(1, 'Serov',' Serov is paint Gauss')
print(pic.name, pic.author, pic.descr)
