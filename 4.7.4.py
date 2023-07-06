class Person:
    __slots__ = ('_fio', '_old', '_job')

    def __init__(self, fio, old, job):
        self._fio = fio
        self._old = old
        self._job = job

    def __repr__(self):
        return f'Person({", ".join([self._fio,str(self._old),str(self._job)])})'


if __name__ == '__main__':
    input_data = """Суворов, 52, полководец
Рахманинов, 50, пианист, композитор
Балакирев, 34, программист и преподаватель
Пушкин, 32, поэт и писатель""".splitlines()

    persons = [Person(fio.strip(), int(old.strip()), job.strip()) for l in input_data for fio, old, job in
               [l.split(",", maxsplit=2)]]