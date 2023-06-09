class Person:
    _slots = ('fio', 'job', 'old', 'salary', 'year_job')

    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.__index = -1

    def __check_index(self, item):
        if not isinstance(item, int) and not 0 <= item < len(self.__slots__):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.__dict__[Person._slots[item]]

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.__dict__[Person._slots[key]] = value

    def __next__(self):
        self.__index += 1
        if self.__index < len(Person._slots):
            return self.__dict__[Person._slots[self.__index]]
        raise StopIteration

    def __iter__(self):
        self.__index = -1
        return self

if __name__ == '__main__':
    p = Person('fio', 'job', 30, 3000, 12)
    for v in p:
        print(v)
    p[0] = "D. R. Yanno"
    p[1] = "sysadmin"
    for v in p:
        print(v)
