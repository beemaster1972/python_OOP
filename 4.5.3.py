class Student:
    def __init__(self, fio, group):
        self._fio = fio
        self._group = group
        self._lect_marks = []  # оценки за лекции
        self._house_marks = []  # оценки за домашние задания

    def add_lect_marks(self, mark):
        self._lect_marks.append(mark)

    def add_house_marks(self, mark):
        self._house_marks.append(mark)

    def __str__(self):
        return f"Студент {self._fio}: оценки на лекциях: {str(self._lect_marks)}; оценки за д/з: {str(self._house_marks)}"


class Mentor:
    _title = "Препод"

    def __init__(self, fio, subject):
        self._fio = fio
        self._subject = subject

    def __str__(self):
        return f'{self._title} {self._fio}: предмет {self._subject}'


# здесь продолжайте программу
class Lector(Mentor):
    _title = "Лектор"

    def set_mark(self, student, mark):
        student.add_lect_marks(mark)


class Reviewer(Mentor):
    _title = "Эксперт"

    def set_mark(self, student, mark):
        student.add_house_marks(mark)


if __name__ == '__main__':
    lector = Lector("Балакирев С.М.", "Информатика")
    print(lector)
    assert str(lector) == "Лектор Балакирев С.М.: предмет Информатика", "неверно отработал метод __str__ класса Lector"
    reviewer = Reviewer("Гейтс Б.", "Информатика")
    students = [Student("Иванов А.Б.", "ЭВМд-11"), Student("Гаврилов С.А.", "ЭВМд-11")]
    persons = [lector, reviewer]
    lector.set_mark(students[0], 4)
    lector.set_mark(students[1], 2)
    reviewer.set_mark(students[0], 5)
    reviewer.set_mark(students[1], 3)
    for p in persons + students:
        print(p)