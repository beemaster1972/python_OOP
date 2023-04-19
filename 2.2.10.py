import re


class PhoneNumber:

    def __init__(self, number, fio):
        if self.__check(number):
            self.__number = number
        self.__fio = fio
        self.__next = None

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if self.__check(number):
            self.__number = number

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.__fio = fio

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next

    @staticmethod
    def __check(number):
        return type(number) is int and re.match(r'\d{11}', str(number))


class PhoneBook:

    def __init__(self):
        self.__head = None
        self.__tail = None

    def add_phone(self, phone):
        if type(phone) is PhoneNumber:
            if not self.__head:
                self.__head = phone
            if self.__tail:
                self.__tail.next = phone
            self.__tail = phone

    def get_phone_list(self):
        res = []
        if not self.__head:
            return res
        phone = self.__head
        res.append(phone)
        while phone.next:
            phone = phone.next
            res.append(phone)

        return res

    def remove_phone(self, indx):
        lst_phone = self.get_phone_list()
        if indx >= len(lst_phone)-1:
            self.__tail = lst_phone[len(lst_phone)-2]
            self.__tail.next = None
        else:
            lst_phone[indx-1].next = lst_phone[indx+1]


p = PhoneBook()

assert hasattr(p, 'add_phone'), 'ошибка метод add_phone не существует в объекте класса'

assert hasattr(p, 'get_phone_list'), 'ошибка метод get_phone_list не существует в объекте класса'

assert hasattr(p, 'remove_phone'), 'ошибка метод remove_phone не существует в объекте класса'

p_num_1 = PhoneNumber(12345678901, "Фамилия")

assert str(p_num_1.number).isdigit() and len(str(p_num_1.number)) == 11, "Длинна телефонного номера должна быть 11 цифр"

assert type(p_num_1.fio) is str and len(p_num_1.fio) >= 3, "Ф.И.О должна быть строкой, длинна не меньше 3 букв"
a = PhoneNumber(21345678901, "Панда")

b = PhoneNumber(12345678901, "Фамилия")

p.add_phone(a)

p.add_phone(b)

# проверяем что все добавленные объекты в списке

lst_user = p.get_phone_list()  # определяем имя пользовательского списка с телефонами

assert len(lst_user) == 2, "Метод add_phone отработал не правильно"
# проверка получение списка из объектов всех телефонных номеров

assert len(p.get_phone_list()) == 2 and all(isinstance(_, PhoneNumber) for _ in p.get_phone_list()), \
    "метод get_phone_list отработал не правильно"
# проверка удаления по индексу

rmv_obj = lst_user[1]  # определяем удаляемый объект

p.remove_phone(1)  # удаляем некий объект по индексу

# сравниваем удалили тот же объект или нет если в списке нет объекта rmv_obj то удаление работает правильно
lst_user = p.get_phone_list()
assert rmv_obj not in lst_user, "Метод remove_phone некорректно отработал !"
print("Правильный ответ !")

