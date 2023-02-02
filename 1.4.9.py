import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def select(self, a, b):
        return [self.lst_data[i] for i in range(a,min(b,len(self.lst_data)))]


    def insert(self, data):
        for elem in data:
            print(list(elem.split()))
            self.lst_data.append(dict(zip(self.FIELDS,elem.split())))


db = DataBase()
db.insert(lst_in)
print(db.select(0,10))