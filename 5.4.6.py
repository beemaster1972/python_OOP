class DateError(Exception):
    """Ошибка формата даты"""

    def __str__(self):
        return "Неверный формат даты"


class DateString:

    def __init__(self, date_string):
        self._date = self.__check_format(date_string)

    def __str__(self):
        return f'{self._date["day"]:02}.{self._date["month"]:02}.{self._date["year"]}'

    def __check_format(self, st):
        try:
            day, month, year = map(int, st.split("."))
        except (TypeError, ValueError):
            raise DateError()
        else:
            if not (0 < day < 32 and 0 < month < 13):
                raise DateError()
            res = {'day': day, 'month': month, 'year': year}
            return res


if __name__ == '__main__':
    date = DateString('asadd')
    print(date)
