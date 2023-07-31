class ValidatorString:

    def __init__(self, min_length, max_length, chars):
        self._min_length = min_length
        self._max_length = max_length
        self._chars = chars

    def is_valid(self, string):
        conditions = [self._min_length <= len(string) <= self._max_length,
                      set(string).intersection(set(self._chars)) if self._chars else True]
        if not all(conditions):
            raise ValueError('недопустимая строка')
        return string

    def __call__(self, string):
        return self.is_valid(string)

class LoginForm:

    def __init__(self, login_validator, password_validator):
        self._login_validator = login_validator
        self._password_validator = password_validator
        self._login = None
        self._password = None

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = self._login_validator(value)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = self._password_validator(value)

    def form(self, request):
        conditions = [type(request) is dict, request.get('login', False), request.get('password', False)]
        if not all(conditions):
            raise TypeError('в запросе отсутствует логин или пароль')
        self.login = conditions[1]
        self.password = conditions[2]


if __name__ == '__main__':
    login_v = ValidatorString(4, 50, "")
    password_v = ValidatorString(10, 50, "!$#@%&?")
    lg = LoginForm(login_v, password_v)
    login, password = input().split()
    try:
        lg.form({'login': login, 'password': password})
    except (TypeError, ValueError) as e:
        print(e)
    else:
        print(lg.login)
