class Person:
    __slots__ = ('fio', 'job', 'old', 'salary', 'year_job')

    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __check_index(self, item):
        if not isinstance(item, int) and not 0 <= item < len(self.__slots__):
            raise IndexError('неверный индекс')

    def __getitem__(self, item):
        self.__check_index(item)
        return self.__slots__[item]


if __name__ == '__main__':
    p = Person('fio', 'sysadmin', 30, 3000, 12)
    job = p[1]
    print(job)
