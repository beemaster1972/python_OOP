import random


class RandomPassword:

    def __init__(self, psw_chars: str, min_length: int, max_length: int):
        self.__psw_chars = psw_chars
        self.__min_length = min_length
        self.__max_length = max_length

    def __call__(self, *args, **kwargs):
        length = random.randrange(self.__min_length, self.__max_length)
        psw = list(self.__psw_chars)
        random.shuffle(psw)
        return ''.join(random.choices(psw, k=length))


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [rnd() for _ in range(3)]
print(*lst_pass)
