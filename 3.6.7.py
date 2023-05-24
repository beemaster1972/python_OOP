class DataBase:

    def __init__(self, path):
        self.path = path
        self.__dict_db = {}

    @property
    def dict_db(self):
        return self.__dict_db

    def write(self, record):
        try:
            self.__dict_db[record].append(record)
        except KeyError:
            self.__dict_db[record] = [record]

    def read(self, pk):
        return [x for y in self.__dict_db.values() for x in y if x.pk == pk][0]

    def __repr__(self):
        return f'{self.path}'


class Record:
    __INDEX = 0

    def __init__(self, fio: str, descr: str, old):
        self.__fio = fio.strip()
        self.__descr = descr.strip()
        self.__old = old if isinstance(old, int) else int(old)
        self.__pk = Record.__INDEX
        Record.__INDEX += 1

    @property
    def pk(self):
        return self.__pk

    @property
    def fio(self):
        return self.__fio

    @property
    def descr(self):
        return self.__descr

    @property
    def old(self):
        return self.__old

    def __hash__(self):
        return hash((self.__fio.lower(), self.__old))

    def __eq__(self, other):
        if not isinstance(other, Record):
            raise TypeError('Второй операнд должен быть типа Record')
        return hash(self) == hash(other)

    def __repr__(self):
        return f'{self.fio} {self.descr} {self.old}'


db = DataBase('PATH')
lst_in = [input() for _ in range(5)]

for i, st in enumerate(lst_in):
    fio, descr, old = st.split(';')
    db.write(Record(fio, descr, old))

db22345 = DataBase('123')
r1 = Record('fio', 'descr', 10)
r2 = Record('fio', 'descr', 10)
assert r1.pk != r2.pk, "равные значения атрибута pk у разных объектов класса Record"

db22345.write(r2)
r22 = db22345.read(r2.pk)
assert r22.pk == r2.pk and r22.fio == r2.fio and r22.descr == r2.descr and r22.old == r2.old, "при операциях write и read прочитанный объект имеет неверные значения атрибутов"

assert len(db22345.dict_db) == 1, "неверное число объектов в словаре dict_db"

fio = lst_in[0].split(';')[0].strip()
v = list(db.dict_db.values())
if fio == "Балакирев С.М.":
    assert len(v[0]) == 2 and len(v[1]) == 1 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"

if fio == "Гейтс Б.":
    assert len(v[0]) == 2 and len(v[1]) == 2 and len(v[2]) == 1 and len(
        v[3]) == 1, "неверно сформирован словарь dict_db"

print("Всё сделано правильно!!!")
