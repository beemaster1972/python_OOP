class Clock:

    def __init__(self, time: int = 0):
        self.__time = 0
        if self.__check_time(time):
            self.__time = time

    @classmethod
    def __check_time(cls, tm):
        return type(tm) in (int,) and 0 <= tm <= 100_000

    def set_time(self, time):
        if self.__check_time(time):
            self.__time = time

    def get_time(self):
        return self.__time


if __name__ == '__main__':
    clock = Clock(4530)
    assert isinstance(clock, Clock) and hasattr(Clock, 'set_time') and hasattr(Clock, 'get_time'), "в классе Clock присутствуют не все методы"

    assert clock.get_time() == 4530, "текущее время в объекте clock не равно 4530"

    clock.set_time(10)
    assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"
    clock.set_time(-10)
    assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"
    clock.set_time(1000001)
    assert clock.get_time() == 10, "неверное текущее время, некорректно работает метод set_time"