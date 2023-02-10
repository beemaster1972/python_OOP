import string


class SomeInput:

    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + string.ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + string.digits

    def __init__(self, name: str, size=10):
        if SomeInput.check_name(name):
            self.name = name
            self.size = size

    @classmethod
    def check_name(cls, name):
        if 3 <= len(name) <= 50 and set(name).intersection(set(cls.CHARS_CORRECT)) == set(name):
            return True
        else:
            raise ValueError(f"некорректное поле {name}")


class TextInput(SomeInput):

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput(SomeInput):

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
print(html)
