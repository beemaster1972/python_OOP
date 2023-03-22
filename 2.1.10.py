import random as rn
from string import ascii_lowercase, digits
class EmailValidator:

    VALID_CHARS = ascii_lowercase + digits + '_' + '.'+'@'
    def __new__(cls, *args, **kwargs):
        return None
    @staticmethod
    def __is_email_str(email):
        return type(email) is str

    @staticmethod
    def chek_dots_in_domain(domain: str):
        if not domain.count('.'):
            return False
        if domain.count('.') == 1:
            return True
        ind = [domain.index('.')]
        for i in range(1, domain.count('.')):
            ind.append(domain.index('.', ind[i-1]+1))
            if ind[i-1]+1 == ind[i]:
                return False
        return True


    @classmethod
    def check_email(cls, email: str):
        if not cls.__is_email_str(email):
            return False
        eml = email.split('@')

        return email.count('@') == 1 and len(eml[0]) <= 100 and len(eml[1]) <= 50 and eml[1].count('.') >= 1 \
               and cls.chek_dots_in_domain(email) and set(email) & set(cls.VALID_CHARS) == set(email)

    @classmethod
    def get_random_email(cls, domain="@gmail.com"):
        while True:
            email = ''.join(rn.sample(cls.VALID_CHARS[:-2] * 4, rn.randint(1, 100)))
            if cls.check_email(email+domain):
                return email+domain




assert EmailValidator.check_email("sc_lib@list.ru") == True, "метод check_email отработал некорректно"
assert EmailValidator.check_email("sc_lib@list_ru") == False, "метод check_email отработал некорректно"
assert EmailValidator.check_email("sc@lib@list_ru") == False, "метод check_email отработал некорректно"
assert EmailValidator.check_email("sc.lib@list_ru") == False, "метод check_email отработал некорректно"
assert EmailValidator.check_email("sclib@list.ru") == True, "метод check_email отработал некорректно"
assert EmailValidator.check_email("sc.lib@listru") == False, "метод check_email отработал некорректно"
assert EmailValidator.check_email("sc..lib@list.ru") == False, "метод check_email отработал некорректно"

m = EmailValidator.get_random_email()
assert EmailValidator.check_email(m) == True, "метод check_email забраковал сгенерированный email методом get_random_email"

assert EmailValidator() is None, "при создании объекта класса EmailValidator возвратилось значение отличное от None"

assert EmailValidator._EmailValidator__is_email_str('abc'), "метод __is_email_str() вернул False для строки"
assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaa") == True
assert EmailValidator.check_email("i.like.this.course@my.stepik.domen.org") == True
assert EmailValidator.check_email('name.surname@mail.com') == True
assert EmailValidator.check_email(1342) == False
assert EmailValidator.check_email('a+a@m.c') == False
assert EmailValidator.check_email('aabda..kkk@m.c') == False
assert EmailValidator.check_email('aaaa@bbb..cc') == False
assert EmailValidator.check_email(f"{'a' * 100}@{'b' * 45}.aaaaa") == False
assert EmailValidator.check_email(f"{'a' * 101}@{'b' * 45}.aaaa") == False
assert EmailValidator.check_email(f"{'a'}@{'b' * 45}aaaa") == False
assert EmailValidator.check_email('name.surnamemail.com') == False
assert EmailValidator.check_email('name@mail') == False