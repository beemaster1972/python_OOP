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


class Papyri(Exhibit):
    def __new__(cls, *args, **kwargs):
        exh = super().__new__(cls)
        exh.check_attr = Exhibit.check_attr
        exh.check_attr['date'] = str
        setattr(exh, 'date', args[1])
        return exh


class Museum:

    def __init__(self, name: str):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj):
        self.exhibits.append(obj)

    def remove_exhibit(self, obj):
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        if indx < len(self.exhibits):
            name = self.exhibits[indx].name
            descr = self.exhibits[indx].descr
        else:
            name = 'Не известно'
            descr = 'Не известно'
        return f"Описание экспоната {name}: {descr}"


# TEST-TASK___________________________________
mus = Museum("Эрмитаж")
assert type(mus.name) is str, "название должно быть строкой"
assert mus.exhibits == [], "exhibits должен быть списком"
assert hasattr(mus, "add_exhibit"), "метод не объявлен"
assert hasattr(mus, "remove_exhibit"), "метод не объявлен"
assert hasattr(mus, "get_info_exhibit"), "метод не объявлен"

pic = Picture("Балакирев с подписчиками пишет письмо иноземному султану", "Неизвестный автор",
              "Вдохновляющая, устрашающая, волнующая картина")
assert 'name' in pic.__dict__.keys() and 'descr' in pic.__dict__.keys() and 'author' in pic.__dict__.keys(), "ошибка в локальных атрибутах"

mum = Mummies("Балакирев", "Древняя Россия", "Просветитель XXI века, удостоенный мумификации")
assert 'name' in mum.__dict__.keys() and 'location' in mum.__dict__.keys() and 'descr' in mum.__dict__.keys(), "ошибка в локальных атрибутах"

p = Papyri("Ученья для, не злата ради",
           "Древняя Россия",
           "Самое древнее найденное рукописное свидетельство о языках программирования")
assert 'name' in p.__dict__.keys(), "ошибка в локальном атрибуте name"
assert 'date' in p.__dict__.keys(), "ошибка в локальном атрибуте date"
assert 'descr' in p.__dict__.keys(), "ошибка в локальном атрибуте descr"
assert type(p.date) is str, "название должно быть строкой"


mus.add_exhibit(pic)
assert mus.exhibits[0] == pic and len(mus.exhibits) == 1, "некорректно отработал метод add_exhibit"

mus.remove_exhibit(pic)
assert len(mus.exhibits) == 0 and pic not in mus.exhibits, "некорректно отработал метод remove_exhibit"

mus.add_exhibit(p)
mus.add_exhibit(pic)
answ = mus.get_info_exhibit(0)
assert answ == f"Описание экспоната {mus.exhibits[0].name}: {mus.exhibits[0].descr}", "некорректно отработал метод get_info_exhibit"
print("Правильный ответ.")
