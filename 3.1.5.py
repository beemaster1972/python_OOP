class Course:

    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        if isinstance(module, Module):
            self.modules.append(module)

    def remove_module(self, indx):
        if isinstance(indx, int):
            self.modules.pop(indx)


class Module:

    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        if isinstance(lesson, LessonItem):
            self.lessons.append(lesson)

    def remove_lesson(self, indx):
        if isinstance(indx, int):
            self.lessons.pop(indx)


class LessonItem:
    check_attr = {'title': str, 'practices': int, 'duration': int}
    def __init__(self, title: str, practices: int, duration: int):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if type(value) != self.check_attr[key] or (key in ('practices', 'duration') and value < 0):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        raise AttributeError('Нельзя удалять атрибуты класса')


# TEST-TASK___________________________________
course = Course("Python ООП")
assert type(course.name) is str, "название курса должно быть строкой"
assert type(course.modules) is list and len(course.modules) == 0, "modules должен быть списком, изначально список пуст"
# add_module(self, module) - добавление нового модуля в конце списка modules;
# remove_module(self, indx) - удаление модуля из списка modules по индексу в этом списке.
assert hasattr(course, 'add_module'), "add_module необъявлен"
assert hasattr(course, 'remove_module'), "remove_module необъявлен"

#
module_1 = Module("Часть первая")
module_2 = Module("Часть вторая")
assert type(module_1.name) is str, "название модуля должно быть строкой"
assert type(module_1.lessons) is list and len(
    module_1.lessons) == 0, "lesson должен быть списком, изначально список пуст"
# add_lesson(self, lesson) - добавление в модуль (в конец списка lessons) нового урока (объекта класса LessonItem);
# remove_lesson(self, indx) - удаление урока по индексу в списке lessons.
assert hasattr(module_1, "add_lesson"), "add_lesson необъявлен"
assert hasattr(module_1, "remove_lesson"), "remove_lesson необъявлен"

#
les_1 = LessonItem("Урок 1", 7, 1000)
les_2 = LessonItem("Урок 2", 10, 1200)
assert type(les_1.title) is str, "название урока должно быть строкой"
assert type(les_1.practices) is int and les_1.practices > 0, "practices должен быть целым числом больше ноля"
assert type(les_1.duration) is int and les_1.practices > 0, "duration должен быть целым положительным числом"

#
# проверка методов
course.add_module(module_1)
course.add_module(module_2)
assert len(course.modules) == 2 and course.modules[1] == module_2, "некоректно отработал метод add_module"
course.remove_module(0)
assert module_1 not in course.modules and len(course.modules) == 1, "некоректно отработал метод remove_module"
#
module_1.add_lesson(les_1)
module_1.add_lesson(les_2)
assert len(module_1.lessons) == 2 and module_1.lessons[1] == les_2, "некоректно отработал метод add_lesson"
module_1.remove_lesson(0)
assert les_1 not in module_1.lessons and len(module_1.lessons) == 1, "некоректно отработал метод remove_lesson"
#
# проверка методов - LessonItem
# 1. Проверять тип присваиваемых данных локальным атрибутам. Если типы не соответствуют требованиям, то генерировать исключение командой:
# raise TypeError("Неверный тип присваиваемых данных.")
try:
    les_3 = LessonItem(3, 8, 900)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при записи некорректных данных в title"

try:
    les_3 = LessonItem("Урок 2", 8.0, 900)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при записи некорректных данных в practices"

try:
    les_3 = LessonItem("Урок 2", 8, 900, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при записи некорректных данных в duration"

# 2. При обращении к несуществующим атрибутам объектов класса LessonItem возвращать значение False.
les_4 = LessonItem("Урок 2", 8, 900)
assert hasattr(les_1, "__getattr__"), \
    "ошибка при обращении к несуществующему локальному атрибуту, метод должен вернуть False"
assert les_4.value_not_atr is False, "ошибка при обращении к несуществующему локальному атрибуту, метод должен вернуть False"
# 3. Запретить удаление атрибутов title, practices и duration в объектах класса LessonItem.
assert hasattr(les_4, "__delattr__"), \
    "возможно вы не продумали запрет на удаление локальных атрибутов - title, practices и duration"
try:
    del les_4.title
    del les_4.practices
    del les_4.duration
except:
    ...
else:
    if any(True if _ not in les_4.__dict__ else False for _ in ["title", "practices", "duration"]):
        print('Ошибка при удалении локальных атрибутов - title, practices и duration')

print("Умница правильный ответ ))")