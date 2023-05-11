class Clock:

    def __init__(self, h: int = 0, m: int = 0, s: int = 0):
        self.__hours = h
        self.__minutes = m
        self.__seconds = s

    def __setattr__(self, key, value):
        if key not in ('_Clock__hours', '_Clock__minutes', '_Clock__seconds'):
            return False
        if isinstance(value, int):
            object.__setattr__(self, key, value)
        elif not hasattr(self, key):
            object.__setattr__(self, key, 0)

    def get_time(self):
        return self.__hours*3600+self.__minutes*60+self.__seconds

    def __call__(self, *args, **kwargs):
        return self.get_time()


class DeltaClock:

    def __init__(self, clock1: Clock, clock2: Clock):
        self.__clock1 = clock1
        self.__clock2 = clock2

    def __len__(self):
        return self.__clock1() - self.__clock2() if self.__clock1() >= self.__clock2() else 0

    def __str__(self):
        h = str(len(self) // 3600).zfill(2)
        m = str((len(self) % 3600) // 60).zfill(2)
        s = str(len(self) % 60).zfill(2)
        return f'{h}: {m}: {s}'


dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
print(dt)  # 01: 30: 00
len_dt = len(dt)  # 5400
print(len_dt)
