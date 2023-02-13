from string import ascii_lowercase, digits
import re


class CardCheck:
    CHARS_FOR_NAME = set(ascii_lowercase.upper() + digits + ' ')

    @staticmethod
    def check_card_number(number):
        return re.match(r'^\d{4}-\d{4}-\d{4}-\d{4}$',number) is not None # and len(number) == 19

    @classmethod
    def check_name(cls, name):
        return cls.CHARS_FOR_NAME.intersection(set(name)) == set(name) and len(re.split(r' ', name)) == 2

print(CardCheck.check_name('DMITRY YANNO'))
print(CardCheck.check_card_number('1244-5678-9012-0000-1234-ABCD'))
print()
