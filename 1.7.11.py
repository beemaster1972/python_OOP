class Message:

    def __init__(self, text='', like=False):
        self.text = text
        self.fl_like = like


class Viber:
    LIST_MSG = []

    @classmethod
    def add_message(cls, msg):
        cls.LIST_MSG.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.LIST_MSG.remove(msg)

    @classmethod
    def set_like(cls, msg):
        cls.LIST_MSG[cls.LIST_MSG.index(msg)].fl_like = not cls.LIST_MSG[cls.LIST_MSG.index(msg)].fl_like

    @classmethod
    def show_last_message(cls, cnt_last_msgs):
        for msg in cls.LIST_MSG[-cnt_last_msgs:]: #cls.LIST_MSG[-1:min(cnt_last_msgs+1, len(cls.LIST_MSG))*-1:-1]:
            print(msg.text)

    @classmethod
    def total_messages(cls):
        return len(cls.LIST_MSG)




assert hasattr(Viber, 'show_last_message'), "отсутствует метод show_last_message"

msg = Message("Всем привет!")
Viber.add_message(msg)
assert Viber.total_messages() == 1, "сообщение не было добавлено: некорректно работает метод add_message"

Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.show_last_message(2)
assert Viber.total_messages() == 3, "неверное число сообщений: некорректно работает метод add_message"

assert msg.fl_like == False, "лайка по умолчанию не должно быть - значение False"
Viber.set_like(msg)
assert msg.fl_like == True, "лайк не проставился: некорректно работает метод set_like"
Viber.set_like(msg)
assert msg.fl_like == False, "лайк не убрался при повторном вызове метода set_like"
Viber.remove_message(msg)

assert Viber.total_messages() == 2, "неверное число сообщений: некорректно работает метод remove_message"
